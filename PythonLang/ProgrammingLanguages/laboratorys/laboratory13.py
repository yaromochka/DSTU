import re


"""
1.	Написать регулярное выражение, определяющее является ли данная строка строкой "abcdefghijklmnopqrstuv18340" или нет.
– пример правильных выражений: abcdefghijklmnopqrstuv18340.
– пример неправильных выражений: abcdefghijklmnoasdfasdpqrstuv18340.
"""


# abcdefghijklmnopqrstuv18340
def first(mas: str) -> list[str]:
    if re.fullmatch(r'abcdefghijklmnopqrstuv18340', mas): return [f'Строка {mas} является строкой abcdefghijklmnopqrstuv18340']
    else: return [f'Строка {mas} не является строкой abcdefghijklmnopqrstuv18340']


"""
2.	Написать регулярное выражение, определяющее является ли данная строка GUID с или без скобок. Где GUID это строчка,
 состоящая из 8, 4, 4, 4, 12 шестнадцатеричных цифр разделенных тире.
– пример правильных выражений: e02fd0e4-00fd-090A-ca30-0d00a0038ba0.
– пример неправильных выражений: e02fd0e400fd090Aca300d00a0038ba0.
"""


def second(mas: str) -> list[str]:
    if re.fullmatch(r'[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12}', mas): return [f'Строка {mas} является строкой GUID']
    else: return [f'Строка {mas} не является строкой GUID']


"""
3.	Написать регулярное выражение, определяющее является ли заданная строка правильным MAC-адресом.
– пример правильных выражений: aE:dC:cA:56:76:54.
– пример неправильных выражений: 01:23:45:67:89:Az.
"""


def third(mas: str) -> list[str]:
    if re.fullmatch(r'^([0-9A-Fa-f]{2}[:]){5}[0-9A-Fa-f]{2}$', mas): return [f'Строка {mas} является MAC-адресом']
    else: return [f'Строка {mas} не является MAC-адресом']


"""
4.	Написать регулярное выражение, определяющее является ли данная строчка валидным URL адресом. В данной задаче правильным URL считаются адреса http и https, явное указание протокола также может отсутствовать. Учитываются только адреса, состоящие из символов, т.е. IP адреса в качестве URL не присутствуют при проверке. Допускаются поддомены, указание порта доступа через двоеточие, GET запросы с передачей параметров, доступ к подпапкам на домене, допускается наличие якоря через решетку. Однобуквенные домены считаются запрещенными. Запрещены спецсимволы, например «–» в начале и конце имени домена. Запрещен символ «_» и пробел в имени домена. При составлении регулярного выражения ориентируйтесь на список правильных и неправильных выражений заданных ниже.
– пример правильных выражений: http://www.example.com, http://example.com.
– пример неправильных выражений: Just Text, http://a.com.
"""


def fourth(mas: str) -> list[str]:
    if re.fullmatch(r'^(https|http):\/\/[a-z0-9]{2,}\.(com|ru)$', mas): return [f'Строка {mas} является URL-адресом']
    else: return [f'Строка {mas} не является URL-адресом']


"""
5.	Написать регулярное выражение, определяющее является ли данная строчка шестнадцатиричным идентификатором цвета в HTML.
 Где #FFFFFF для белого, #000000 для черного, #FF0000 для красного и т.д.
– пример правильных выражений: #FFFFFF, #FF3421, #00ff00.
– пример неправильных выражений: 232323, f#fddee, #fd2.
"""


def fifth(mas: str) -> list[str]:
    if re.fullmatch(r'^#[0-9a-fA-F]{6}$', mas): return [f'Строка {mas} является идентефикаторов цвета в HTML']
    else: return [f'Строка {mas} не является идентификатором цвета в HTML']


"""
6.	Написать регулярное выражение, определяющее является ли данная строчка датой в формате dd/mm/yyyy. Начиная с 1600 года до 9999 года.
– пример правильных выражений: 29/02/2000, 30/04/2003, 01/01/2003.
– пример неправильных выражений: 29/02/2001, 30-04-2003, 1/1/1899.
"""


def sixth(mas: str) -> list[str]:
    if re.fullmatch(r'^(0[1-9]|1\d|2[0-8])/(0[1-9]|1[0-2])/((?:1[6-9]|[2-9]\d)?\d{2})$|^29/02/(?:(?:(?:1[6-9]|[2-9]\d)(?:0[' \
                    r'48]|[2468][048]|[13579][26]))|(?:16|[2468][048]|[3579][26])00)$', mas): return [f'Строка {mas} является датой']
    else: return [f'Строка {mas} не является датой']


"""
7.	Написать регулярное выражение, определяющее является ли данная строчка валидным E-mail адресом согласно RFC под номером 2822.
– пример правильных выражений: user@example.com, root@localhost
– пример неправильных выражений: bug@@@com.ru, @val.ru, Just Text2.
"""


def seventh(mas: str) -> list[str]:
    if re.fullmatch(r'^\w+@\w+\.?\w+}$', mas): return [f'Строка {mas} является валидным E-mail адресом']
    else: return [f'Строка {mas} не является валидным E-mail адресом']


"""
8.	Составить регулярное выражение, определяющее является ли заданная строка IP адресом, записанным в десятичном виде.
– пример правильных выражений: 127.0.0.1, 255.255.255.0.
– пример неправильных выражений: 1300.6.7.8, abc.def.gha.bcd.
"""


def eighth(mas: str) -> list[str]:
    if re.fullmatch(r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', mas): return [f'Строка {mas} является IP адресом']
    else: return [f'Строка {mas} не является IP адресом']


"""
9.	Проверить, надежно ли составлен пароль. Пароль считается надежным, если он состоит из 8 или более символов.
Где символом может быть английская буква, цифра и знак подчеркивания. Пароль должен содержать хотя бы одну заглавную букву,
одну маленькую букву и одну цифру.
– пример правильных выражений: C00l_Pass, SupperPas1.
– пример неправильных выражений: Cool_pass, C00l.
"""


def ninth(mas: str) -> list[str]:
    if re.search(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z0-9_]{8,}$', mas): return [f'Строка {mas} является надёжным паролем']
    else: return [f'Строка {mas} не является надёжным паролем']


"""
10.	Проверить является ли заданная строка шестизначным числом, записанным в десятичной системе счисления без нулей в старших разрядах.
– пример правильных выражений: 123456, 234567.
– пример неправильных выражений: 1234567, 12345.
"""


def tenth(mas: str) -> list[str]:
    if re.fullmatch(r'[1-9]\d{5}$', mas): return [f'Строка {mas} является шестизначным числом']
    else: return [f'Строка {mas} не является шестизначным числом']


"""
11.	Есть текст со списками цен. Извлечь из него цены в USD, RUR, EU.
– пример правильных выражений: 23.78 USD.
– пример неправильных выражений: 22 UDD, 0.002 USD.
"""


def eleventh(mas: str) -> list[str]:
    patt = r'(\d+(?:\.\d+)?)\s+(USD|RUB|EU)'
    matches = re.findall(patt, mas)
    return [f'В тексте найдены валюты: {[str(price) + ' ' + currency for price, currency in matches]}']


"""
12.	Проверить существуют ли в тексте цифры, за которыми не стоит «+».
– пример правильных выражений: (3 + 5) – 9 × 4.
– пример неправильных выражений: 2 * 9 – 6 × 5.
"""


def twelfth(mas: str) -> list[str]:
    if re.search(r'^\b\d+(?:\s*\+)$', mas): return [f'В строке {mas} есть цифры, за которыми не стоит «+»']
    else: return [f'В строке {mas} нет цифр, за которыми не стоит «+»']


"""
13.	Создать запрос для вывода только правильно написанных выражений со скобками (количество открытых и закрытых скобок должно быть одинаково).
– пример правильных выражений: (3 + 5) – 9 × 4.
– пример неправильных выражений: ((3 + 5) – 9 × 4.
"""


def thirteenth(mas: str) -> list[str]:
    match = re.fullmatch(r'[^()]*((\([^()]*\)[^()]*)*)', mas)
    if match and match.group(0).count('(') == match.group(0).count(')'): return [f'В строке {mas} правильно написано выражение со скобками']
    else: return [f'В строке {mas} неправильно написано выражение со скобками']


def main(n: int, *, mas: str) -> bool | list[str]:
    if n == '1': return first(mas)
    if n == '2': return second(mas)
    if n == '3': return third(mas)
    if n == '4': return fourth(mas)
    if n == '5': return fifth(mas)
    if n == '6': return sixth(mas)
    if n == '7': return seventh(mas)
    if n == '8': return eighth(mas)
    if n == '9': return ninth(mas)
    if n == '10': return tenth(mas)
    if n == '11': return eleventh(mas)
    if n == '12': return twelfth(mas)
    if n == '13': return thirteenth(mas)
    else: return False


if __name__ == '__main__':
    main()