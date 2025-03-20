def knapsack(N, M, weights, costs):
    dp = [0] * (M + 1)  # dp[j] — максимальная стоимость для веса j
    prev = [-1] * (M + 1)  # Запоминаем предмет, который использовался для j

    # Заполняем dp
    for i in range(N):
        w, c = weights[i], costs[i]
        for j in range(M, w - 1, -1):  # Обратный проход
            if dp[j - w] + c > dp[j]:
                dp[j] = dp[j - w] + c
                prev[j] = i  # Запоминаем предмет i

    # Восстанавливаем список предметов
    j = M
    items = set()  # Используем множество, чтобы избежать дубликатов
    while j > 0 and prev[j] != -1:
        i = prev[j]
        if i + 1 not in items:  # Проверяем, добавлен ли предмет
            items.add(i + 1)  # Записываем индекс предмета (1-based)
        j -= weights[i]

    return sorted(items)  # Выводим в порядке возрастания

# Чтение входных данных
N, M = map(int, input().split())
weights = list(map(int, input().split()))
costs = list(map(int, input().split()))

# Получаем ответ
result = knapsack(N, M, weights, costs)

# Вывод результата
print(*result, sep='\n')
