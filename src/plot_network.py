import matplotlib.pyplot as plt
import matplotlib as mpl

def scatter_cities(cities, ax):
    ax.scatter(cities['x'], cities['y'], color='red', s=4)

def plot_neurons(neurons, ax):
    ax.plot(neurons[:,0], neurons[:,1], 'r.', ls='-', color='#0063ba', markersize=2)

def save_figure(fig, name):
    plt.savefig(name, bbox_inches='tight', pad_inches=0, dpi=200)
    plt.close()

def plot_network(cities, neurons, name='diagram.png', ax=None):
    """Plot a graphical representation of the problem"""
    mpl.rcParams['agg.path.chunksize'] = 10000

    if not ax:
        fig = plt.figure(figsize=(5, 5), frameon = False)
        axis = fig.add_axes([0,0,1,1])

        axis.set_aspect('equal', adjustable='datalim')
        plt.axis('off')

        scatter_cities(cities, axis)
        plot_neurons(neurons, axis)

        save_figure(fig, name)

    else:
        scatter_cities(cities, ax)
        plot_neurons(neurons, ax)
        return ax

