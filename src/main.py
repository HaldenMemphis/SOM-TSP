import datetime
from som import som
from fileread import read_tsp


def main():
    file_path = '/Users/jasondennis/PycharmProjects/SOM-TSP/san8301.tsp'

    iterations = 100 * 1000
    learning_rate = 0.8
    decrease_rate = 0.997

    # Read from file
    cities_list = read_tsp(file_path)
    print(cities_list)
    # SOM
    som_start_time = datetime.datetime.now()
    route = som(cities_list, iterations, learning_rate, decrease_rate)
    som_end_time = datetime.datetime.now()
    # print('SOM Time Usage:' + (som_end_time - som_start_time).seconds)
    # final_route = cities_list.reindex(route)
    print(route)
    # TODO: calculate the final route distance
    # distance = route_distance(final_route)

    # print('Route found of length {}'.format(distance))

if __name__ == '__main__':
    main()
