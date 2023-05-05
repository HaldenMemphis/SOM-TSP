import numpy as np


'''This function will create a normal distribution to confirm *Winner Takes More* '''
def get_normal_distribution(center, radix, domain):
    # Calculate the distance between the chosen node and the other nodes
    distances = np.absolute(center - np.arange(domain))
    # Sort them in descending order
    distances = np.minimum(distances, distances - domain)
    # Calculate the normal distribution
    normal_distribution = np.exp(-(distances * distances) / (2 * (radix * radix)))
    return normal_distribution


def learn(winner, network, learning_rate, distance, size):
    radix = size//10
    # Get Normal Distribution to make the winner learns more
    normal_distribution = get_normal_distribution(winner, radix, network.shape[0])
    # reshape the array
    reshaped_normal_distribution = normal_distribution[:,np.newaxis]
    # learn
    network += reshaped_normal_distribution * learning_rate * distance
    return network
