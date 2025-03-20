from bisect import bisect_left


def generate_sequence(n, a1, k, b, m):
    sequence = [a1]
    for _ in range(n - 1):
        a1 = (k * a1 + b) % m
        sequence.append(a1)
    return sequence


def longest_increasing_subsequence(seq):
    if not seq:
        return []

    dp = []
    pos = []  # Храним индексы в `dp` для восстановления пути
    prev = [-1] * len(seq)

    for i, num in enumerate(seq):
        idx = bisect_left(dp, num)  # Находим место в `dp`
        if idx < len(dp):
            dp[idx] = num  # Заменяем
        else:
            dp.append(num)  # Добавляем

        if idx > 0:
            prev[i] = pos[idx - 1]  # Сохраняем предшественника

        if idx < len(pos):
            pos[idx] = i  # Обновляем индекс в pos
        else:
            pos.append(i)

    # Восстановление LIS
    lis = []
    index = pos[-1]  # Последний элемент LIS
    while index != -1:
        lis.append(seq[index])
        index = prev[index]

    return lis[::-1]


# Входные данные
n, a1, k, b, m = map(int, input().split())

# Генерация последовательности
sequence = generate_sequence(n, a1, k, b, m)

# Поиск LIS
lis = longest_increasing_subsequence(sequence)
print(*lis)
