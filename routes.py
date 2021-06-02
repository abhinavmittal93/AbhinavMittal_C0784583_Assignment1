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


def calc_stops_btwn_routes(graph, origin, destination, max_stops, routes_visited=[]):
    if origin in graph and destination in graph:
        routes = 0
        stops = 0

        if stops == max_stops:
            return 0

        for route in graph[origin]:
            if not routes_visited[route]:
                if route == destination:
                    stops += 1
                    routes += 1
                    routes_visited.append(route)

                if route not in routes_visited and route != destination:
                    routes_visited.append(route)
                    routes += calc_stops_btwn_routes(graph, route, destination, max_stops - stops)

        return routes

    else:
        return 'NO SUCH ROUTE'


def get_diff_routes_from_origin(graph, origin, routes=[], single_route=[], visited = []):
    if origin in graph:

        if len(single_route) > 2 and single_route[-1] == single_route[0]:
            temp = single_route[0]
            single_route = [temp]

        single_route.append(origin)
        #visited.append(origin)
        for route in graph[origin]:
            #if len(visited) == 0 or route not in visited:
                #visited.append(route)
            if len(single_route) > 1 and single_route[0] == origin:
                routes.append(single_route)
                break

            get_diff_routes_from_origin(graph, route, routes, single_route)


    return routes
