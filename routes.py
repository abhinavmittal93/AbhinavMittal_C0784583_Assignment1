# This will calculate the distance between the routes
def calc_distance_btwn_routes(graph, route):
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


def calc_stops_btwn_routes(graph, origin, destination, max_stops):
    response = 0
    if origin in graph and destination in graph:

        routes = get_diff_routes_from_origin(graph, origin, [], [], [])

        for route in routes:
            if len(route) - 1 <= max_stops:
                response += 1

        return response

    else:
        return 'NO SUCH ROUTE'


def get_diff_routes_from_origin(graph, origin, routes=[], single_route=[], visited=[]):

    if origin in graph:

        if len(single_route) > 2 and single_route[-1] == single_route[0]:
            temp = single_route[0]
            single_route = [temp]

        single_route.append(origin)

        if len(single_route) > 1 and single_route[0] == origin and single_route not in routes:
            routes.append(single_route)

        if len(visited) == 0 or origin not in visited or (len(visited) > 0 and visited[0] == origin):
            visited.append(origin)
            for route in graph[origin]:
                get_diff_routes_from_origin(graph, route, routes, single_route)

    return routes
