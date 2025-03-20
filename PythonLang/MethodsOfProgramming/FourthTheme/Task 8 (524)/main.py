import heapq
import sys

INF = 10 ** 9  # Достаточно большое число для инициализации времени


def find_earliest_arrival(n, a, b, flights):
    graph = [[] for _ in range(n + 1)]  # Список смежности

    for u, t1, v, t2 in flights:
        graph[u].append((t1, v, t2))  # (время отправления, пункт назначения, время прибытия)

    # Инициализируем массив минимального времени
    min_time = {i: INF for i in range(1, n + 1)}
    min_time[a] = 0  # Начальная точка

    # Очередь для Дейкстры (минимальная куча)
    pq = [(0, a)]  # (время прибытия, пункт)

    while pq:
        cur_time, u = heapq.heappop(pq)

        if cur_time > min_time[u]:
            continue  # Пропускаем неактуальные значения

        for t1, v, t2 in graph[u]:
            if t1 >= cur_time and t2 < min_time[v]:  # Учитываем время отправления
                min_time[v] = t2
                heapq.heappush(pq, (t2, v))

    return min_time[b]  # Минимальное время прибытия в B


# Считывание входных данных
def main():
    n = int(input().strip())
    a, b = map(int, input().split())
    k = int(input().strip())

    flights = [tuple(map(int, input().split())) for _ in range(k)]

    print(find_earliest_arrival(n, a, b, flights))


if __name__ == "__main__":
    main()
