import matplotlib.pyplot as plt
import numpy as np


def plot_dp(Best_path):
    plt.figure(figsize=(5, 5), frameon=False)
    plt.scatter(Best_path[:, 0], Best_path[:, 1],s=1,c='r')
    Best_path = np.vstack([Best_path, Best_path[0]])
    plt.plot(Best_path[:, 0], Best_path[:, 1])
    plt.title('DP Route Result')
    plt.show()
