def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n  # dp[i] — длина LIS, заканчивающегося в arr[i]
    prev = [-1] * n  # prev[i] — индекс предыдущего элемента в LIS

    # Заполнение dp и prev
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j

    # Найдём индекс конца LIS
    max_index = max(range(n), key=lambda i: dp[i])

    # Восстановление LIS
    lis = []
    while max_index != -1:
        lis.append(arr[max_index])
        max_index = prev[max_index]

    return lis[::-1]  # Переворачиваем, чтобы получить правильный порядок


# Чтение входных данных
n = int(input())
arr = list(map(int, input().split()))

# Вычисление LIS
lis = longest_increasing_subsequence(arr)

# Вывод результата
print(*lis)
