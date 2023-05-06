import numpy as np


def get_euclidean_distance(group_a, group_b):
    return np.linalg.norm(group_a - group_b, axis=1)


def route_lenth(cities):
    points = cities[['x', 'y']]
    distances = get_euclidean_distance(points, np.roll(points, 1, axis=0))
    return np.sum(distances)