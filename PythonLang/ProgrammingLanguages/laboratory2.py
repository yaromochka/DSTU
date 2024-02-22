from random import randint, sample
from string import ascii_letters


def first(mas):
    if len(mas.split(' ')) == 1 and all([i.replace('-', '').replace('.', '') in '0123456789' for i in mas]):
        my_number = randint(1, 10000000000000)
        user_number = int(mas)
        if user_number <= my_number: return 'Вы не угадали =('
        else: return 'Поздравляю! Вы ввели число больше загаданного'
    else: return False


def second(mas):
    return [word for word in mas.split(' ') if word != '' and word[0] == 'r']


def third():
    word = sample(ascii_letters + '0123456789', 8)
    if any([i for i in word if i in '0123456890']): return ''.join(word)
    else:
        return 'Не получилось. Пробуем заново'


def fourthy(mas):
    digit_str, letter_str = '', ''
    for i in mas:
        if i.isdigit(): digit_str += i
        else: letter_str += i
    return (f'Строка чисел - {digit_str}', f'Строка букв - {letter_str}')


def main(n, *, mas):
    if n == '1' and first(mas) is not False: return [f'{first(mas)}']
    if n == '2' and second(mas) is not False: return [f'Слова начинающиеся с буквы r: {second(mas)}']
    if n == '3' and third() is not False: return [f'Рандомная строка - {third()}']
    if n == '4' and fourthy(mas) is not False: return fourthy(mas)
    else: return False


if __name__ == '__main__':
    main()