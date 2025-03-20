import sys

"""
НЕ РАБОТАЕТ
"""

def read_input():
    """Считываем входные данные."""
    N = int(sys.stdin.readline().strip())
    distances = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    Q = int(sys.stdin.readline().strip())
    queries = []
    for _ in range(Q):
        line = list(map(int, sys.stdin.readline().split()))
        excluded = set(line[1:])  # точки, которые удалены
        queries.append(excluded)
    return N, distances, Q, queries


def solve_tsp_dp(N, distances, excluded):
    """Решает задачу коммивояжера методом DP по битмаске."""

    # Определяем доступные точки
    nodes = [i for i in range(N) if i not in excluded]
    node_count = len(nodes)

    # Если осталась только одна точка (1), то путь = 0
    if node_count == 1:
        return 0

    # Перенумеровка узлов (1 -> 0, остальные -> свои индексы)
    index_map = {nodes[i]: i for i in range(node_count)}

    # DP-массив: dp[mask][i] - минимальный путь, пройдя mask и закончив в i
    INF = float('inf')
    dp = [[INF] * node_count for _ in range(1 << node_count)]
    dp[1][0] = 0  # Начинаем с точки 1 (бит 0 включен)

    # Перебираем все возможные подмножества (маски)
    for mask in range(1 << node_count):
        for u in range(node_count):
            if (mask & (1 << u)) == 0:  # Точка u не входит в mask
                continue
            for v in range(node_count):
                if (mask & (1 << v)) == 0:  # Если v ещё не была пройдена
                    new_mask = mask | (1 << v)
                    dp[new_mask][v] = min(dp[new_mask][v], dp[mask][u] + distances[nodes[u]][nodes[v]])

    # Минимальный путь, возвращающийся в 1 (индекс 0)
    final_mask = (1 << node_count) - 1  # Все точки посещены
    return min(dp[final_mask][i] + distances[nodes[i]][0] for i in range(1, node_count))


def main():
    # Читаем данные
    N, distances, Q, queries = read_input()

    # Обрабатываем каждый запрос
    results = []
    for excluded in queries:
        result = solve_tsp_dp(N, distances, excluded)
        results.append(str(result))

    # Выводим результат
    sys.stdout.write("\n".join(results) + "\n")


if __name__ == "__main__":
    main()
