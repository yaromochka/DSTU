from functools import reduce

"""
1. Напишите программу для решения примера (по вариантам).
Предусмотрите проверку деления на ноль. Все необходимые переменные
пользователь вводит через консоль. Запись |пример| означает «взять по
модулю», т.е. если значение получится отрицательным, необходимо
сменить знак с минуса на плюс.
Вариант 4. |a - b*c*d3+(c5-a2)/a + f3*(a-213)|
"""


def first(mas: str) -> bool | str:
    if len(mas.split(', ')) == 5 and all([i.replace('-', '').replace('.', '').isdigit() for i in mas.split(', ')]):
        a, b, c, d, f = map(float, mas.split(', '))
        if a != 0:
            return str(abs(a - (b * c * (d ** 3)) + ((c ** 5) - (a ** 2)) / a + (f ** 3) * (a - 213)))
        else:
            return False
    else:
        return False


"""
2. Дан произвольный список, содержащий и строки и числа
Вариант 4. Выведите все нечетные элементы в одной строке
"""


def second(mas: str) -> bool | str:
    if all([i.replace('-', '').replace('.', '').isdigit() for i in mas.split(', ')]):
        return ', '.join([i for i in mas.split(', ') if int(i) % 2 != 0])
    else:
        return False


"""
3. Дан произвольный список, содержащий только числа.
Вариант 4. Выведите результат умножения всех чисел меньше 10.
"""


def third(mas: str) -> bool | str:
    if all([i.replace('-', '').replace('.', '').isdigit() for i in mas.split(', ')]):
        return reduce(lambda x, y: x * y, [int(i) for i in mas.split(', ') if int(i) < 10], 1)
    else:
        return False


"""
4. Дан произвольный список, содержащий только числа
Вариант 4. Выведите число, находящееся посередине массива
"""


def fourthy(mas: str) -> bool | str:
    if all([i.replace('-', '').replace('.', '').isdigit() for i in mas.split(', ')]):
        return mas.split(', ')[len(mas.split(', ')) // 2]
    else:
        return False


def main(n: int, *, mas: str) -> bool | list[str]:
    if n == '1' and first(mas) is not False: return [f'Сумма элементов равна {first(mas)}']
    if n == '2' and second(mas) is not False: return [f'Список нечётных элементов {second(mas)}']
    if n == '3' and third(mas) is not False: return [f'Произведение всех чисел меньше 10 равно {third(mas)}']
    if n == '4' and fourthy(mas) is not False:
        return [f'Число, находящееся по середине массива - {fourthy(mas)}']
    else:
        return False


if __name__ == '__main__':
    main()
