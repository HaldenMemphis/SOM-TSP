import matplotlib.pyplot as plt

def plot_city_neurons(city_df, neuron_coords, figname='network.png'):

    plt.scatter(city_df['x'], city_df['y'], c='b', label='City')
    plt.scatter(neuron_coords[:, 0], neuron_coords[:, 1], c='r', label='Neuron')

    # 添加图例和标题
    plt.legend()
    plt.title('City and Neuron Coordinates')
    plt.savefig(figname, bbox_inches='tight', pad_inches=0)
    plt.close()

