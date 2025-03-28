from collections import defaultdict


class Graph:
    def __init__(self):
        self.adj_list = defaultdict(list)

    def add_edge(self, u, v, weight):
        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight))  # Для неориентированного графа