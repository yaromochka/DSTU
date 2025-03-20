import sys
import math


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, a, b):
        rootA, rootB = self.find(a), self.find(b)
        if rootA != rootB:
            if self.rank[rootA] > self.rank[rootB]:
                self.parent[rootB] = rootA
            elif self.rank[rootA] < self.rank[rootB]:
                self.parent[rootA] = rootB
            else:
                self.parent[rootB] = rootA
                self.rank[rootA] += 1
            return True
        return False


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def solve():
    # Читаем количество точек
    N = int(sys.stdin.readline())
    points = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

    # Читаем количество существующих рёбер
    M = int(sys.stdin.readline())
    edges = []
    dsu = DSU(N)

    # Обрабатываем уже имеющиеся рёбра (добавляем их в DSU)
    for _ in range(M):
        u, v = map(int, sys.stdin.readline().split())
        dsu.union(u - 1, v - 1)

    # Добавляем все возможные рёбра с их длиной
    for i in range(N):
        for j in range(i + 1, N):
            edges.append((distance(points[i], points[j]), i, j))

    # Сортируем рёбра по длине (алгоритм Крускала)
    edges.sort()
    total_cost = 0.0

    for w, u, v in edges:
        if dsu.union(u, v):  # Добавляем ребро, если соединяет разные компоненты
            total_cost += w

    print(f"{total_cost:.5f}")


# Запускаем решение
solve()
