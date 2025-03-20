import sys
import itertools
import math

def euclidean_distance(p1, p2):
    """ Вычисляет Евклидово расстояние между двумя точками """
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def tsp_held_karp(n, points):
    """ Решает задачу коммивояжёра динамическим программированием по подмножествам """
    # Вычисляем матрицу расстояний
    dist = [[euclidean_distance(points[i], points[j]) for j in range(n)] for i in range(n)]

    # dp[mask][i] - минимальная длина пути для подмножества mask, оканчивающегося в i
    dp = [[float('inf')] * n for _ in range(1 << n)]
    dp[1][0] = 0  # Стартуем из первой вершины

    # Проходим по всем подмножествам вершин
    for mask in range(1, 1 << n):
        for i in range(n):
            if not (mask & (1 << i)):  # Вершина i не в подмножестве
                continue
            prev_mask = mask & ~(1 << i)  # Убираем вершину i из подмножества
            if prev_mask == 0:
                continue
            for j in range(n):
                if prev_mask & (1 << j):  # Если вершина j была в маршруте
                    dp[mask][i] = min(dp[mask][i], dp[prev_mask][j] + dist[j][i])

    # Восстанавливаем минимальный цикл
    last_mask = (1 << n) - 1  # Все вершины посещены
    min_cost = float('inf')
    last_node = -1

    for j in range(1, n):  # Последний переход в вершину 0
        cost = dp[last_mask][j] + dist[j][0]
        if cost < min_cost:
            min_cost = cost
            last_node = j

    # Восстанавливаем порядок посещения
    path = []
    mask = last_mask
    node = last_node

    for _ in range(n - 1):
        path.append(node + 1)
        prev_mask = mask & ~(1 << node)
        for j in range(n):
            if dp[mask][node] == dp[prev_mask][j] + dist[j][node]:
                node = j
                mask = prev_mask
                break

    path.reverse()  # Порядок восстановления был в обратном направлении

    # Выводим ответ
    print(f"{min_cost:.6f}")
    print(" ".join(map(str, path)))

# Читаем входные данные
n = int(sys.stdin.readline().strip())
points = [tuple(map(float, sys.stdin.readline().split())) for _ in range(n)]

# Запускаем решение
tsp_held_karp(n, points)
