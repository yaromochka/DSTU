import sys

def manacher(s: str) -> int:
    # Преобразуем строку: вставляем между буквами #
    t = '#' + '#'.join(s) + '#'
    n = len(t)
    p = [0] * n
    c, r = 0, 0  # Центр и правый край текущего палиндрома
    total_palindromes = 0

    for i in range(n):
        mirror = 2 * c - i  # Зеркальная позиция i относительно центра c
        if i < r:
            p[i] = min(r - i, p[mirror])

        # Расширяем палиндром
        while i + p[i] + 1 < n and i - p[i] - 1 >= 0 and t[i + p[i] + 1] == t[i - p[i] - 1]:
            p[i] += 1

        # Обновляем центр и правый край
        if i + p[i] > r:
            c, r = i, i + p[i]

        total_palindromes += (p[i] + 1) // 2  # Добавляем количество палиндромов

    return total_palindromes


# Читаем ввод и вызываем алгоритм
s = sys.stdin.readline().strip()
print(manacher(s))
