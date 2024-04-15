from csv import reader
import re
from typing import Dict, List, Any


# Считывание данных из файла
def dictor() -> dict[Any, Any]:
    with open(r"/PythonLang/ProgrammingLanguages/files/student.csv") as f:
        file, temp = list(reader(f)), {}
        for i in file[1::]:
            i = (''.join(i)).split(';')
            temp[i[0]] = i[1::]
        return temp


"""
1. Пусть список студентов представлен в виде структуры [[№, ФИО, Возраст,
Группа],[№, ФИО, Возраст, Группа],[№, ФИО, Возраст, Группа]].
Преобразуйте список в словарь вида: {№: [ФИО, Возраст, Группа], №:
[....], №: [....]}
"""


def first() -> reversed[list[str]]:
    return reversed(['Файл, преобразованный в словарь', *[f'{k[0]}:{" ".join(k[1])}' for k in dictor().items()]])


"""
1. Увеличить возраст конкретного студента на 1. Поиск по «ФИО»
(«ФИО» студента необходимо ввести с клавиатуры).
"""


def increase_age(s: str) -> reversed[list[str]]:
    fam = s.split(' ')[2]
    temp = dictor()
    for i, j in temp.items():
        if fam in j[0]:
            temp[i] = [j[0], str(int(j[1]) + 1), j[2]]
    return reversed(['Словарь:', *[f'{k[0]}:{" ".join(k[1])}' for k in temp.items()]])


"""
2. Изменить «ФИО» студента. Поиск по «ФИО» (старое и новое «ФИО»
студента необходимо ввести с клавиатуры).
"""


def change_name(s: str) -> reversed[list[str]]:
    fname, sname = s.split(' ')[4], s.split(' ')[6]
    temp = dictor()
    for i, j in temp.items():
        if fname in j[0]: temp[i] = [sname + ' ' + ' '.join(j[0].split(' ')[1::]), j[1], j[2]]
    return reversed(['Словарь:', *[f'{k[0]}:{" ".join(k[1])}' for k in temp.items()]])


"""
3. Увеличить возраст конкретного студента на 1. Поиск по «№» («№»
студента необходимо ввести с клавиатуры).
"""


def increase_age_num(s: str) -> reversed[list[str]]:
    num, temp = s.split(' ')[5], dictor()
    temp[num] = [temp[num][0], str(int(temp[num][1]) + 1), temp[num][2]]
    return reversed(['Словарь:', *[f'{k[0]}:{" ".join(k[1])}' for k in temp.items()]])


"""
4. Изменить группу студента. Поиск по «ФИО» («ФИО» студента и
новый номер группы необходимо ввести с клавиатуры).
"""


def change_group(s: str) -> reversed[list[str]]:
    fam, group = s.split(' ')[3], s.split(' ')[5]
    temp = dictor()
    for i, j in temp.items():
        if fam in j[0]: temp[i] = [j[0], j[1], group]
    return reversed(['Словарь:', *[f'{k[0]}:{" ".join(k[1])}' for k in temp.items()]])


"""
5. Удалить запись о студенте. Поиск по «№» («№» студента, которого
нужно удалить из списка, задается с клавиатуры)
"""


def delete_student(s: str) -> reversed[list[str]]:
    num, temp = s.split(' ')[-1], dictor()
    del temp[num]
    return reversed(['Словарь:', *[f'{k[0]}:{" ".join(k[1])}' for k in temp.items()]])


"""
6. Если возраст студента больше 22 уменьшить его на 1.
"""


def decrease_age() -> reversed[list[str]]:
    temp = dictor()
    for i, j in temp.items():
        if int(j[1]) > 22: temp[i] = [j[0], str(int(j[1]) - 1), j[2]]
    return reversed(['Словарь:', *[f'{k[0]}:{" ".join(k[1])}' for k in temp.items()]])


"""
7. Если возраст студента равен 23, удалить его из списка.
"""


def delete_student_age() -> reversed[list[str]]:
    temp = dictor()
    t = temp.copy()
    for i, j in t.items():
        if int(j[1]) == 23: del temp[i]
    return reversed(['Словарь:', *[f'{k[0]}:{" ".join(k[1])}' for k in temp.items()]])


"""
8. У всех студентов с фамилией «Иванов» увеличить возраст на 1
"""


def increase_age_ivanov() -> reversed[list[str]]:
    fam = 'Иванов'
    temp = dictor()
    for i, j in temp.items():
        if fam in j[0]: temp[i] = [j[0], str(int(j[1]) + 1), j[2]]
    return reversed(['Словарь:', *[f'{k[0]}:{" ".join(k[1])}' for k in temp.items()]])


"""
9. У студентов с фамилией «Иванов» изменить фамилию на «Сидоров».
"""


def change_ivanov() -> reversed[list[str]]:
    fam = 'Иванов'
    temp = dictor()
    for i, j in temp.items():
        if fam in j[0]: temp[i] = ['Сидоров ' + ' '.join(j[0].split(' ')[1::]), j[1], j[2]]
    return reversed(['Словарь:', *[f'{k[0]}:{" ".join(k[1])}' for k in temp.items()]])


"""
10.Поменять «ФИО» и «Группа» местами
"""


def swap_groups() -> reversed[list[str]]:
    temp = dictor()
    for i, j in temp.items():
        temp[i] = [j[2], j[1], j[0]]
    return reversed(['Словарь:', *[f'{k[0]}:{" ".join(k[1])}' for k in temp.items()]])


"""
2. Добавьте к задаче №1 для словаря возможность (без преобразования
словаря обратно в список)
"""


def second(mas: str) -> bool | reversed[list[str]]:
    commands = {
        r"[иИ]зменить возраст \w+ на 1": increase_age,
        r"[иИ]зменить ФИО студента с \w+ на \w+": change_name,
        r"[уУ]величить возраст студента с номером \d+ на 1": increase_age_num,
        r"[Ии]зменить группу студента \w+ на \w+-\d+": change_group,
        r"[Уу]далить запись о студенте с номером \d+": delete_student,
        r"Если возраст студента больше 22, уменьшить его на 1": decrease_age,
        r"Если возраст студента равен 23, удалить его из списка": delete_student_age,
        r"У всех студентов с фамилией Иванов увеличить возраст на 1": increase_age_ivanov,
        r"У студентов с фамилией Иванов изменить фамилию на Сидоров": change_ivanov,
        r"Поменять ФИО и группа местами": swap_groups
    }

    for string, function in commands.items():
        if re.fullmatch(string, mas): return function(mas)
    return False


"""
1. Списка студентов (а также информацию о них) группы 'БО-111111'.
"""


def print_group() -> reversed[list[str]]:
    group = 'БО-111111'
    temp = dictor()
    return reversed(['Словарь:', *[f'{k[0]}:{" ".join(k[1])}' for k in temp.items() if group in k[1][2]]])


"""
2. Списка студентов (а также информацию о них) с номерами 1-10
"""


def print_numbers() -> reversed[list[str]]:
    temp = dictor()
    return reversed(['Словарь:', *[f'{k[0]}:{" ".join(k[1])}' for k in temp.items() if 1 <= int(k[0]) <= 2]])


"""
3. Списка студентов (а также информацию о них) в возрасте 22 лет.
"""


def print_age() -> reversed[list[str]]:
    temp = dictor()
    return reversed(['Словарь:', *[f'{k[0]}:{" ".join(k[1])}' for k in temp.items() if int(k[1][1]) == 22]])


"""
4. Список студентов (а также информацию о них) с фамилией 'Иванов'.
"""


def print_surname() -> reversed[list[str]]:
    temp = dictor()
    return reversed(['Словарь:', *[f'{k[0]}:{" ".join(k[1])}' for k in temp.items() if 'Иванов' in k[1][0]]])


"""
5. Списка студентов (а также информацию о них), чьи фамилии
заканчиваются на «а».
"""


def print_surname_a() -> reversed[list[str]]:
    temp = dictor()
    return reversed(
        ['Словарь:', *[f'{k[0]}:{" ".join(k[1])}' for k in temp.items() if k[1][0].split(' ')[0][-1] == 'а']])


"""
6. Списка студентов (а также информацию о них), чей возраст – четное
число.
"""


def print_age_even() -> reversed[list[str]]:
    temp = dictor()
    return reversed(['Словарь:', *[f'{k[0]}:{" ".join(k[1])}' for k in temp.items() if int(k[1][1]) % 2 == 0]])

"""
7. Списка студентов (а также информацию о них), если в возрасте
студента встречается число 5.
"""


def print_age_five() -> reversed[list[str]]:
    temp = dictor()
    return reversed(['Словарь:', *[f'{k[0]}:{" ".join(k[1])}' for k in temp.items() if '5' in k[1][1]]])


"""
8. Списка студентов (а также информацию о них), если их номера группы
длиннее 7 символов
"""


def print_len_group() -> reversed[list[str]]:
    temp = dictor()
    return reversed(['Словарь:', *[f'{k[0]}:{" ".join(k[1])}' for k in temp.items() if len(k[1][2]) > 7]])


"""
9. Списка студентов (а также информацию о них), если их «№» четное
число.
"""


def print_even_num() -> reversed[list[str]]:
    temp = dictor()
    return reversed(['Словарь:', *[f'{k[0]}:{" ".join(k[1])}' for k in temp.items() if int(k[0]) % 2 == 0]])


"""
10. Списка студентов (а также информацию о них), если их номер группы
заканчивается на «1»
"""


def print_group_one() -> reversed[list[str]]:
    temp = dictor()
    return reversed(['Словарь:', *[f'{k[0]}:{" ".join(k[1])}' for k in temp.items() if k[1][2][-1] == '1']])


"""
3. Добавьте к пользовательскому интерфейсу из задачи №2 возможность
вывода из словаря (без его преобразования в список)
"""


def third(mas: str) -> bool | reversed[list[str]]:
    commands = {
        "Вывести список студентов группы БО-111111": print_group,
        "Вывести список студентов с номерами от 1 до 2": print_numbers,
        "Вывести список студентов в возрасте 22 лет": print_age,
        "Вывести список студентов с фамилией Иванов": print_surname,
        "Вывести список студентов, чьи фамилии заканчиваются на 'а'": print_surname_a,
        "Вывести список студентов, чей возраст - это чётное число": print_age_even,
        "Вывести список студентов, если в возрасте студента встречается число 5": print_age_five,
        "Вывести список студентов, если их номера группы длиннее 7 символов": print_len_group,
        "Вывести список студентов, если их номер - чётное число": print_even_num,
        "Вывести список студентов, если их номер группы заканчивается на '1'": print_group_one
    }

    for string, function in commands.items():
        if re.fullmatch(string, mas):
            return function(mas)
    return False


def main(n: int, *, mas: str) -> bool | reversed[list[str]]:
    if n == '1': return first()
    if n == '2': return second(mas)
    if n == '3':
        return third(mas)
    else:
        return False


if __name__ == '__main__':
    main()
