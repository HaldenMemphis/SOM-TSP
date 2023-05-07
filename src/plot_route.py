import matplotlib.pyplot as plt

def plot_route(city_df, route, figname='route.png'):
    plt.scatter(city_df['x'], city_df['y'], c='b', label='City',s=1)
    # for i in range(len(route) - 1):
    #     start = route[i]
    #     end = route[i + 1]
    #     plt.plot([city_df.loc[start, 'x'], city_df.loc[end, 'x']],
    #              [city_df.loc[start, 'y'], city_df.loc[end, 'y']],
    #              c='r', linewidth=0.5)
    route = city_df.reindex(route)
    route.loc[route.shape[0]] = route.iloc[0]
    plt.plot(route['x'], route['y'], c='r', label='Route', linewidth=0.5)

    plt.legend()
    plt.title('Route Result')
    plt.savefig(figname, bbox_inches='tight', pad_inches=0)
    plt.show()
    plt.close()
