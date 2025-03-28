import heapq

from PythonLang.MethodsOfProgramming.Lections.Graphs.core.Graph import Graph


def prim(graph, start):
    mst = []
    visited = set()
    priority_queue = [(0, start, None)]

    while priority_queue:
        weight, node, parent = heapq.heappop(priority_queue)

        if node in visited:
            continue

        visited.add(node)
        if parent is not None:
            mst.append((parent, node, weight))

        for neighbor, edge_weight in graph.adj_list[node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (edge_weight, neighbor, node))

    return mst

def main():
    g = Graph()
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 1)
    g.add_edge(1, 2, 2)
    g.add_edge(1, 3, 5)
    g.add_edge(2, 3, 8)
    g.add_edge(3, 4, 3)

    print("\nМинимальное остовное дерево (Прим):")
    prim_result = prim(g, 0)
    for u, v, weight in prim_result:
        print(f"{u} - {v}: {weight}")

if __name__ == "__main__":
    main()