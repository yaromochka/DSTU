import sys
from collections import deque

def bfs(capacity, flow, n):
    """ BFS для поиска пути увеличения потока. """
    parent = [-1] * n
    parent[0] = -2  # Отмечаем источник
    queue = deque([(0, float('inf'))])  # (текущая вершина, минимальная доступная пропускная способность)

    while queue:
        node, min_cap = queue.popleft()

        for neighbor in range(n):
            if parent[neighbor] == -1 and capacity[node][neighbor] > flow[node][neighbor]:
                parent[neighbor] = node
                new_cap = min(min_cap, capacity[node][neighbor] - flow[node][neighbor])
                if neighbor == n - 1:
                    return new_cap, parent
                queue.append((neighbor, new_cap))

    return 0, parent  # Если пути нет

def max_flow(n, m, edges):
    """ Реализация алгоритма Эдмондса-Карпа. """
    capacity = [[0] * n for _ in range(n)]
    flow = [[0] * n for _ in range(n)]

    # Заполняем пропускные способности
    for u, v, cap in edges:
        capacity[u - 1][v - 1] += cap  # Учитываем многократные рёбра

    max_flow = 0

    while True:
        augment, parent = bfs(capacity, flow, n)
        if augment == 0:
            break  # Если пути увеличения нет, завершаем

        # Обновляем потоки
        v = n - 1
        while v != 0:
            u = parent[v]
            flow[u][v] += augment
            flow[v][u] -= augment  # Обратное ребро для отмены потока
            v = u

        max_flow += augment

    return max_flow

def main():
    n, m = map(int, sys.stdin.readline().split())
    edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]
    print(max_flow(n, m, edges))

if __name__ == "__main__":
    main()
