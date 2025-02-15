def levenshtein_distance(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Инициализация границ
    for i in range(n + 1):
        dp[i][0] = i  # Превратить i символов в пустую строку
    for j in range(m + 1):
        dp[0][j] = j  # Превратить пустую строку в j символов

    # Заполнение таблицы
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # Буквы совпадают — ничего не делаем
            else:
                dp[i][j] = min(
                    dp[i - 1][j] + 1,  # Удаление символа из s1
                    dp[i][j - 1] + 1,  # Вставка символа в s1
                    dp[i - 1][j - 1] + 1  # Замена символа
                )

    return dp[n][m]


# Чтение входных данных
s1 = input().strip()
s2 = input().strip()

# Выводим расстояние Левенштейна
print(levenshtein_distance(s1, s2))
