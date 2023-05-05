from sys import argv
from som import som

def main():
    if len(argv) != 2:
        print("Correct use: python src/main.py <filename>.tsp")
        return -1

    iterations= 100*1000
    learning_rate= 0
    decrease_rate= 0
    #TODO: Read from file and normalize it

    def som(cities_list, iterations, learning_rate, decrease_rate):

    route = som(cities_list, iterations,learning_rate,decrease_rate)

    final_route = problem.reindex(route)

    # TODO: calculate the final route distance
    distance = route_distance(final_route)

    print('Route found of length {}'.format(distance))