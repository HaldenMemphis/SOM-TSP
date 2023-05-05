import matplotlib.pyplot as plt
import matplotlib as mpl

def scatter_cities(cities, ax):
    ax.scatter(cities['x'], cities['y'], color='red', s=4)

def plot_route_lines(route, ax):
    route.loc[route.shape[0]] = route.iloc[0]
    ax.plot(route['x'], route['y'], color='purple', linewidth=1)

def save_figure(fig, name):
    plt.savefig(name, bbox_inches='tight', pad_inches=0, dpi=200)
    plt.close()

def plot_route(cities, route, name='diagram.png', ax=None):
    """Plot a graphical representation of the route obtained"""
    mpl.rcParams['agg.path.chunksize'] = 10000

    if not ax:
        fig = plt.figure(figsize=(5, 5), frameon = False)
        axis = fig.add_axes([0,0,1,1])

        axis.set_aspect('equal', adjustable='datalim')
        plt.axis('off')

        scatter_cities(cities, axis)
        plot_route_lines(cities.reindex(route), axis)

        save_figure(fig, name)

    else:
        scatter_cities(cities, ax)
        plot_route_lines(cities.reindex(route), ax)
        return ax

