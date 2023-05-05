import numpy as np


def get_euclidean_distance(group_a, group_b):
    return np.linalg.norm(group_a - group_b, axis=1)
