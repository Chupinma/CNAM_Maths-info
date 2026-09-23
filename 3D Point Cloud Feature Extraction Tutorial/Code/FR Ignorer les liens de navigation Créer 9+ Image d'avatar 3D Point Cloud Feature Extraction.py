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
pcd_pv.plot(eye_dome_lighting=True)