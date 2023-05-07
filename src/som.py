import random
import numpy as np
from normalize import normalize
from distance import get_euclidean_distance
from learn import learn
from plot_network import plot_learning_network
from plot_route import plot_route


# first we assume that the normalize function will provide a numpy array (nodes)
def find_winner(network, city):
    winner = get_euclidean_distance(network, city).argmin()
    return winner


def create_network(size):
    return np.random.rand(size, 2)


# Get the final route after execution
def get_route(cities, network):
    cities['winner'] = cities[['x', 'y']].apply(
        lambda c: find_winner(network, c),
        axis=1, raw=True)
    return cities.sort_values('winner').index


def som(cities_list, iterations, learning_rate, decrease_rate):
    learning_rate_records=[]
    cities = cities_list.copy()
    # normalize all the cities' coordinates to [0,1]
    cities[['x', 'y']] = normalize(cities[['x', 'y']])

    size = cities.shape[0] * 10
    network = create_network(size)
    print('Initialized a {} nodes network.'.format(size))

    # start iterate
    for i in range(iterations):
        if not i % 100:
            print('\tIterated {} out of {}'.format(i, iterations), end="\r")
        # select a random city
        select_city = cities.sample(1)[['x', 'y']].values
        # find the winner
        winner = find_winner(network, select_city)
        network = learn(winner, network, learning_rate, (select_city - network), size)
        # Decay the variables
        learning_rate = learning_rate * decrease_rate
        size = size * 0.9997

        # Generate a graph every 1000 iterations
        if i % 1000 == 0:
            plot_learning_network(cities, network)
        # Check if any parameter has completely decayed.
        if size < 1 or learning_rate < 0.0001:
            print('Complete execution',
                  'at {} iterations'.format(i))
            break
    else:
        print('Completed {} iterations.'.format(iterations))
        plot_learning_network(cities, network, name='diagrams/{:05d}.png'.format(i))

    route = get_route(cities, network)
    plot_route(cities, route, 'diagrams/route.png')
    return route
