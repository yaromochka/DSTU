import sqlite3 
import re
import csv


def create_db():
    connection = sqlite3.connect('new_db.db')
    cursor = connection.cursor()

    cursor.execute(''' CREATE TABLE IF NOT EXISTS discipline
                   (id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   id_day INTEGER,
                   id_lesson INTEGER);
                   ''')

    cursor.execute(''' CREATE TABLE IF NOT EXISTS day
                   (id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL);
                   ''')

    cursor.execute(''' CREATE TABLE IF NOT EXISTS lesson
                   (id INTEGER PRIMARY KEY,
                   num INTEGER,
                   start_time TIME,
                   end_time TIME);
                   ''')
    
    connection.commit()
    connection.close()


def first():
    connection = sqlite3.connect('new_db.db')
    cursor = connection.cursor()
    
    cursor.execute(""" 
    SELECT * FROM discipline
    """)

    disciplines = cursor.fetchall()

    cursor.execute(""" 
    SELECT * FROM day
    """)

    days = cursor.fetchall()

    cursor.execute(""" 
    SELECT * FROM lesson
    """)

    lessons = cursor.fetchall()
    connection.close()
    return reversed([f'Таблица lessons: ', *[' '.join([str(j) for j in i]) for i in lessons], f'Таблица days: ', *[' '.join([str(j) for j in i]) for i in days], f'Таблица disciplines: ', *[' '.join([str(j) for j in i]) for i in disciplines]])


def add_item(s):
    connection = sqlite3.connect('new_db.db')
    cursor = connection.cursor()
    cursor.execute(""" 
    SELECT * FROM day
    """)
    days = {}
    temp = cursor.fetchall()
    for i in temp: days[i[1]] = i[0]
    name, day, num = s.split(' ')[1], s.split(' ')[3], s.split(' ')[4]
    insert_data = """ 
    INSERT INTO discipline
    (name, id_day, id_number)
    VALUES 
    (?, ?, ?); """
    data_tuple = (name, days[day], num)
    cursor.execute(insert_data, data_tuple)
    connection.commit()
    connection.close()
    return ['Запись успешно добавлена']


def modify_item(s):
    connection = sqlite3.connect('new_db.db')
    cursor = connection.cursor()
    cursor.execute(""" 
    SELECT * FROM day
    """)
    days = {}
    temp = cursor.fetchall()
    for i in temp: days[i[1]] = i[0]
    day, num, new_name = s.split(' ')[2], s.split(' ')[3], s.split(' ')[6]
    insert_data = """ 
    UPDATE discipline
    SET name = ?
    WHERE id_day = ? AND id_number = ?
    """
    data_tuple = (new_name, days[day], num)
    cursor.execute(insert_data, data_tuple)
    connection.commit()
    connection.close()
    return ['Запись успешно изменена']


def del_item(s):
    connection = sqlite3.connect('new_db.db')
    cursor = connection.cursor()
    cursor.execute(""" 
    SELECT * FROM day
    """)
    days = {}
    temp = cursor.fetchall()
    for i in temp: days[i[1]] = i[0]
    day, num = s.split(' ')[3], s.split(' ')[4]
    insert_data = """ 
    DELETE FROM discipline
    WHERE id_day = ? AND id_number = ?
    """
    data_tuple = (days[day], num)
    cursor.execute(insert_data, data_tuple)
    connection.commit()
    connection.close()
    return ['Запись успешно удалена']

def second(mas):
    commands = {
            r'Добавить \w+ в \w+? \d+ парой': add_item,
            r'Изменить значение \w+? \d+ пара на \w+': modify_item,
            r'Удалить значения в \w+? \d+ парой': del_item
                }
    

    for string, function in commands.items():
        if re.fullmatch(string, mas): return function(mas)
    return False



def third():
    connection = sqlite3.connect('new_db.db')
    cursor = connection.cursor()
    cursor.execute(""" 
        SELECT discipline.name, day.name, lesson.num 
        FROM discipline 
        CROSS JOIN day ON day.id = discipline.id_day
        CROSS JOIN lesson ON lesson.id = discipline.id_number
        ORDER BY discipline.name ASC
    """)
    data = cursor.fetchall()
    connection.close()
    return reversed(['Название дисциплины, день недели, номер пары', *[' '.join([str(j) for j in i]) for i in data]])


def fourth():
    connection = sqlite3.connect('new_db.db')
    cursor = connection.cursor()
    cursor.execute(""" 
        SELECT day.name as "День недели", COUNT(discipline.id_number) as "Количество пар"
        FROM discipline
        JOIN day ON day.id = id_day
        GROUP BY day.id
    """)
    data = cursor.fetchall()
    connection.close()
    return reversed(['День недели, количество пар', *[' '.join([str(j) for j in i]) for i in data]])


def fifth(mas):
    if re.fullmatch(r"(Записать|Вписать)\s?(данные|информацию)?", mas):
        connection = sqlite3.connect('new_db.db')
        cursor = connection.cursor()
        cursor.execute(""" 
            SELECT discipline.name, day.name, lesson.num, lesson.start_time, lesson.end_time
            FROM discipline
            JOIN day ON day.id = id_day
            JOIN lesson ON lesson.id = id_number
            ORDER BY day.id ASC, lesson.num ASC
        """)
        data = cursor.fetchall()
        with open('db_to_csv.csv', 'w') as f:
            wr = csv.writer(f)
            for row in data: wr.writerow(row)
        connection.close()
        return ['Данные успешно записаны']


    if re.fullmatch(r"(Считать|Прочитать)\s?(данные|информацию)?", mas):
        connection = sqlite3.connect('new_db.db')
        cursor = connection.cursor()  
        cursor.execute(""" CREATE TABLE IF NOT EXISTS new_table 
                   (id INTEGER PRIMARY KEY,
                    discipline_name TEXT NOT NULL,
                    day_name TEXT NOT NULL,
                    lesson_num TEXT NOT NULL,
                    lesson_start_time TIME,
                    lesson_end_time TIME);
                       """)      
        with open('db_to_csv.csv', 'r') as f:
            rd = csv.reader(f)
            for row in rd:
                rd = list(rd)
                for j, i in enumerate(rd):
                    if len(i) > 0:
                        insert_param = """ 
                        INSERT INTO new_table
                        VALUES 
                        (?, ?, ?, ?, ?, ?);
                    """
                        discipline_name, day_name, lesson_num, lesson_start_time, lesson_end_time = i
                        data_tuple = (j, discipline_name, day_name, lesson_num, lesson_start_time, lesson_end_time)
                        cursor.execute(insert_param, data_tuple)
                        connection.commit()
        connection.close()
        return ['Данные успешно считаны']


def main(n, *, mas):
    create_db()
    if n == '1': return first()
    if n == '2': return second(mas)
    if n == '3': return third()
    if n == '4': return fourth()
    if n == '5': return fifth(mas)
    else: return False



if __name__ == '__main__':
    main()