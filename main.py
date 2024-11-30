import numpy as np

# Матриця суміжності графа
graph_matrix = [
    [0, 89, 92, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
    [89, 0, 62, 40, 9999, 9999, 9999, 9999, 9999, 9999],
    [92, 62, 0, 70, 44, 9999, 9999, 9999, 9999, 9999],
    [9999, 40, 70, 0, 68, 56, 9999, 9999, 9999, 9999],
    [9999, 9999, 44, 68, 0, 66, 90, 9999, 9999, 9999],
    [9999, 9999, 9999, 56, 66, 0, 86, 57, 9999, 9999],
    [9999, 9999, 9999, 9999, 90, 86, 0, 58, 77, 9999],
    [9999, 9999, 9999, 9999, 9999, 57, 58, 0, 52, 81],
    [9999, 9999, 9999, 9999, 9999, 9999, 77, 52, 0, 78],
    [9999, 9999, 9999, 9999, 9999, 9999, 9999, 81, 78, 0],
]

graph = np.array(graph_matrix)

# Алгоритм Дейкстри
def dijkstra(graph, start, end):
    n = len(graph)
    visited = [False] * n
    distances = [float('inf')] * n
    distances[start] = 0
    previous = [-1] * n

    for _ in range(n):
        min_distance = float('inf')
        min_vertex = -1
        for vertex in range(n):
            if not visited[vertex] and distances[vertex] < min_distance:
                min_distance = distances[vertex]
                min_vertex = vertex

        if min_vertex == -1:
            break

        visited[min_vertex] = True

        for neighbor in range(n):
            edge_weight = graph[min_vertex][neighbor]
            if edge_weight != 9999 and not visited[neighbor]:
                new_distance = distances[min_vertex] + edge_weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = min_vertex

    path = []
    current = end
    while current != -1:
        path.append(current)
        current = previous[current]
    path.reverse()

    return distances[end], path

# Розрахунок
start_point = 0  # A
end_point = 9  # B
min_cost, optimal_path = dijkstra(graph, start_point, end_point)

print("Мінімальна вартість:", min_cost)
print("Оптимальний маршрут:", " → ".join(map(str, optimal_path)))