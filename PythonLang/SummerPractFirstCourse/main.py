# Побитовая перестановка текста
FIRST_PERMUTATION = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

# Сжатие ключа до 56 бит
KEY_PERMUTATION_FIRST = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]

# Сжатие ключа до 48 бит
KEY_PERMUTATION_SECOND = [
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]

# Расширение правой части с 32 до 48 бит
SECOND_PERMUTATION = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

LAST_PERMUTATION = [
    16, 7, 20, 21,
    29, 12, 28, 17,
    1, 15, 23, 26,
    5, 18, 31, 10,
    2, 8, 24, 14,
    32, 27, 3, 9,
    19, 13, 30, 6,
    22, 11, 4, 25
]

IP_PERMUTATION = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25,
]

CIPHER_S_BLOCKS = {
    1: [
        [14, 4,  13, 1,  2,  15, 11, 8,  3,  10, 6,  12, 5,  9,  0,  7],
        [0,  15, 7,  4,  14, 2,  13, 1,  10, 6,  12, 11, 9,  5,  3,  8],
        [4,  1,  14, 8,  13, 6,  2,  11, 15, 12, 9,  7,  3,  10, 5,  0],
        [15, 12, 8,  2,  4,  9,  1,  7,  5,  11, 3,  14, 10, 0,  6,  13]
    ],
    2: [
        [15, 1,  8,  14, 6,  11, 3,  4,  9,  7,  2,  13, 12, 0,  5,  10],
        [3,  13, 4,  7,  15, 2,  8,  14, 12, 0,  1,  10, 6,  9,  11, 5],
        [0,  14, 7,  11, 10, 4,  13, 1,  5,  8,  12, 6,  9,  3,  2,  15],
        [13, 8,  10, 1,  3,  15, 4,  2,  11, 6,  7,  12, 0,  5,  14, 9]
    ],
    3: [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    4: [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    5: [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    6: [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    7: [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    8: [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
}

# Индекс сдвига бит влево в ключе в зависимости от номера раунда
KEY_ROUND = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]


# Перевод в другую (до 16-ти) систему счисления из десятичной
def in_notation(string: int, base: int) -> str:
    try: (string // base)
    except TypeError: return 'Вводимые данные должны быть int'

    if base < 2 or base > 16:
        return 'Неверная система счисления'
    else:
        extra = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
        ans = ''

        while string > 0:
            if string % base < 10:
                ans += str(string % base)
            else:
                ans += extra[string % base]
            string //= base
        if ans != '': return ans[::-1]
        else: return '0'


# Перевод из любой (до 16ти) в десятиричную систему счисления
def ten_notation(string: str, base: int) -> str | int:
    extra = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
             'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

    try: all(extra[i] for i, j in zip(string, str(base)))
    except TypeError: return 'Неверные входные данные'
    if max([extra[i] for i in str(string)]) < int(base):

        ans = 0
        for num, ind in zip(str(string)[::-1], range(0, len(str(string)))):
            if num.isdigit():
                ans += int(int(num) * base ** ind)
            else:
                ans += int(int(extra[num]) * base ** ind)
        return ans
    else:
        return 'Неверная система счисления'


# Ввод текста и ключа
def get_info() -> tuple(str, str):
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
    for i in text: # text = аааааааааааа
        if length == num:
            temp.append(line)
            length = 0
            line = i
        else:
            line += i
        length += 1
    if line != '': temp.append(line)
    return temp


def get_pass(left_pw, right_pw):
    pwrd = []
    # Разбиение ключа на 2 части и смещение на n бит влево
    for rnd in range(16):
        # Побитовое смещение в зависимости от цикла
        left_pw = left_pw[KEY_ROUND[rnd]::] + left_pw[0:KEY_ROUND[rnd]]
        right_pw = right_pw[KEY_ROUND[rnd]::] + right_pw[0:KEY_ROUND[rnd]]

        # Перестановка бит в ключе
        new_pass = left_pw + right_pw
        new_pass = ''.join([new_pass[i - 1] for i in KEY_PERMUTATION_SECOND])

        # Разделение ключа по 4 бита и перевод в шестнадцатиричную систему
        new_pass = ''.join(separate(new_pass, 4))
        pwrd.append(''.join([in_notation(ten_notation(i, 2), 16) for i in separate(new_pass, 4)]))

    return pwrd


def XOR(arg1: str, arg2: str) -> str: return str(int(arg1) ^ int(arg2))


def encrypted(message: str, password: str) -> str:
    message = ''.join([added(in_notation(ten_notation(sym, 16), 2), 4) for sym in message])
    # Первая перестанвока бит в сообщении
    new_message = ''.join([message[i - 1] for i in FIRST_PERMUTATION])
    # print(f'После начальной перестановки: {"".join([in_notation(ten_notation(i, 2), 16) for i in separate(new_message, 4)])}')

    L0 = new_message[0:32]
    R0 = new_message[32::]

    # 16 раундов
    for rnd in range(16):

        # Правая часть сообщения проходит вторую перестановку и XOR с ключом
        R0_perm = ''.join([R0[i - 1] for i in SECOND_PERMUTATION])

        bin_key = ''.join([added(in_notation(ten_notation(i, 16), 2), 4) for i in password[rnd]])

        cipher = ''.join([XOR(a, b) for a,b in zip(bin_key, R0_perm)])

        # Разделение XORed сообщения на блоки по 6 бит
        S_blocks = separate(cipher, 6)

        S_cipher = []
        # Проход по S-блоку
        for ind in range(len(S_blocks)):

            first = S_blocks[ind][0] + S_blocks[ind][-1]
            second = S_blocks[ind][1:5]

            first = ten_notation(first, 2)
            second = ten_notation(second, 2)

            S_cipher.append(CIPHER_S_BLOCKS[ind + 1][first][second])

        # Перевод в двоичную S-блок сообщения
        S_cipher = ''.join([added(in_notation(i, 2), 4) for i in S_cipher])

        # Последняя перестановка в S-блок сообщении и XOR с левой частью
        cipher = ''.join([S_cipher[i - 1] for i in LAST_PERMUTATION])
        cipher = ''.join([XOR(a, b) for a, b in zip(cipher, L0)])
        L0 = cipher
        if (rnd != 15):
            L0, R0 = R0, L0
        # print(f'Round {rnd + 1}', ''.join([in_notation(ten_notation(i, 2), 16) for i in separate(L0, 4)]), ''.join([in_notation(ten_notation(i, 2), 16) for i in separate(R0, 4)]), password[rnd])

    cipher = L0 + R0
    cipher = ''.join([cipher[i - 1] for i in IP_PERMUTATION])

    cipher = separate(cipher, 4)
    cipher = ''.join(in_notation(ten_notation(i, 2), 16) for i in cipher)
    return cipher


def main() -> None:
    try: x = int(input('Вы хотите кодировать(0) или декодировать(1) текст?: '))
    except ValueError: return print('Либо 0, либо 1, а не буковки')
    if x == 0:
        message, password = get_info()
        message = list(message)
        for i in range(len(message)):
            message[i] = separate(message[i].encode('UTF-8').hex().upper(), 16)

        ans = []
        password = added(password.encode('UTF-8').hex().upper(), 16)
        password = ''.join([added(in_notation(ten_notation(sym, 16), 2), 4) for sym in password])
        # Создание 56-битного ключа перестановкой P-блока
        password = ''.join([password[i - 1] for i in KEY_PERMUTATION_FIRST])

        left_pw = password[:len(password) // 2]
        right_pw = password[(len(password) // 2)::]

        pwrd = get_pass(left_pw, right_pw)

        # return print(f'Зашифрованное сообщение: {encrypted(message, pwrd)}')
        for msg in message:
            temp = []
            for i in msg:
                i = added(i, 16)
                temp.append(encrypted(i, pwrd))
            ans.append(' '.join(temp))
        return [print(i, end=' ') for i in ans]

    if x == 1:
        # Создание 56-битного ключа перестановкой P-блока
        message, password = get_info()
        message = message.split(' ')

        password = added(password.encode('UTF-8').hex().upper(), 16)
        password = ''.join([added(in_notation(ten_notation(sym, 16), 2), 4) for sym in password])
        # Создание 56-битного ключа перестановкой P-блока
        password = ''.join([password[i - 1] for i in KEY_PERMUTATION_FIRST])

        left_pw = password[:len(password) // 2]
        right_pw = password[(len(password) // 2)::]

        pwrd = get_pass(left_pw, right_pw)
        temp = []
        ans = []
        try:
            for msg in message:
                a = (bytes.fromhex(encrypted(msg, pwrd[::-1])).decode('UTF-8')).replace('\x00', '')
                temp.append(a)
            return print(''.join(temp))
        except: return print('Ошибка. Вероятно, неправильный пароль')

    else:
        return print('Вводить надо либо 0, либо 1')


if __name__ == '__main__':
    main()
