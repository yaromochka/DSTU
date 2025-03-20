import sys

class DSU:
    """Структура данных для объединения и поиска"""
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, v):
        """Находим корень множества сжатие путей"""
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, v1, v2):
        """Объединяем два множества по рангу"""
        root1 = self.find(v1)
        root2 = self.find(v2)
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1
            return True
        return False

def kruskal(n, edges):
    """Алгоритм Крускала для поиска MST"""
    edges.sort(key=lambda x: x[2])  # Сортируем рёбра по весу
    dsu = DSU(n)
    mst_weight = 0
    edges_used = 0

    for u, v, w in edges:
        if dsu.union(u - 1, v - 1):  # Пробуем соединить компоненты
            mst_weight += w
            edges_used += 1
            if edges_used == n - 1:  # Если нашли n-1 рёбер — выходим
                break

    return mst_weight

# Читаем входные данные
n, m = map(int, sys.stdin.readline().split())
edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]

# Вычисляем MST и выводим результат
print(kruskal(n, edges))
