def first(mas):
    mas = mas.split(', ')
    if len(mas) == 2 and all(i.isdigit() for i in mas):
        n, k = map(int, mas)
        if 1 <= n <= 8 and 1 <= k <= 8: return reversed([f'Число на позиции ({n}, {k}): ', str(matrix[n - 1][k - 1])])
        else: return False
    else: return False


def second(mas):
    mas = mas.split(', ')
    if len(mas) == 1 and all(i.isdigit() for i in mas):
        mas = int(''.join(mas)) - 1
        if 0 <= mas <= 8: return reversed([f'Изначальная строка: {matrix[mas]}', f'Строка квадратов: {[i ** 2 for i in matrix[mas]]}'])
        else: return False
    else: return False


def third(mas):
    mas, ans = mas.split(', '), []
    if len(mas) == 1 and all(i.isdigit() for i in mas):
        mas = int(''.join(mas)) - 1
        if 0 <= mas <= 8:
            for i in range(8):
                for j in range(8):
                    if j == mas:
                        ans.append(matrix[i][j])
            return reversed([f'Изначальный столбец: {ans}', f'Сумма всех элементов столбца: {sum(ans)}'])
        else: return False
    else: return False


def fourthy(mas):
    mas = mas.split(', ')
    if len(mas) == 3 and all([i.isdigit() for i in mas]):
        a, b, c = map(int, mas)
        if 1 <= a <= 8 and 1 <= b <= 8:
            temp, matrix[a - 1][b - 1] = matrix[a - 1][b - 1], c
            return reversed([f'Изменённое число: {temp}', f'Новая матрица:', *[''.join(str(i)) for i in matrix]])
        else: return False
    else: return False


def main(n, *, mas):
    global matrix
    matrix = [
        [1, 2, 3, 4, 5, 6, 7, 8],
        [8, 7, 6, 5, 4, 3, 2, 1],
        [2, 3, 4, 5, 6, 7, 8, 9],
        [9, 8, 7, 6, 5, 4, 3, 2],
        [1, 3, 5, 7, 9, 7, 5, 3],
        [3, 1, 5, 3, 2, 6, 5, 7],
        [1, 7, 5, 9, 7, 3, 1, 5],
        [2, 6, 3, 5, 1, 7, 3, 2]
    ]
    if n == '1' and first(mas) is not False: return first(mas)
    if n == '2' and second(mas) is not False: return second(mas)
    if n == '3' and third(mas) is not False: return third(mas)
    if n == '4' and fourthy(mas) is not False: return fourthy(mas)
    else: return False


if __name__ == '__main__':
    main()