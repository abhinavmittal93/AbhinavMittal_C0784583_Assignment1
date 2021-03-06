import routes

# Graph: AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7
graph = {
    'A': {'B': 5, 'D': 5, 'E': 7},
    'B': {'C': 4},
    'C': {'D': 8, 'E': 2},
    'D': {'C': 8, 'E': 6},
    'E': {'B': 3}
}

# ----------------------- GROUP A starts --------------------------------------------
print(routes.calc_distance_btwn_routes(graph, ['A', 'B', 'C']))  # A1
print(routes.calc_distance_btwn_routes(graph, ['A', 'D']))  # A2
print(routes.calc_distance_btwn_routes(graph, ['A', 'D', 'C']))  # A3
print(routes.calc_distance_btwn_routes(graph, ['A', 'E', 'B', 'C', 'D']))  # A4
print(routes.calc_distance_btwn_routes(graph, ['A', 'E', 'D']))  # A5
# ----------------------- GROUP A ends --------------------------------------------


print(routes.calc_stops_btwn_routes(graph, 'C', 'C', 3))

# print(routes.get_diff_routes_from_origin(graph, 'C', [], [], []))
