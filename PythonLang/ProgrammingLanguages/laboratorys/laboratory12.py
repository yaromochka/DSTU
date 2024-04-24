import sqlite3


# Создание таблиц в БД (если они не существуют)
def create_db():
    connection = sqlite3.connect('../files/new_db12.db')
    cursor = connection.cursor()

    cursor.execute(''' CREATE TABLE IF NOT EXISTS child
                   (id INTEGER PRIMARY KEY,
                   full_name TEXT NOT NULL,
                   full_name_father TEXT,
                   full_name_mother TEXT,
                   age INTEGER,
                   id_certificate INTEGER,
                   id_doctor INTEGER);
                   ''')

    cursor.execute(''' CREATE TABLE IF NOT EXISTS certificate
                   (id INTEGER PRIMARY KEY,
                   number_certificate TEXT NOT NULL);
                   ''')

    cursor.execute(''' CREATE TABLE IF NOT EXISTS doctors
                   (id INTEGER PRIMARY KEY,
                   full_name TEXT NOT NULL,
                   age INTEGER);
                   ''')
    
    connection.commit()
    connection.close()


"""
1. Пусть дана база данных (приведена ниже). Используйте нужные
структуры данных для ее хранения. Заполните БД. Выведите список детей
в возрасте до 10 лет.
"""


def first() -> list[str]:
    connection = sqlite3.connect('../files/new_db12.db')
    cursor = connection.cursor()
    cursor.execute(""" 
        SELECT child.full_name, child.age FROM child
        WHERE child.age < 10
    """)
    data = cursor.fetchall()
    connection.close()
    return reversed(['Список детей до 10ти лет', *[', '.join([str(j) for j in i]) for i in data]])


"""
2. Для БД из задания 1 выведите информацию о детях, чьи родители имеют
разные фамилии. 
"""


def second() -> list[str]:
    connection = sqlite3.connect('../files/new_db12.db')
    cursor = connection.cursor()
    cursor.execute(""" 
        SELECT * FROM child
    """)
    data = cursor.fetchall()
    connection.close()
    answer = []
    for i in data:
        if (i[2].split(' '))[0] not in (i[3].split(' '))[0] and (i[3].split(' '))[0] != '' and (i[2].split(' '))[0] != '': answer.append(i)
    return reversed(['Информация о детях, чьи родители имеют разные фамилии', *[', '.join([str(j) for j in i]) for i in answer]])


"""
3. Для БД из задания 1 выведите список врачей в возрасте от 20 до 60 лет.
"""


def third() -> list[str]:
    connection = sqlite3.connect('../files/new_db12.db')
    cursor = connection.cursor()
    cursor.execute(""" 
        SELECT doctors.full_name, doctors.age FROM doctors
        WHERE doctors.age > 20 and doctors.age < 60
    """)
    data = cursor.fetchall()
    connection.close()
    return reversed(['Список врачей в возрасте от 20 до 60 лет', *[', '.join([str(j) for j in i]) for i in data]])


def main(n: int, *, mas: str) -> bool | list[str]:
    create_db()
    if n == '1': return first()
    if n == '2': return second()
    if n == '3': return third()
    else: return False


if __name__ == '__main__':
    main()