import numpy as np


"""
Пусть дана матрица:
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
2 3 4 5 6 7 8 9
9 8 7 6 5 4 3 2
1 3 5 7 9 7 5 3
3 1 5 3 2 6 5 7
1 7 5 9 7 3 1 5
2 6 3 5 1 7 3 2
"""


"""
Вариант №1. Определите структуру для хранения матрицы.
4. Напишите функцию возведения первых четырех строк в квадрат.
"""


def first() -> list[str]:
    return reversed([f'Первые четыре строки: ', *[''.join(str(matrix[i])) for i in range(4)], f'Строка с элементами, возведёнными в квадрат: ', *[''.join(str(np.power(i, 2))) for i in matrix[0:4, :]]])


"""
Вариант №2. Определите структуру для хранения матрицы
4. Напишите функцию сложения по столбцам четных элементов.
"""

def second() -> list[str]:
    return reversed([f'Вектор сумм по столбцам: ', ' '.join([str(np.sum(i)) for i in matrix.T])])


"""
Вариант №3. Определите структуру для хранения матрицы.
4. Напишите функцию сложения по столбцам четных элементов
"""


def third() -> list[str]:
    return reversed([f'Вектор сумм по строкам: ', ' '.join([str(np.sum(i)) for i in matrix])])


"""
Вариант №4. Определите структуру для хранения матрицы.
4. Напишите функцию замены значений всех элементов матрицы на 0.
"""


def fourthy() -> list[str]:
    return reversed([f'Заменённая матрица на нули: ', *[''.join(str(i)) for i in np.zeros_like(matrix)]])


"""
Вариант №5. Определите структуру для хранения матрицы.
4. Напишите функцию, которая удалит 4 последних строки.
"""


def fifth() -> list[str]:
    return reversed([f'Матрица с четырьмя удалёнными строками: ', *[''.join(str(i)) for i in matrix[-4::]]])


"""
Вариант №6. Определите структуру для хранения матрицы
4. Напишите функцию, которая поменяет первый и последний столбцы матрицы местами. 
"""


def sixth() -> list[str]:
    matrix[:, [0, -1]] = matrix[:, [-1, 0]]
    return reversed(['Матрица с поменянными столбцами: ', *[''.join(str(i)) for i in matrix]])


"""
Вариант №7. Определите структуру для хранения матрицы.
4. Пусть пользователь может ввести число через консоль. Напишите
функцию, которая посчитает, сколько раз в матрице встречается
заданное пользователем число
"""


def seventh(mas: str) -> bool | list[str]:
    mas = mas.split(', ')
    if len(mas) and all([i.isdigit() for i in mas]):
        mas = int(''.join(mas))
        counter = 0
        for i in range(8):
            for j in range(8):
                if matrix[i][j] == mas: counter += 1
        return reversed([f'Количество цифр {mas} в матрице равно {counter}'])
    else:
        return False


"""
Вариант №8. Определите структуру для хранения матрицы.
4. Пусть пользователь через консоль вводит три числа: первое – номер
строки, второе – номер столбца, третье – число (на которое нужно
перезаписать данные в введенной позиции). Напишите функцию,
которая найдет число в данной позиции (пересечение введенных
строки и столбца) и заменит на введенное пользователем.
"""


def eighth(mas: str) -> bool | list[str]:
    mas = mas.split(', ')
    if len(mas) == 3 and all([i.isdigit() for i in mas]):
        a, b, c = map(int, mas)
        if 1 <= a <= 8 and 1 <= b <= 8:
            temp, matrix[a - 1][b - 1] = matrix[a - 1][b - 1], c
            return reversed([f'Изменённое число: {temp}', f'Новая матрица:', *[''.join(str(i)) for i in matrix]])
        else:
            return False
    else:
        return False


def main(n: int, *, mas: str) -> bool | list[str]:
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