import sys


def prefix_function(s):
    """Вычисляет префикс-функцию для строки s"""
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi


def find_max_k(s):
    """Находит максимальное k"""
    n = len(s)
    pi = prefix_function(s)

    # Наименьший период
    period = n - pi[n - 1]

    # Если строка делится на period без остатка
    if n % period == 0:
        return n // period
    return 1


if __name__ == "__main__":
    s = sys.stdin.read().strip()
    print(find_max_k(s))
