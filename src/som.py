import random

import numpy
import numpy as np
import math
import pandas as pd
from distance import get_euclidean_distance
from learn import learn


# first we assume that the normalize function will provide a numpy array (nodes)
def find_winner(network, city):
    winner = get_euclidean_distance(network, city).argmin()
    return winner


def create_network(size):
    return np.random.rand(size, 2)


# This Function aims to normalize all the cities' coordinates
def normalize(nodes):
    # Incase the denominator is 0
    ratio = (nodes.x.max() - nodes.x.min()) / (nodes.y.max() - nodes.y.min()), 1
    ratio = np.array(ratio) / max(ratio)
    # Removal of Initial Offset
    normalized = nodes.apply(lambda c: (c - c.min()) / (c.max() - c.min()))
    return normalized.apply(lambda p: ratio * p, axis=1)

# Get the final route after execution
def get_route(cities,network):
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
        if i % 100 :
            print('Iterated {} out of {}'.format(i, iterations), end="\r")
        # select a random city
        random_num = random.randint(0,cities.shape[0])
        select_city=cities.iloc(random_num)[['x', 'y']].values
        # find the winner
        winner = find_winner(network,select_city)
        network= learn(winner,network,learning_rate,(select_city - network))
        # Decay the variables
        learning_rate = learning_rate * decrease_rate
        size = size * decrease_rate

        # Generate a graph every 500 iterations
        if i%500 == 0:
            #TODO: draw the picture
        # Check if any parameter has completely decayed.
        if size < 1 or learning_rate < 0.001:
            print('Complete execution',
                'at {} iterations'.format(i))
            break
        else:
            print('Completed {} iterations.'.format(iterations))
        #TODO draw the picture

        return get_route(cities,network)

