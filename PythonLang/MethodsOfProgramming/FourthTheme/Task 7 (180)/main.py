from array import array
from collections import deque
from typing import Final, List

INF: Final[int] = 10**9  # Используем большое число вместо float('inf')


def restore_cycle(path: List[int], start: int) -> List[int]:
    """Восстанавливаем цикл, начиная с найденной вершины."""
    cycle = []
    v = start
    for _ in range(len(path)):  # Гарантируем выход из цикла
        v = path[v]
    start = v

    while True:
        cycle.append(start)
        start = path[start]
        if start == v:
            break
    cycle.append(v)
    cycle.reverse()

    return cycle


def main() -> None:
    n: int = int(input())

    # Храним граф в виде списка списков (экономия памяти)
    graph: List[List[int]] = [list(map(int, input().split())) for _ in range(n)]

    # Алгоритм Беллмана-Форда
    distance = [INF] * n
    path = [-1] * n

    cycle_start = -1

    for start in range(n):
        if distance[start] == INF:
            distance[start] = 0
            for _ in range(n):
                cycle_start = -1
                for u in range(n):
                    for v in range(n):
                        if graph[u][v] < 100000:  # Проверяем, есть ли ребро
                            if distance[u] < INF and distance[v] > distance[u] + graph[u][v]:
                                distance[v] = distance[u] + graph[u][v]
                                path[v] = u
                                cycle_start = v

    if cycle_start == -1:
        print("NO")
    else:
        cycle = restore_cycle(path, cycle_start)
        print("YES")
        print(len(cycle))
        print(" ".join(str(v + 1) for v in cycle))  # Перевод в 1-based индексацию


if __name__ == '__main__':
    main()
