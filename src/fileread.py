import pandas as pd
import numpy as np

def read_tsp(filename):
    with open(filename) as f:
        f.seek(0)
        cities = read_cities_data(f)
        return cities

def read_cities_data(file):
    cities = pd.read_csv(
        file,
        sep=' ',
        names=['city', 'y', 'x'],
        dtype={'city': str, 'x': np.float64, 'y': np.float64},
        header=None,
    )
    return cities
