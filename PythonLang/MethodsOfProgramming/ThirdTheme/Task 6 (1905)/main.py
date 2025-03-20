def longest_valid_bracket_subsequence(s):
    n = len(s)
    if n == 0:
        return ""

    # DP-таблица: dp[i][j] - максимальная длина правильной подпоследовательности в s[i:j+1]
    dp = [[0] * n for _ in range(n)]
    # Трассировка для восстановления ответа
    trace = [[None] * n for _ in range(n)]

    # Проверка на парность скобок
    def is_pair(l, r):
        return (l == '(' and r == ')') or (l == '[' and r == ']') or (l == '{' and r == '}')

    # Заполняем DP снизу вверх
    for length in range(2, n + 1):  # Длина подстроки
        for i in range(n - length + 1):
            j = i + length - 1  # Правая граница
            # Рассматриваем два случая:
            # 1) Скобки на концах образуют пару
            if is_pair(s[i], s[j]):
                dp[i][j] = dp[i + 1][j - 1] + 2
                trace[i][j] = (i + 1, j - 1)
            # 2) Иначе - берем максимум из возможных разбиений
            for k in range(i, j):
                if dp[i][k] + dp[k + 1][j] > dp[i][j]:
                    dp[i][j] = dp[i][k] + dp[k + 1][j]
                    trace[i][j] = (i, k, k + 1, j)

    # Восстановление ответа
    def restore(i, j):
        if i > j:
            return ""
        if trace[i][j] is None:
            return ""
        if len(trace[i][j]) == 2:  # Пара скобок
            return s[i] + restore(i + 1, j - 1) + s[j]
        else:  # Разделение на две части
            i1, j1, i2, j2 = trace[i][j]
            return restore(i1, j1) + restore(i2, j2)

    return restore(0, n - 1)


# Чтение строки
s = input().strip()
print(longest_valid_bracket_subsequence(s))
