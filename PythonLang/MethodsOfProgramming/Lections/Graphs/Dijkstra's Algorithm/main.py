import heapq

from PythonLang.MethodsOfProgramming.Lections.Graphs.core.Graph import Graph


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph.adj_list}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph.adj_list[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


def main() -> None:
    g = Graph()
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 1)
    g.add_edge(1, 2, 2)
    g.add_edge(1, 3, 5)
    g.add_edge(2, 3, 8)
    g.add_edge(3, 4, 3)

    print("Кратчайшие пути от вершины 0 (Дейкстра):")
    dijkstra_result = dijkstra(g, 0)
    for node, dist in dijkstra_result.items():
        print(f"0 -> {node}: {dist}")

if __name__ == "__main__":
    main()