import matplotlib.pyplot as plt

def plot_learning_network(city_df, neuron_coords, figname='network.png'):

    plt.scatter(city_df['x'], city_df['y'], c='b', label='City',s=2)
    plt.scatter(neuron_coords[:, 0], neuron_coords[:, 1], c='r', label='Neuron',s=2)
    plt.legend()
    plt.title('City and Neuron Coordinates')
    plt.show()
    plt.close()

