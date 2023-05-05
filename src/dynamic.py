import numpy as np
from scipy.spatial.distance import pdist, squareform


def dataframe_to_distance_matrix(coordinates):
    # Convert DataFrame to NumPy array
    coordinates = coordinates.to_numpy()

    # Calculate distance matrix
    distances = pdist(coordinates, metric='euclidean')
    distance_matrix = squareform(distances)

    return distance_matrix


def tsp_dp(distance_matrix):
    n = len(distance_matrix)
    dp = np.zeros((1 << n, n))
    for i in range(1, 1 << n):
        for j in range(n):
            if i == 1 << j:
                dp[i][j] = distance_matrix[0][j]
            elif i & (1 << j) != 0:
                dp[i][j] = float('inf')
                S = [k for k in range(n) if k != j and (i & (1 << k)) != 0]
                for k in S:
                    dp[i][j] = min(dp[i][j], dp[i ^ (1 << j)][k] + distance_matrix[k][j])
    return dp[(1 << n) - 1][0]
