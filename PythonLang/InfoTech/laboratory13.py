import math as mt


def first():
    try:
       T = float(input('Введите температуру по Цельсию: '))
    except ValueError:
        print('Неверное значение')
        exit()
    TF = 32 + 9 / 5 * T
    return TF


def second():
    try:
        x, y, z = map(int, input('Введите значения для переменных: ').split())
    except ValueError:
        print('Неверное значение')
        exit()
    a = y ** (2 * x ** 2 - y) + (3 * mt.acos(1) / ((z ** 2 + x * y) ** 2))
    b = mt.tan((abs(x - y) ** 2) / 3 * z + mt.cos(x ** 2))
    return a, f'{a:.1f}', b, f'{1.124214214:.1f}', round(1.124214214, 1)


def third():
    try:
        A, B, C = map(int, input('Введите три целых числа: ').split())
    except ValueError:
        print('Неверное значение')
        exit()
    print(f'Исходные данные: {A}, {B}, {C}')
    if all([i > 0 for i in [A, B, C]]):
        print(f'Числа {A}, {B} и {C} - положительные')
    else:
        k = 0
        for i in [A, B, C]:
            if i < 0:
                k += 1
        print(f'Есть хотя бы одно отрицательное число')
        print(f'Количество отрицательных {k}')

def fourth():
    try:
        N = int(input('Введите значение N: '))
    except ValueError:
        print('Неверное значение')
    K = 0
    while 2 ** K != N:
        if K >= N ** 0.5:
            print(f'Число {N} не является степенью числа 2')
            break
        K += 1
    else:
        print(f'Число {N} равно числу 2 в степени {K}')


def main():
    try:
        a = int(input('Введите номер задания: '))
    except ValueError:
        print('Неверный номер задания')
        exit()
    if a == 1:
        print(f'Значение по фаренгейту равно {first()}')
    elif a == 2:
        print(f'Значения a и b {second()}')
    elif a == 3:
        third()
    elif a == 4:
        fourth()
    else:
        print('Неверный номер задания')


if __name__ == '__main__':
    main()