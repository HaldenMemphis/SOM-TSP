import datetime
from som import som
from fileread import read_tsp
from dynamic import DP
from distance import route_lenth
import numpy as np
from plot_route import plot_route


def main():
    file_path = '/Users/jasondennis/PycharmProjects/SOM-TSP/san7999.csv'

    iterations = 100 * 1000
    learning_rate = 0.8
    decrease_rate = 0.99997

    # Read from file
    cities_list = read_tsp(file_path)
    print(cities_list)
    # SOM
    print('Start SOM')
    som_start_time = datetime.datetime.now()
    route = som(cities_list, iterations, learning_rate, decrease_rate)
    som_end_time = datetime.datetime.now()
    print('Time Usage of SOM {}'.format((som_end_time - som_start_time).microseconds))
    plot_route(cities_list,route)
    print(route)
    print('Route found of length(SOM) {}'.format(route_lenth(route)))
    # Dynamic
    print('Start Dynamic')
    data = np.array(cities_list)
    data = data[:, 1:]
    model = DP(num_city=data.shape[0], num_total=25, iteration=500, data=data.copy())
    dynamic_start_time=datetime.datetime.now()
    Best_path, Best = model.run()
    dynamic_end_time =datetime.datetime.now()
    print('Time Usage of Dynamic {}'.format((dynamic_end_time - dynamic_start_time).microseconds))
    print('Route found of length(Dynamic):{}'.format(Best))


if __name__ == '__main__':
    main()
