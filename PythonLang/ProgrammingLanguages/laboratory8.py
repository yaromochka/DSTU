from csv import reader
import re


def dictor():
    with open(r"/Users/yaromochka/IdeaProjects/DSTU/PythonLang/ProgrammingLanguages/files/student.csv") as f:
        file, temp = list(reader(f)), {}
        for i in file[1::]:
                i = (''.join(i)).split(';')
                temp[i[0]] = i[1::]
        return temp


def first():
    return reversed(['Файл, преобразованный в словарь', *[f'{k[0]}:{" ".join(k[1])}' for k in dictor().items()]])


def increase_age(s): 
    fam = s.split(' ')[2]
    temp = dictor()
    for i, j in temp.items(): 
        if fam in j[0]: temp[i] = [j[0], str(int(j[1]) + 1), j[2]]
    return reversed(['Словарь:', *[f'{k[0]}:{" ".join(k[1])}' for k in temp.items()]])
    
def change_name(s): 
    fname, sname = s.split(' ')[4], s.split(' ')[6]
    temp = dictor()
    for i, j in temp.items(): 
        if fname in j[0]: temp[i] = [sname + ' ' + ' '.join(j[0].split(' ')[1::]), j[1], j[2]]
    return reversed(['Словарь:', *[f'{k[0]}:{" ".join(k[1])}' for k in temp.items()]])

def increase_age_num(s): 
    num, temp = s.split(' ')[5], dictor()
    temp[num] = [temp[num][0], str(int(temp[num][1]) + 1), temp[num][2]]
    return reversed(['Словарь:', *[f'{k[0]}:{" ".join(k[1])}' for k in temp.items()]])

def change_group(s): 
    fam, group = s.split(' ')[3], s.split(' ')[5]
    temp = dictor()
    for i, j in temp.items(): 
        if fam in j[0]: temp[i] = [j[0], j[1], group]
    return reversed(['Словарь:', *[f'{k[0]}:{" ".join(k[1])}' for k in temp.items()]])


def delete_student(s): 
    num, temp = s.split(' ')[-1], dictor()
    del temp[num]
    return reversed(['Словарь:', *[f'{k[0]}:{" ".join(k[1])}' for k in temp.items()]])
    
def decrease_age(s): 
    temp = dictor()
    for i, j in temp.items():
        if int(j[1]) > 22: temp[i] = [j[0], str(int(j[1]) - 1), j[2]]
    return reversed(['Словарь:', *[f'{k[0]}:{" ".join(k[1])}' for k in temp.items()]])

def delete_student_age(s):
    temp = dictor()
    t = temp.copy()
    for i, j in t.items():
        if int(j[1]) == 23: del temp[i]
    return reversed(['Словарь:', *[f'{k[0]}:{" ".join(k[1])}' for k in temp.items()]])

def increase_age_ivanov(s): 
    fam = 'Иванов'
    temp = dictor()
    for i, j in temp.items(): 
        if fam in j[0]: temp[i] = [j[0], str(int(j[1]) + 1), j[2]]
    return reversed(['Словарь:', *[f'{k[0]}:{" ".join(k[1])}' for k in temp.items()]])

def change_ivanov(s): 
    fam = 'Иванов'
    temp = dictor()
    for i, j in temp.items(): 
        if fam in j[0]: temp[i] = ['Сидоров ' + ' '.join(j[0].split(' ')[1::]), j[1], j[2]]
    return reversed(['Словарь:', *[f'{k[0]}:{" ".join(k[1])}' for k in temp.items()]])

def swap_groups(s): 
    temp = dictor()
    for i, j in temp.items():
        temp[i] = [j[2], j[1], j[0]]
    return reversed(['Словарь:', *[f'{k[0]}:{" ".join(k[1])}' for k in temp.items()]])


def second(mas):
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


def print_group(s): 
    group = 'БО-111111'
    temp = dictor()
    return reversed(['Словарь:', *[f'{k[0]}:{" ".join(k[1])}' for k in temp.items() if group in k[1][2]]])

def print_numbers(s): 
    temp = dictor()
    return reversed(['Словарь:', *[f'{k[0]}:{" ".join(k[1])}' for k in temp.items() if 1 <= int(k[0]) <= 2]])

def print_age(s): 
    temp = dictor()
    return reversed(['Словарь:', *[f'{k[0]}:{" ".join(k[1])}' for k in temp.items() if int(k[1][1]) == 22]])

def print_surname(s): 
    temp = dictor()
    return reversed(['Словарь:', *[f'{k[0]}:{" ".join(k[1])}' for k in temp.items() if 'Иванов' in k[1][0]]])

def print_surname_a(s): 
    temp = dictor()
    return reversed(['Словарь:', *[f'{k[0]}:{" ".join(k[1])}' for k in temp.items() if k[1][0].split(' ')[0][-1] == 'а']])

def print_age_even(s): 
    temp = dictor()
    return reversed(['Словарь:', *[f'{k[0]}:{" ".join(k[1])}' for k in temp.items() if int(k[1][1]) % 2 == 0]])

def print_age_five(s): 
    temp = dictor()
    return reversed(['Словарь:', *[f'{k[0]}:{" ".join(k[1])}' for k in temp.items() if '5' in k[1][1]]])

def print_len_group(s): 
    temp = dictor()
    return reversed(['Словарь:', *[f'{k[0]}:{" ".join(k[1])}' for k in temp.items() if len(k[1][2]) > 7]])

def print_even_num(s): 
    temp = dictor()
    return reversed(['Словарь:', *[f'{k[0]}:{" ".join(k[1])}' for k in temp.items() if int(k[0]) % 2 == 0]])

def print_group_one(s):
    temp = dictor()
    return reversed(['Словарь:', *[f'{k[0]}:{" ".join(k[1])}' for k in temp.items() if k[1][2][-1] == '1']])


def third(mas):
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
        if re.fullmatch(string, mas): return function(mas)
    return False


def main(n, *, mas):
    if n == '1': return first()
    if n == '2': return second(mas)
    if n == '3': return third(mas)
    else: return False


if __name__ == '__main__':
    main()