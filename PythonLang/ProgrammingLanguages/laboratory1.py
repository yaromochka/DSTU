from functools import reduce


def first(mas):
    if len(mas.split(', ')) == 5 and all([i.replace('-', '').replace('.', '').isdigit() for i in mas.split(', ')]):
        a, b, c, d, f = map(float, mas.split(', '))
        if a != 0: return str(abs(a - (b * c * (d ** 3)) + ((c ** 5) - (a ** 2)) / a + (f ** 3) * (a - 213)))
        else: return False
    else:
        return False


def second(mas):
    if all([i.replace('-', '').replace('.', '').isdigit() for i in mas.split(', ')]):
        return ', '.join([i for i in mas.split(', ') if int(i) % 2 != 0])
    else: return False


def third(mas):
    if all([i.replace('-', '').replace('.', '').isdigit() for i in mas.split(', ')]):
        return reduce(lambda x, y: x * y, [int(i) for i in mas.split(', ') if int(i) < 10], 1)
    else: return False


def fourthy(mas):
    if all([i.replace('-', '').replace('.', '').isdigit() for i in mas.split(', ')]): return mas.split(', ')[len(mas.split(', ')) // 2]
    else: return False


def main(n, *, mas):
    if n == '1' and first(mas) is not False: return [f'Сумма элементов равна {first(mas)}']
    if n == '2' and second(mas) is not False: return [f'Список нечётных элементов {second(mas)}']
    if n == '3' and third(mas) is not False: return [f'Произведение всех чисел меньше 10 равно {third(mas)}']
    if n == '4' and fourthy(mas) is not False: return [f'Число, находящееся по середине массива - {fourthy(mas)}']
    else: return False


if __name__ == '__main__':
    main()

