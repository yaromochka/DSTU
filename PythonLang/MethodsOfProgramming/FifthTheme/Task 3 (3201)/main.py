"""
НЕ РАБОТАЕТ
"""


def distribute_students(S, N, seats):
    row_count = [0] * (S + 1)  # Разница M - W в ряду
    col_count = [0] * (S + 1)  # Разница M - W в колонке
    result = [''] * N  # Итоговый список с 'M' и 'W'

    for i, (r, c) in enumerate(seats):
        if (row_count[r] <= 0 and col_count[c] <= 0) or (row_count[r] == col_count[c]):
            result[i] = 'M'
            row_count[r] += 1
            col_count[c] += 1
        else:
            result[i] = 'W'
            row_count[r] -= 1
            col_count[c] -= 1

    print("".join(result))

# Чтение входных данных
S, N = map(int, input().split())
seats = [tuple(map(int, input().split())) for _ in range(N)]

distribute_students(S, N, seats)
