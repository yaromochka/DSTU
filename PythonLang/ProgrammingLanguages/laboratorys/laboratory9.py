from csv import reader
from typing import Any


# Считывание данных из файла
def dictor() -> dict[Any, Any]:
    with open(r"/PythonLang/ProgrammingLanguages/files/student.csv", encoding='utf-16') as f:
        file, temp = list(reader(f)), {}
        for i in file[1::]:
            i = (''.join(i)).split(';')
            temp[i[0]] = i[1::]
    return temp


"""
1. Пусть список студентов представлен в виде структуры {№: [ФИО, Возраст,
Группа], №: [....], №: [....]}. Реализуйте функционал по добавлению нового
студента (данные вводятся через консоль)
"""


def first(mas: str) -> list[str]:
    temp = dictor()
    mas = mas.split(', ')
    if mas[0] in list(temp.keys()):
        mas[0] = str(int(list(temp.keys())[-1]) + 1)
    temp[mas[0]] = mas[1::]
    return reversed([f'{k[0]}:{" ".join([str(i) for i in k[1]])}' for k in temp.items()])
    # else: return ['Человек с таким номером уже есть в таблице!']


"""
2. Пусть список студентов представлен в виде структуры {№: [ФИО, Возраст,
Группа], №: [....], №: [....]}. Реализуйте функционал по изменению всех
данных о студенте (поиск по «№»).
"""


def second(mas: str) -> list[str]:
    temp = dictor()
    mas = mas.split(', ')
    if mas[0] in list(temp.keys()):
        temp[mas[0]] = mas[1::]
        return reversed(['Данные успешно изменены!', *[f'{k[0]}:{" ".join([str(i) for i in k[1]])}' for k in temp.items()]])
    else: return ['Человека с таким номером нет в таблице']


"""
3. Пусть список студентов представлен в виде структуры {№: [ФИО, Возраст,
Группа], №: [....], №: [....]}. Реализуйте функционал по удалению данных о
студенте (поиск по «№»).
"""


def third(mas: str) -> bool | list[str]:
    temp = dictor()
    if all([i in '0123456789' for i in mas]) and mas in list(temp.keys()):
        del temp[str(mas)]
        return reversed(['Данные успешно удалены!', *[f'{k[0]}:{" ".join([str(i) for i in k[1]])}' for k in temp.items()]])
    else: return False


"""
4. Пусть список студентов представлен в виде структуры {№: [ФИО, Возраст,
Группа], №: [....], №: [....]}. Выведите информацию о студенте с
конкретным «№» («№» задается через консоль).
"""


def fourthy(mas: str) -> bool | list[str]:
    temp = dictor()
    if all([i in '0123456789' for i in mas]) and mas in list(temp.keys()):
        return reversed([f'Информация о студенте №{mas}', f'{mas}: {temp[mas]}'])
    else: return False


def main(n: int, *, mas: str) -> bool | list[str]:
    if n == '1' and first(mas) is not False: return first(mas)
    if n == '2' and second(mas) is not False: return second(mas)
    if n == '3' and third(mas) is not False: return third(mas)
    if n == '4' and fourthy(mas) is not False: return fourthy(mas)
    else: return False


if __name__ == '__main__':
    main()