import codecs

from config import *


# Перевод в другую (до 16-ти) систему счисления из десятичной
def in_notation(string: int, base: int) -> str:

    extra = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    ans = ''

    while string > 0:
        if string % base < 10:
            ans += str(string % base)
        else:
            ans += extra[string % base]
        string //= base
    if ans != '':
        return ans[::-1]
    else:
        return '0'


# Перевод из любой (до 16ти) в десятеричную систему счисления
def ten_notation(string: str, base: int) -> str | int:
    extra = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
             'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

    ans = 0
    for num, ind in zip(str(string)[::-1], range(0, len(str(string)))):
        if num.isdigit():
            ans += int(int(num) * base ** ind)
        else:
            ans += int(int(extra[num]) * base ** ind)
    return ans


# Ввод текста и ключа
def get_info() -> tuple[str, str]:
    text_message = input('Введите текст: \n').rstrip()
    password = input('Введите пароль: ').rstrip()
    return text_message, password


# Добавление незначащих нулей
def added(text: str, num: int) -> str:
    while len(text) % num != 0:
        text = '0' + text
    if len(text) == 0:
        text = '0000'
    return text


# разделение текста на блоки по 64 бита
def separate(text: str, num: int) -> str:
    temp = []
    length = 0
    line = ''
    for i in text:  # text = аааааааааааа
        if length == num:
            temp.append(line)
            length = 0
            line = i
        else:
            line += i
        length += 1
    if line != '': temp.append(line)
    return temp


def get_pass(left_pw, right_pw) -> list[str]:
    pwrd = []
    # Разбиение ключа на 2 части и смещение на n бит влево
    for rnd in range(16):
        # Побитовое смещение в зависимости от цикла
        left_pw = left_pw[KEY_ROUND[rnd]::] + left_pw[0:KEY_ROUND[rnd]]
        right_pw = right_pw[KEY_ROUND[rnd]::] + right_pw[0:KEY_ROUND[rnd]]

        # Перестановка бит в ключе
        new_pass = left_pw + right_pw
        new_pass = ''.join([new_pass[i - 1] for i in KEY_PERMUTATION_SECOND])

        # Разделение ключа по 4 бита и перевод в шестнадцатеричную систему
        new_pass = ''.join(separate(new_pass, 4))
        pwrd.append(''.join([in_notation(ten_notation(i, 2), 16) for i in separate(new_pass, 4)]))

    return pwrd


def XOR(arg1: str, arg2: str) -> str: return str(int(arg1) ^ int(arg2))


def encrypted(message: str, password: str) -> str:
    message = ''.join([added(in_notation(ten_notation(sym, 16), 2), 4) for sym in message])

    # Первая перестановка бит в сообщении
    new_message = ''.join([message[i - 1] for i in FIRST_PERMUTATION])

    left_block_0 = new_message[0:32]
    right_block_0 = new_message[32::]

    # 16 раундов
    for rnd in range(16):

        # Правая часть сообщения проходит вторую перестановку и XOR с ключом
        right_block_perm = ''.join([right_block_0[i - 1] for i in SECOND_PERMUTATION])

        bin_key = ''.join([added(in_notation(ten_notation(i, 16), 2), 4) for i in password[rnd]])

        cipher = ''.join([XOR(a, b) for a, b in zip(bin_key, right_block_perm)])

        # Разделение XORed сообщения на блоки по 6 бит
        s_blocks = separate(cipher, 6)

        s_cipher = []
        # Проход по S-блоку
        for ind in range(len(s_blocks)):
            first_half = ten_notation(s_blocks[ind][0] + s_blocks[ind][-1], 2)
            second_half = ten_notation(s_blocks[ind][1:5], 2)

            s_cipher.append(CIPHER_S_BLOCKS[ind + 1][first_half][second_half])

        # Перевод в двоичную S-блок сообщения
        s_cipher = ''.join([added(in_notation(i, 2), 4) for i in s_cipher])

        # Последняя перестановка в S-блок сообщении и XOR с левой частью
        cipher = ''.join([s_cipher[i - 1] for i in LAST_PERMUTATION])
        cipher = ''.join([XOR(a, b) for a, b in zip(cipher, left_block_0)])
        left_block_0 = cipher
        if (rnd != 15):
            left_block_0, right_block_0 = right_block_0, left_block_0

    cipher = left_block_0 + right_block_0
    cipher = ''.join([cipher[i - 1] for i in IP_PERMUTATION])

    cipher = separate(cipher, 4)
    cipher = ''.join(in_notation(ten_notation(i, 2), 16) for i in cipher)
    return cipher


# Создание 56-битного ключа перестановкой P-блока
def generate_key() -> tuple[str, list[str]]:
    message, password = get_info()

    password = added(password.encode("utf-8").hex().upper(), 16)
    password = ''.join([added(in_notation(ten_notation(sym, 16), 2), 4) for sym in password])
    # Создание 56-битного ключа перестановкой P-блока
    password = ''.join([password[i - 1] for i in KEY_PERMUTATION_FIRST])

    left_pw = password[:len(password) // 2]
    right_pw = password[(len(password) // 2)::]

    pwrd = get_pass(left_pw, right_pw)

    return message, pwrd


def des(turn: int) -> list[None] | None:
    message, list_of_keys = generate_key()

    if turn == 0:
        message = list(message)
        for i in range(len(message)):
            message[i] = separate(message[i].encode("utf-8").hex().upper().replace("FFFE", ''), 16)

        ans = []

        for msg in message:
            temp = []
            for i in msg:
                i = added(i, 16)
                temp.append(encrypted(i, list_of_keys))
            ans.append(' '.join(temp))
        return [print(i, end=' ') for i in ans]

    if turn == 1:
        message = message.split(' ')
        temp = []
        for msg in message:
            a = (bytes.fromhex(encrypted(msg, list_of_keys[::-1])).decode('UTF-8')).replace('\x00', '')
            temp.append(a)
        return print(''.join(temp))
    else:
        return print('Вводить надо либо 0, либо 1')