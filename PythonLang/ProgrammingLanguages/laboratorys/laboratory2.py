from random import randint, sample
from string import ascii_letters

"""
1. Пусть задано некоторое число my_number. Пользователь вводит с
клавиатуры свое число user_number.
Вариант 4. Запрашивайте у пользователя вводить число user_number до
тех пор, пока оно не будет больше my_number.
"""


def first(mas: str) -> bool | str:
    if len(mas.split(' ')) == 1 and all([i.replace('-', '').replace('.', '') in '0123456789' for i in mas]):
        my_number = randint(1, 10000000000000)
        user_number = int(mas)
        if user_number <= my_number:
            return 'Вы не угадали =('
        else:
            return 'Поздравляю! Вы ввели число больше загаданного'
    else:
        return False


"""
2. Пусть задан список, содержащий строки.
Вариант 4. Выведите все строки, начинающиеся с буквы r.
"""


def second(mas: str) -> bool | list[str]:
    return [word for word in mas.split(' ') if word != '' and word[0] == 'r']


"""
3. Сгенерируйте и выведите:
Вариант 4. Случайную строку, состоящую из 8 символов и
содержащую цифры и буквы. Строка должна содержать
хотя бы одну цифру. 
"""


def third() -> str:
    word = sample(ascii_letters + '0123456789', 8)
    if any([i for i in word if i in '0123456890']):
        return ''.join(word)
    else:
        return 'Не получилось. Пробуем заново'


"""
4. Пусть дана строка:
Вариант 4. На основе данной строки сформируйте две новые. Первая
строка содержит только цифры, вторая — только буквы.
Выведите новые строки построчно.
"""


def fourthy(mas: str) -> tuple[str, str]:
    digit_str, letter_str = '', ''
    for i in mas:
        if i.isdigit():
            digit_str += i
        else:
            letter_str += i
    return f'Строка чисел - {digit_str}', f'Строка букв - {letter_str}'


def main(n: int, *, mas: str) -> bool | list[str] | tuple[str, str]:
    if n == '1' and first(mas) is not False: return [f'{first(mas)}']
    if n == '2' and second(mas) is not False: return [f'Слова начинающиеся с буквы r: {second(mas)}']
    if n == '3' and third() is not False: return [f'Рандомная строка - {third()}']
    if n == '4' and fourthy(mas) is not False:
        return fourthy(mas)
    else:
        return False


if __name__ == '__main__':
    main()
