# This will calculate the distance between the routes
def calc_distance_btwn_routes(graph={}, route=[]):
    distance = 0
    for i in range(len(route)):
        origin_city = route[i]
        if i + 1 < len(route):
            next_city = route[i + 1]
            if next_city in graph[origin_city]:
                distance += graph[origin_city][next_city]
            else:
                return f'NO SUCH ROUTE - {route}'
    return f'The distance between route: {route} is {distance}'
