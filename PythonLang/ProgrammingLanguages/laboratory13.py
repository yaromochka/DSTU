import re


# abcdefghijklmnopqrstuv18340
def first(mas):
    if re.fullmatch(r'abcdefghijklmnopqrstuv18340', mas): return [f'Строка {mas} является строкой abcdefghijklmnopqrstuv18340']
    else: return [f'Строка {mas} не является строкой abcdefghijklmnopqrstuv18340']


def second(mas):
    if re.fullmatch(r'[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12}', mas): return [f'Строка {mas} является строкой GUID']
    else: return [f'Строка {mas} не является строкой GUID']


def third(mas):
    if re.fullmatch(r'^([0-9A-Fa-f]{2}[:]){5}[0-9A-Fa-f]{2}$', mas): return [f'Строка {mas} является MAC-адресом']
    else: return [f'Строка {mas} не является MAC-адресом']


def fourth(mas):
    if re.fullmatch(r'^(https|http):\/\/[a-z0-9]{2,}\.(com|ru)$', mas): return [f'Строка {mas} является URL-адресом']
    else: return [f'Строка {mas} не является URL-адресом']


def fifth(mas):
    if re.fullmatch(r'^#[0-9a-fA-F]{6}$', mas): return [f'Строка {mas} является идентефикаторов цвета в HTML']
    else: return [f'Строка {mas} не является идентефикатором цвета в HTML']


def sixth(mas):
    if re.fullmatch(r'^(0[1-9]|1\d|2[0-8])/(0[1-9]|1[0-2])/((?:1[6-9]|[2-9]\d)?\d{2})$|^29/02/(?:(?:(?:1[6-9]|[2-9]\d)(?:0[' \
                    r'48]|[2468][048]|[13579][26]))|(?:16|[2468][048]|[3579][26])00)$', mas): return [f'Строка {mas} является датой']
    else: return [f'Строка {mas} не является датой']


def seventh(mas):
    if re.fullmatch(r'^\w+@\w+\.?\w+}$', mas): return [f'Строка {mas} является валидным E-mail адресом']
    else: return [f'Строка {mas} не является валидным E-mail адресом']


def eighth(mas):
    if re.fullmatch(r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', mas): return [f'Строка {mas} является IP адресом']
    else: return [f'Строка {mas} не является IP адресом']


def ninth(mas):
    if re.search(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z0-9_]{8,}$', mas): return [f'Строка {mas} является надёжным паролем']
    else: return [f'Строка {mas} не является надёжным паролем']


def tenth(mas):
    if re.fullmatch(r'[1-9]\d{5}$', mas): return [f'Строка {mas} является шестизначным числом']
    else: return [f'Строка {mas} не является шестизначным числом']


def eleventh(mas):
    patt = r'(\d+(?:\.\d+)?)\s+(USD|RUB|EU)'
    matches = re.findall(patt, mas)
    return [f'В тексте найдены валюты: {[str(price) + ' ' + currency for price, currency in matches]}']


def twelfeth(mas):
    if re.search(r'^\b\d+(?:\s*\+)$', mas): return [f'В строке {mas} есть цифры, за которыми не стоит «+»']
    else: return [f'В строке {mas} нет цифр, за которыми не стоит «+»']


def thirteenth(mas):
    match = re.fullmatch(r'[^()]*((\([^()]*\)[^()]*)*)', mas)
    if match and match.group(0).count('(') == match.group(0).count(')'): return [f'В строке {mas} правильно написано выражение со скобками']
    else: return [f'В строке {mas} неправильно написано выражение со скобками']


def main(n, *, mas):
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
    if n == '12': return twelfeth(mas)
    if n == '13': return thirteenth(mas)
    else: return False


if __name__ == '__main__':
    main()