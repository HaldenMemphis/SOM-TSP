import random
import numpy as np
from normalize import normalize
from distance import get_euclidean_distance
from learn import learn


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
    cities = cities_list.copy()
    # normalize all the cities' coordinates to [0,1]
    cities[['x', 'y']] = normalize(cities[['x', 'y']])

    size = cities.shape[0] * 10
    network = create_network(size)
    print('Initialized a {} nodes network.'.format(size))

    # start iterate
    for i in range(iterations):
        if i % 100:
            print('Iterated {} out of {}'.format(i, iterations), end="\r")
        # select a random city
        random_num = random.randint(0, cities.shape[0])
        select_city = cities.sample(1)[['x', 'y']].values
        # find the winner
        winner = find_winner(network, select_city)
        network = learn(winner, network, learning_rate, (select_city - network), size)
        # Decay the variables
        learning_rate = learning_rate * decrease_rate
        size = size * decrease_rate

        # Generate a graph every 500 iterations
        # if i%500 == 0:
        #     #TODO: draw the picture
        #     return 0
        # Check if any parameter has completely decayed.
        if size < 1 or learning_rate < 0.001:
            print('Complete execution',
                  'at {} iterations'.format(i))
            break
        else:
            print('Completed {} iterations.'.format(iterations))
        # TODO draw the picture

        return get_route(cities, network)
