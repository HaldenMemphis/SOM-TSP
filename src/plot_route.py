import matplotlib.pyplot as plt

def plot_route(city_df, route, figname='route.png'):
    plt.scatter(city_df['x'], city_df['y'], c='b', label='City',s=2)

    for i in range(len(route) - 1):
        start = route[i]
        end = route[i + 1]
        plt.plot([city_df.loc[start, 'x'], city_df.loc[end, 'x']],
                 [city_df.loc[start, 'y'], city_df.loc[end, 'y']],
                 c='r', linewidth=2)

    plt.legend()
    plt.title('Route Result')
    plt.show()
    plt.close()
