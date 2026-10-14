import numpy as np
import open3d as o3d

#%% 2. Generate a synthetic point cloud

num_points = 2000
plane_points = np.random.rand(num_points // 2, 3)
plane_points[:, 2] = 0.1 * np.random.rand(num_points // 2) + 1  # Add some noise to z-coordinate

sphere_center = np.array([2, 2, 2])
sphere_radius = 1
theta = np.random.uniform(0, 2*np.pi, num_points // 2)
phi = np.random.uniform(0, np.pi, num_points // 2)

x = sphere_center[0] + sphere_radius * np.sin(phi) * np.cos(theta)
y = sphere_center[1] + sphere_radius * np.sin(phi) * np.sin(theta)
z = sphere_center[2] + sphere_radius * np.cos(phi)

sphere_points = np.column_stack((x, y, z))
sphere_points += 0.05 * np.random.randn(*sphere_points.shape)  # Add some noise

points = np.vstack((plane_points, sphere_points))

pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points)

""" o3d.visualization.draw_geometries([pcd]) """

#%% 3. Define the RANSAC functions

def ransac_plane(points, num_iterations=1000, threshold=0.1):
    best_inliers = []
    best_plane = None

    for _ in range(num_iterations):

        # Randomly sample 3 points
        sample_indices = np.random.choice(len(points), 3, replace=False)
        sample = points[sample_indices]

        # Calculate plane equation ax + by + cz + d = 0
        v1 = sample[1] - sample[0]
        v2 = sample[2] - sample[0]

        # Normal vector to the plane
        normal = np.cross(v1, v2)

        # Normalize the normal vector
        normal = normal / np.linalg.norm(normal)

        a, b, c = normal

        # Calculate d
        d = -np.dot(normal, sample[0])

        # Calculate distances of all points to the plane
        distances = np.abs(
            a * points[:, 0]
            + b * points[:, 1]
            + c * points[:, 2]
            + d
        )

        # Count inliers
        inliers = np.where(distances < threshold)[0]

        if len(inliers) > len(best_inliers):
            best_inliers = inliers
            best_plane = (a, b, c, d)

    return best_plane, best_inliers


def ransac_sphere(points, num_iterations=1000, threshold=0.1):
    best_inliers = []
    best_sphere = None

    for _ in range(num_iterations):

        # Randomly sample 4 points
        sample_indices = np.random.choice(len(points), 4, replace=False)
        sample = points[sample_indices]

        # Calculate sphere equation
        # (x-a)^2 + (y-b)^2 + (z-c)^2 = r^2

        A = np.array([
            [2 * (sample[1][0] - sample[0][0]),
             2 * (sample[1][1] - sample[0][1]),
             2 * (sample[1][2] - sample[0][2])],

            [2 * (sample[2][0] - sample[0][0]),
             2 * (sample[2][1] - sample[0][1]),
             2 * (sample[2][2] - sample[0][2])],

            [2 * (sample[3][0] - sample[0][0]),
             2 * (sample[3][1] - sample[0][1]),
             2 * (sample[3][2] - sample[0][2])]
        ])

        B = np.array([
            [sample[1][0]**2
             + sample[1][1]**2
             + sample[1][2]**2
             - sample[0][0]**2
             - sample[0][1]**2
             - sample[0][2]**2],

            [sample[2][0]**2
             + sample[2][1]**2
             + sample[2][2]**2
             - sample[0][0]**2
             - sample[0][1]**2
             - sample[0][2]**2],

            [sample[3][0]**2
             + sample[3][1]**2
             + sample[3][2]**2
             - sample[0][0]**2
             - sample[0][1]**2
             - sample[0][2]**2]
        ])

        center = np.linalg.solve(A, B).flatten()

        radius = np.sqrt(
            np.sum((sample[0] - center)**2)
        )

        # Calculate distances of all points to the sphere surface
        distances = np.abs(
            np.sqrt(
                np.sum((points - center)**2, axis=1)
            ) - radius
        )

        # Count inliers
        inliers = np.where(distances < threshold)[0]

        if len(inliers) > len(best_inliers):
            best_inliers = inliers
            best_sphere = (*center, radius)

    return best_sphere, best_inliers

#%% 4. Apply RANSAC Shape Detection

# Find plane using RANSAC
plane_params, plane_inliers = ransac_plane(points)

# Find sphere using RANSAC
sphere_params, sphere_inliers = ransac_sphere(points)

print(f"Plane equation: {plane_params[0]}x + {plane_params[1]}y + {plane_params[2]}z + {plane_params[3]} = 0")

print(f"Sphere equation: (x - {sphere_params[0]})^2 + (y - {sphere_params[1]})^2 + (z - {sphere_params[2]})^2 = {sphere_params[3]}^2")

#%% 5. Visualize results

# Select and segment the planar points
plane_cloud = o3d.geometry.PointCloud()
plane_cloud.points = o3d.utility.Vector3dVector(points[plane_inliers])
plane_cloud.paint_uniform_color([1, 0, 0])  # Red

# Select and Segment the spherical points
sphere_cloud = o3d.geometry.PointCloud()
sphere_cloud.points = o3d.utility.Vector3dVector(points[sphere_inliers])
sphere_cloud.paint_uniform_color([0, 1, 0])  # Green

# Select and Segment the remaining points
other_points = np.delete(
    points,
    np.union1d(plane_inliers, sphere_inliers),
    axis=0
)

other_cloud = o3d.geometry.PointCloud()
other_cloud.points = o3d.utility.Vector3dVector(other_points)
other_cloud.paint_uniform_color([0, 0, 1])  # Blue

# Create coordinate frame
coordinate_frame = o3d.geometry.TriangleMesh.create_coordinate_frame(
    size=1,
    origin=[0, 0, 0]
)

# Visualize
o3d.visualization.draw_geometries([
    plane_cloud,
    sphere_cloud,
    other_cloud,
    coordinate_frame
])