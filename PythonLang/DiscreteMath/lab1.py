from decimal import Decimal


def digit(n):
    n = n.replace('.', '').replace('-', '')
    return all([i.isdigit() for i in n])


def nok(a, b): return (a * b // nod(a, b))


def nod(a, b):
    while a != 0 and b != 0:
        if a > b: a = a % b
        else: b = b % a
    return a + b


def main():
    a = input('Что вы хотите найти (НОК или НОД): ').lower()
    if a == 'нок' or a == 'нод':
        nums = input('Введите два числа через пробел: ').split()
        if all([digit(i) for i in nums]) and len(nums) == 2:
            x, y = map(Decimal, nums)
            if x != 0 and y != 0:
                x, y = abs(int(x)), abs(int(y))
                if a == 'нок': return print(f'Наименьшее общее кратное равно {nok(x, y)}')
                if a == 'нод': return print(f'Наибольший общий делитель равен {nod(x, y)}')
                else: return print('Вот это мы найти не можем')
            else: return print('Нельзя вводить 0')
        else: return print('Введены неверные данные')
    else: return print('Введены неверные данные')


if __name__ == '__main__':
    main()