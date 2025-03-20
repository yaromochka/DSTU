import sys
import math


def build_sparse_table(arr):
    """Строим Sparse Table за O(N log N)"""
    n = len(arr)
    log_n = math.ceil(math.log2(n)) + 1
    st = [[0] * log_n for _ in range(n)]

    # Заполняем таблицу начальными значениями (0-й уровень)
    for i in range(n):
        st[i][0] = (arr[i], i)  # Храним значение и индекс

    # Заполняем таблицу для всех степеней двойки
    j = 1
    while (1 << j) <= n:
        i = 0
        while i + (1 << j) - 1 < n:
            left = st[i][j - 1]
            right = st[i + (1 << (j - 1))][j - 1]
            st[i][j] = max(left, right)  # Максимум между двумя интервалами
            i += 1
        j += 1

    return st


def query_sparse_table(st, l, r):
    """Отвечаем на запрос за O(1)"""
    length = r - l + 1
    j = int(math.log2(length))
    left = st[l][j]
    right = st[r - (1 << j) + 1][j]
    return max(left, right)[1] + 1  # Возвращаем 1-индексированный номер


def main():
    # Читаем входные данные
    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().split()))
    k = int(sys.stdin.readline().strip())

    # Создаём Sparse Table
    sparse_table = build_sparse_table(arr)

    # Обрабатываем запросы
    result = []
    for _ in range(k):
        l, r = map(int, sys.stdin.readline().split())
        result.append(str(query_sparse_table(sparse_table, l - 1, r - 1)))

    print(" ".join(result))


if __name__ == "__main__":
    main()
