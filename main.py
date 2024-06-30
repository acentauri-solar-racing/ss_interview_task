# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# Loading the data
current_dir = os.path.dirname(os.path.abspath(__file__))
route = pd.read_csv(os.path.join(current_dir, 'route.csv'))
cars = pd.read_csv(os.path.join(current_dir, 'cars.csv'))

# Implement your solution
# TODO:
