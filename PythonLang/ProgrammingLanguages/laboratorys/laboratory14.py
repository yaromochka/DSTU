from typing import Any

import mimesis
from mimesis.builtins import RussiaSpecProvider
from random import randint
import re


"""
 1.	Создать класс Student, содержащий поля: фамилия и инициалы, номер группы, успеваемость (массив из пяти элементов).
Создать массив из десяти элементов такого типа, упорядочить записи по возрастанию среднего балла.
Добавить возможность вывода фамилий и номеров групп студентов, имеющих оценки, равные только 4 или 5.
"""

""" КЛАСС СТУДЕНТОВ """


class Student:
    def characters(self, fullname: str, group: str, progress: list):
        self.fullname = fullname
        self.group = group
        self.progress = progress
        return self.fullname, self.group, self.progress


"""
2.	Создать класс с именем Train, содержащий поля: название пункта назначения, номер поезда, время отправления. 
Ввести данные в массив из пяти элементов типа train, упорядочить элементы по номерам поездов. 
Добавить возможность вывода информации о поезде, номер которого введен пользователем.
Добавить возможность сортировки массива по пункту назначения, причем поезда с одинаковыми пунктами назначения должны быть
упорядочены по времени отправления.
"""

""" КЛАСС ПОЕЗДОВ"""


class Train:
    def characters(self, arrival, number, time):
        self.arrival = arrival
        self.number = number
        self.time = time
        return self.arrival, self.number, self.time


"""
3.	Создать класс с двумя переменными.
Добавить функцию вывода на экран и функцию изменения этих переменных. 
Добавить функцию, которая находит сумму значений этих переменных, и функцию которая находит наибольшее значение из этих
двух переменных.
"""

""" ДВА ЧИСЛА"""


class Numbers:
    global x, y
    x = randint(1, 10000)
    y = randint(1, 10000)

    def __init__(self):
        super().__init__()
        self.x = x
        self.y = y

    def modify(self, new_value_x, new_value_y):
        global x, y
        x = new_value_x
        y = new_value_y
        self.x = x
        self.y = y
        return self

    def info_print(self): return [str(self.x), str(self.y)]

    def maximum(self): return [max(self.x, self.y)]

    def add(self): return [self.x + self.y]


"""
4.	Класс «Домашняя библиотека». Предусмотреть возможность работы с произвольным числом книг,
поиска книги по какому-либо признаку (например, по автору или по году издания),
добавления книг в библиотеку, удаления книг из нее, сортировки книг по разным полям.
"""


""" БИБЛИОТЕКА """


class Library:
    def __init__(self, books=None):
        self.books = [] if books is None else books

    def info(self):
        for i in self.books:
            print(i)

    def add(self, book):
        self.books.append(book)
        return [', '.join(list([str(j) for j in i])) for i in self.books]

    def remove(self, book):
        for index, item in enumerate(self.books):
            if item[1] == book[1]:
                self.books.pop(index)
        return [', '.join(list([str(j) for j in i])) for i in self.books]

    def find_author(self, author):
        for book in self.books:
            if book[0] == author:
                return [', '.join([str(j) for j in book])]

    def find_age(self, age):
        for book in self.books:
            if str(book[2]) == age:
                return [', '.join([str(j) for j in book])]

    def find_title(self, title):
        for book in self.books:
            if book[1] == title:
                return [', '.join([str(j) for j in book])]

    def sort_author(self):
        return [', '.join(list([str(j) for j in i])) for i in sorted(self.books, key=lambda x: x[0], reverse=True)]

    def sort_age(self):
        return [', '.join(list([str(j) for j in i])) for i in sorted(self.books, key=lambda x: x[2], reverse=True)]

    def sort_title(self):
        return [', '.join(list([str(j) for j in i])) for i in sorted(self.books, key=lambda x: x[1], reverse=True)]


""" КЛАСС КНИГ """


class Book:
    def __init__(self, title, author, age):
        self.title = title
        self.author = author
        self.age = age

    def info(self):
        return self.title, self.author, self.age


"""
5.	Класс Покупатель: Фамилия, Имя, Отчество, Адрес, Номер кредитной карточки, Номер банковского счета; 
Методы: установка значений атрибутов, получение значений атрибутов, вывод информации. 
Создать массив объектов данного класса. Вывести список покупателей в алфавитном порядке и список покупателей, 
у которых номер кредитной карточки находится в заданном диапазоне.
"""


""" КЛАСС ПОКУПАТЕЛЕЙ"""


class Customer:
    def __init__(self, surname, name, middlename, address, credit_num, bank_num):
        self.surname = surname
        self.name = name
        self.middlename = middlename
        self.address = address
        self.credit_num = credit_num
        self.bank_num = bank_num

    def info(self):
        return self.surname, self.name, self.middlename, self.address, self.credit_num, self.bank_num


"""
6.	Класс Абонент: Идентификационный номер, Фамилия, Имя, Отчество, Адрес, Номер кредитной карточки, 
Дебет, Кредит, Время междугородных и городских переговоров; Конструктор; 
Методы: установка значений атрибутов, получение значений атрибутов, вывод информации. 
Создать массив объектов данного класса. Вывести сведения относительно абонентов, 
у которых время городских переговоров превышает заданное.  Сведения относительно абонентов, 
которые пользовались междугородной связью. Список абонентов в алфавитном порядке.
"""


""" КЛАСС АБОНЕНТОВ"""


class Abonent:
    def __init__(self, ID, surname, name, middlename, address, credit_num, time_out_city, time_in_city):
        self.surname = surname
        self.ID = ID
        self.name = name
        self.middlename = middlename
        self.address = address
        self.credit_num = credit_num
        self.time_out_city = time_out_city
        self.time_in_city = time_in_city

    def info(self):
        return (self.ID, self.surname, self.name, self.middlename, self.address, self.credit_num, self.time_out_city,
                self.time_in_city)


""" ФУНКЦИИ ДЛЯ ПЕРВОГО ЗАДАНИЯ """


def average(studs: str) -> sorted[str]:
    return sorted(studs, key=lambda x: sum(x[2]) / len(x[2]), reverse=True)


def only_4_5(studs: str) -> list[str]:
    return [i for i in studs if all(j in [4, 5] for j in i[2])]


""" ПЕРВОЕ ЗАДАНИЕ """


def first(mas: str) -> bool:
    students = []
    string = 'АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЭЮЯ'
    for _ in range(10):
        temp = Student()
        person = mimesis.Person('ru')
        students.append(temp.characters(
            person.surname() + ' ' + string[randint(0, len(string) - 1)] + '.' + string[randint(0, len(string) - 1)],
            'ВКБ22', [randint(3, 5) for i in range(5)]))

    commands = {
        r'Упорядочить по среднему баллу': average,
        r'Вывести только 4 и 5': only_4_5
    }
    answer = False
    for string, value in commands.items():
        if re.fullmatch(mas, string):
            answer = []
            temp = list(value(students))
            for i in temp:
                ans = ''
                for j in i:
                    ans = ans + str(j) + ', '
                answer.append(ans)
    return answer


""" ФУНКЦИИ ДЛЯ ВТОРОГО ЗАДАНИЯ """


def num_train(trns: list) -> reversed[str]:
    answer = []
    temp = list(sorted(trns, key=lambda x: x[1]))
    for i in temp:
        ans = ''
        for j in i:
            ans = ans + str(j) + ', '
        answer.append(ans)
    return reversed([f'Информация о всех поездах', *answer])


def num_info(trns: list, mas: str) -> reversed[str]:
    number = mas.split(' ')[4]
    for i in trns:
        if i[1] == int(number):
            return reversed([f'Информация о поезде номер {number}', ', '.join([str(j) for j in i])])
    return [f'Поезда с номером {number} нет в списке']


def sort_arrive(trns: list) -> reversed[str]:
    answer = []
    temp = list(sorted(trns, key=lambda x: (x[0], x[2])))
    for i in temp:
        ans = ''
        for j in i:
            ans = ans + str(j) + ', '
        answer.append(ans)
    return reversed([f'Отсортированная информация о поездах', *answer])


""" ВТОРОЕ ЗАДАНИЕ """


def second(mas: str) -> reversed[str]:
    trains = []
    for _ in range(5):
        temp = Train()
        trains.append(temp.characters(mimesis.Address(locale=mimesis.Locale.RU).city(), randint(1, 10),
                                      str(mimesis.Datetime().time().hour).zfill(2) + ':' + str(
                                          mimesis.Datetime().time().minute).zfill(2)))

    commands = {
        r'Упорядочить по номеру поезда': num_train,
        r'Информация о поезде номер \d+': num_info,
        r'Отсортировать по пункту назначения': sort_arrive
    }
    for string, value in commands.items():
        if re.fullmatch(string, mas): return value(trains, mas)


""" ТРЕТЬЕ ЗАДАНИЕ """


def third(mas: str) -> list[str]:
    nums = Numbers()
    commands = {
        r'Найти сумму чисел': nums.add,
        r'Найти наибольшее число': nums.maximum,
        r'Вывести числа': nums.info_print
    }
    for string, value in commands.items():
        if re.fullmatch(string, mas):
            return [', '.join(list(str(i) for i in value()))]
        elif re.fullmatch(r"Поменять числа на \d+ и \d+", mas):
            nums.modify(int(mas.split(' ')[3]), int(mas.split(' ')[5]))
            return nums.info_print()


""" ЧЕТВЁРТОЕ ЗАДАНИЕ """


def fourth(mas: str) -> list[str]:
    books = Library()
    temp = Book('Джордж Оруэлл', 'Да здравствует фикус', 1936)
    books.add(temp.info())
    for _ in range(10):
        text = mimesis.Text('ru')
        person = mimesis.Person('ru')
        temp = Book(person.full_name(), ' '.join(text.words(quantity=randint(1, 3))), randint(1800, 2023))
        books.add(temp.info())

    commands = {
        r"Отсортировать книги по годам": books.sort_age,
        r"Отсортировать книги по авторам": books.sort_author,
        r"Отсортировать книги по названиям": books.sort_title
    }

    if re.fullmatch(r'Добавить книгу ([\d\-\.A-Яа-яA-Za-z\s]+)', mas):
        book_temp = mas.split(' ')[2:]
        book_author, book_age, book_title = ' '.join(book_temp[0:2]), book_temp[-1], ' '.join(book_temp[2:-1])
        return books.add(Book(book_author, book_title, book_age).info())
    elif re.fullmatch(r'Удалить книгу ([\d\-\.A-Яа-яA-Za-z\s]+)', mas):
        book_temp = mas.split(' ')[2:]
        book_author, book_age, book_title = ' '.join(book_temp[0:2]), book_temp[-1], ' '.join(book_temp[2:-1])
        return books.remove(Book(book_author, book_title, book_age).info())
    elif re.fullmatch(r'Найти книгу по автору ([\d\-\.A-Яа-яA-Za-z\s]+)', mas):
        return books.find_author(' '.join(mas.split(' ')[4:]))
    elif re.fullmatch(r'Найти книгу по названию ([\d\-\.A-Яа-яA-Za-z\s]+)', mas):
        return books.find_title(' '.join([str(i) for i in mas.split(' ')[4:]]))
    elif re.fullmatch(r'Найти книгу по году (\d+)', mas):
        return books.find_age(' '.join(mas.split(' ')[4:]))
    else:
        for string, value in commands.items():
            if re.fullmatch(string, mas): return value()


""" ФУНКЦИИ ДЛЯ ПЯТОГО ЗАДАНИЯ"""


def customer_sort(cust: list) -> list[str]:
    return [', '.join(list([str(j) for j in i])) for i in sorted(cust, key=lambda x: x[0], reverse=True)]


def customer_credit(cust: list, mas: str) -> list[str]:
    num1, num2 = int(mas.split(' ')[-3]), int(mas.split(' ')[-1])
    ans = []
    for i in cust:
        if num1 <= i[4] <= num2: ans.append(i)
    return [', '.join(list([str(j) for j in i])) for i in ans]


def fifth(mas: str) -> list[str]:
    customers = []
    for _ in range(10):
        person = mimesis.Person('ru')
        ru = RussiaSpecProvider()
        temp = Customer(person.surname(), person.name(),
                        ru.patronymic(gender=(mimesis.Gender.MALE, mimesis.Gender.FEMALE)[randint(0, 1)]), \
                        mimesis.Address('ru').address(), randint(1000000, 9999999), randint(100000000, 999999999))
        customers.append(temp.info())

    commands = {
        r'Вывести покупателей в алфавитном порядке': customer_sort,
        r'Вывести покупателей с кредиткой от \d+ до \d+': customer_credit,
    }
    for string, value in commands.items():
        if re.fullmatch(string, mas): return value(customers, mas)


""" ФУНКЦИИ ДЛЯ ШЕСТОГО ЗАДАНИЯ"""


def abonent_over(abon: list, mas: str) -> list[str]:
    t = int(mas.split(' ')[-1])
    ans = []
    for i in abon:
        if i[-1] > t: ans.append(i)
    return [', '.join(list([str(j) for j in i])) for i in ans]


def abonent_inter_city(abon: list) -> list[str]:
    ans = []
    for i in abon:
        if i[-2] > 0:
            ans.append(i)
    return [', '.join(list([str(j) for j in i])) for i in ans]


def abonent_sort(abon: list) -> list[str]:
    return [', '.join(list([str(j) for j in i])) for i in sorted(abon, key=lambda x: x[1], reverse=True)]


""" ШЕСТОЕ ЗАДАНИЕ """


def sixth(mas: str) -> list[str]:
    abonents = []
    for _ in range(10):
        person = mimesis.Person('ru')
        ru = RussiaSpecProvider()
        temp = Abonent(randint(1, 1000), person.surname(), person.name(),
                       ru.patronymic(gender=(mimesis.Gender.MALE, mimesis.Gender.FEMALE)[randint(0, 1)]), \
                       mimesis.Address('ru').address(), randint(1000000, 9999999), randint(0, 200), randint(0, 500))
        abonents.append(temp.info())

    commands = {
        r'Вывести у которых превышает \d+': abonent_over,
        r'Вывести которые пользовались межгородом': abonent_inter_city,
        r'Вывести список в алфавитном порядке': abonent_sort
    }
    for string, value in commands.items():
        if re.fullmatch(string, mas): return value(abonents, mas)


def main(n: int, *, mas: str) -> bool | reversed[str | Any] | reversed[str] | list[str]:
    if n == '1': return first(mas)
    if n == '2': return second(mas)
    if n == '3': return third(mas)
    if n == '4': return fourth(mas)
    if n == '5': return fifth(mas)
    if n == '6':
        return sixth(mas)
    else:
        return False


if __name__ == '__main__':
    main()
