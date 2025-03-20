import sys
import math
from functools import lru_cache

def read_input():
    n = int(sys.stdin.readline().strip())
    points = [tuple(map(float, sys.stdin.readline().split())) for _ in range(n)]
    return n, points

def distance(p1, p2):
    return math.dist(p1, p2)

def tsp(n, points):
    dist_matrix = [[distance(points[i], points[j]) for j in range(n)] for i in range(n)]

    @lru_cache(None)
    def dp(mask, i):
        """Возвращает минимальную длину пути, заканчивающегося в `i`, с посещёнными вершинами `mask`."""
        if mask == (1 << i):  # Если в пути только стартовая вершина
            return dist_matrix[0][i]
        prev_mask = mask & ~(1 << i)
        return min(dp(prev_mask, j) + dist_matrix[j][i] for j in range(n) if prev_mask & (1 << j))

    # Ищем минимальный цикл с возвратом в 0
    last_mask = (1 << n) - 1
    last_vertex = min(range(1, n), key=lambda i: dp(last_mask, i) + dist_matrix[i][0])
    min_cost = dp(last_mask, last_vertex) + dist_matrix[last_vertex][0]

    # Восстановление пути
    path = [0]
    mask = last_mask
    curr = last_vertex
    while curr != 0:
        path.append(curr)
        for prev in range(n):
            if mask & (1 << prev) and dp(mask, curr) == dp(mask ^ (1 << curr), prev) + dist_matrix[prev][curr]:
                mask ^= (1 << curr)
                curr = prev
                break

    path.reverse()  # Переворачиваем в нужный порядок
    print(f"{min_cost:.14e}")
    print(" ".join(str(x + 1) for x in path[1:]))

if __name__ == "__main__":
    n, points = read_input()
    tsp(n, points)
