import pandas as pd
import numpy as np

def read_tsp(filename):
    with open(filename) as f:
        node_coord_start, dimension = get_tsp_info(f)
        print('Problem with {} cities read.'.format(dimension))
        f.seek(0)
        cities = read_cities_data(f, node_coord_start, dimension)
        # cities.set_index('city', inplace=True)
        return cities

def get_tsp_info(file):
    node_coord_start = None
    dimension = None
    lines = file.readlines()
    i = 0
    while not dimension or not node_coord_start:
        line = lines[i]
        if line.startswith('NODE_COORD_SECTION'):
            node_coord_start = i
        i += 1
    return node_coord_start, dimension

def read_cities_data(file, node_coord_start, dimension):
    cities = pd.read_csv(
        file,
        skiprows=node_coord_start + 1,
        sep=' ',
        names=['city', 'y', 'x'],
        dtype={'city': str, 'x': np.float64, 'y': np.float64},
        header=None,
        nrows=dimension
    )
    return cities
