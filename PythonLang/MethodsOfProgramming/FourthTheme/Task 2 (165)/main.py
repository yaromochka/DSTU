from collections import defaultdict


def is_bipartite(n, graph):
    """Проверяет, можно ли разделить граф на два множества (двудольный граф)"""
    color = [-1] * (n + 1)  # -1: не посещён, 0: первый стол, 1: второй стол

    def dfs(v, c):
        color[v] = c
        for neighbor in graph[v]:
            if color[neighbor] == -1:
                if not dfs(neighbor, 1 - c):
                    return False
            elif color[neighbor] == color[v]:  # Конфликт
                return False
        return True

    for i in range(1, n + 1):  # Граф может быть несвязным
        if color[i] == -1:
            if not dfs(i, 0):
                return False, []

    # Собираем группы
    table1 = [i for i in range(1, n + 1) if color[i] == 0]
    return True, table1


# Читаем входные данные
n, m = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# Проверяем двудольность
possible, table1 = is_bipartite(n, graph)

# Вывод результата
if possible:
    print("YES")
    print(*table1)
else:
    print("NO")
