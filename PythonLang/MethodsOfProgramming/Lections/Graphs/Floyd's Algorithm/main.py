from PythonLang.MethodsOfProgramming.Lections.Graphs.core.Graph import Graph


def floyd_warshall(graph):
    nodes = list(graph.adj_list.keys())
    dist = {i: {j: float('inf') for j in nodes} for i in nodes}

    for node in nodes:
        dist[node][node] = 0

    for u in graph.adj_list:
        for v, weight in graph.adj_list[u]:
            dist[u][v] = weight

    for k in nodes:
        for i in nodes:
            for j in nodes:
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

def main():
    g = Graph()
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 1)
    g.add_edge(1, 2, 2)
    g.add_edge(1, 3, 5)
    g.add_edge(2, 3, 8)
    g.add_edge(3, 4, 3)

    print("\nМатрица кратчайших путей (Флойд-Уоршелл):")
    floyd_result = floyd_warshall(g)
    for u in floyd_result:
        print(f"{u}: {floyd_result[u]}")

if __name__ == "__main__":
    main()