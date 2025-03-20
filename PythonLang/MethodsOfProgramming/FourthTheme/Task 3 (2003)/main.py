import heapq
import sys

"""
НЕ РЕШЕНО
"""

input = sys.stdin.read
dx = [-1, 0, 1, 0]  # Смещения по строкам (N, E, S, W)
dy = [0, 1, 0, -1]  # Смещения по столбцам (N, E, S, W)
directions = "NESW"


def dijkstra(n, m, start, end, grid):
    x1, y1 = start
    x2, y2 = end

    # Матрица расстояний (изначально ∞)
    dist = [[float('inf')] * m for _ in range(n)]
    parent = [[None] * m for _ in range(n)]  # Запоминаем, откуда пришли

    # Очередь с приоритетом (по минимальному расстоянию)
    pq = []
    heapq.heappush(pq, (0, x1, y1))  # (стоимость, x, y)
    dist[x1][y1] = 0

    while pq:
        cost, x, y = heapq.heappop(pq)

        # Если достигли конечной точки
        if (x, y) == (x2, y2):
            break

        # Проверяем все 4 направления
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != '#':  # Проверяем границы и проходимость
                new_cost = cost + (1 if grid[nx][ny] == '.' else 2)

                if new_cost < dist[nx][ny]:  # Улучшение пути
                    dist[nx][ny] = new_cost
                    parent[nx][ny] = (x, y, directions[d])  # Запоминаем предка и направление
                    heapq.heappush(pq, (new_cost, nx, ny))

    if dist[x2][y2] == float('inf'):
        return -1, ""  # Нет пути

    # Восстановление пути
    path = []
    cur_x, cur_y = x2, y2
    while (cur_x, cur_y) != (x1, y1):
        prev_x, prev_y, move = parent[cur_x][cur_y]
        path.append(move)
        cur_x, cur_y = prev_x, prev_y

    return dist[x2][y2], ''.join(reversed(path))


# Чтение входных данных
data = input().splitlines()
n, m = map(int, data[0].split())
x1, y1 = map(int, data[1].split())
x2, y2 = map(int, data[2].split())
grid = data[3:]

# Индексы в Python начинаются с 0, приводим их к 0-based
x1, y1 = x1 - 1, y1 - 1
x2, y2 = x2 - 1, y2 - 1

# Решаем задачу
time, path = dijkstra(n, m, (x1, y1), (x2, y2), grid)

# Вывод результата
if time == -1:
    print(-1)
else:
    print(time)
    print(path)
