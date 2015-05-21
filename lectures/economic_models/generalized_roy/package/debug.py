# Time access and conversions
import time

# Unix Pattern Extensions
import glob

# System-specific parameters and functions
import sys

# Operating System Interfaces
import os
import numpy as np

# Plotting
import matplotlib.pyplot as plt

# Notebook Displays
from IPython.display import display, HTML, Image

# Importing the grmpy package by editing the PYTHONPATH
sys.path.insert(0, 'grmpy')

# Package
import grmpy as gp

# Hidden function
from tests._auxiliary import random_init




np.random.seed(123)
# Generate random request
init_dict = random_init()
gp.simulate(init_dict)

# Estimate model
rslt = gp.estimate(init_dict)

# Check for convergence, which is very different from our
# notion of a SUCCESSFUL estimation run.
assert (rslt['success'] is True)


print rslt['fval']
assert np.abs(rslt['fval']- 0.734631068458) < 0.00001