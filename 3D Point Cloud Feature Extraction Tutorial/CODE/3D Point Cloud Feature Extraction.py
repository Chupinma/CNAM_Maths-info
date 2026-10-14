#%% Gathering Data

#%% 1. Python Environnement and Library setup

#Base Libraries
import numpy as np
import time

# [Optional] Project Module
from scipy.spatial import KDTree

# 3D Library
#import open3d as o3d
import pyvista as pv

#%% 2. Load Point Cloud Data (PyVista)

pcd_pv = pv.read(r"...\3D Point Cloud Feature Extraction Tutorial\DATA\MLS_UTWENTE_super_sample.ply")

#Plot quickly with EDL on
#pcd_pv.plot(eye_dome_lighting=True)

#%% 2.2. Exploring pyvista capabilities

# Storing in variable for pyvista
pcd_pv["elevation"] = pcd_pv.points[:, 2]
pcd_pv["random"] = pcd_pv.points[:, 0] *pcd_pv.points[:,1]

# Render as spheres
#pv.plot(pcd_pv, scalars=pcd_pv["random"],render_points_as_spheres=True, show_scalar_bar=False)

#%% 3. Pre-processing : Creating a 3D data structure
#%% 3.1 KD-Tree with pyvista

#one point at a tine not efficient
temp = pcd_pv.find_closest_point((1,1,0), n=20)
#print (temp)

#%% 3.2 KD-Tree with scipy

tree = KDTree(pcd_pv.points)

#%% 3.3 K-nearest Neighbors Search and indexing

t0 = time.time()

# Find nearest neighbors for each point in the point cloud
dists, indices = tree.query(pcd_pv.points, k=20)

# Get the neighbor points for each point
neighbor_points = pcd_pv.points[indices]

t1 = time.time()
print(f"Time taken for KNN search: {t1 - t0} seconds")