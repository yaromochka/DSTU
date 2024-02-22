import numpy as np


def first():
    return reversed([f'Первые четыре строки: ', *[''.join(str(matrix[i])) for i in range(4)], f'Строка с элементами, возведёнными в квадрат: ', *[''.join(str(np.power(i, 2))) for i in matrix[0:4, :]]])


def second():
    return reversed([f'Вектор сумм по столбцам: ', ' '.join([str(np.sum(i)) for i in matrix.T])])


def third():
    return reversed([f'Вектор сумм по строкам: ', ' '.join([str(np.sum(i)) for i in matrix])])


def fourthy():
    return reversed([f'Заменённая матрица на нули: ', *[''.join(str(i)) for i in np.zeros_like(matrix)]])


def fifth():
    return reversed([f'Матрица с четырьмя удалёнными строками: ', *[''.join(str(i)) for i in matrix[-4::]]])


def sixth():
    matrix[:, [0, -1]]= matrix[:, [-1, 0]]
    return reversed(['Матрица с поменянными столбцами: ', *[''.join(str(i)) for i in matrix]])


def seventh(mas):
    mas = mas.split(', ')
    if len(mas) and all([i.isdigit() for i in mas]):
        mas = int(''.join(mas))
        counter = 0
        for i in range(8):
            for j in range(8):
                if matrix[i][j] == mas: counter += 1
        return reversed([f'Количество цифр {mas} в матрице равно {counter}'])
    else: return False


def eighth(mas):
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
    matrix = np.array([
        [1, 2, 3, 4, 5, 6, 7, 8],
        [8, 7, 6, 5, 4, 3, 2, 1],
        [2, 3, 4, 5, 6, 7, 8, 9],
        [9, 8, 7, 6, 5, 4, 3, 2],
        [1, 3, 5, 7, 9, 7, 5, 3],
        [3, 1, 5, 3, 2, 6, 5, 7],
        [1, 7, 5, 9, 7, 3, 1, 5],
        [2, 6, 3, 5, 1, 7, 3, 2]
    ])
    if n == '1': return first()
    if n == '2': return second()
    if n == '3': return third()
    if n == '4': return fourthy()
    if n == '5': return fifth()
    if n == '6': return sixth()
    if n == '7': return seventh(mas)
    if n == '8': return eighth(mas)
    else: return False


if __name__ == '__main__':
    main()