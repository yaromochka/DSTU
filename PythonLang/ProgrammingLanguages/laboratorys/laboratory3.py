"""
1. Пусть дана строка, состоящая из слов, пробелов и знаков препинания. На
основании этой строки создайте новую (и выведите ее на консоль):
Вариант 4. Содержащую только слова, в которых две последние
буквы — «ов».
"""


def first(mas: str) -> list[str]:
    return [i.rstrip('.,/&^%*$)#!?@)(*""') for i in mas.split(' ')
            if i.rstrip('.,/&^%*$)#!?@)(*""')[-2::].lower() == 'ов']


"""
2. Пусть дана строковая переменная, содержащая информацию о студентах:
my_string = «Ф;И;О;Возраст;Категория;_Иванов;Иван;Иванович;23
года;Студент 3 курса;_Петров;Семен;Игоревич;22 года;Студент 2 курса».
Вариант 4. Выведите информацию в виде:
ФИО О студенте
Иванов Иван Иванович Студент 3 курса, 23 года
Петров Семен Игоревич Студент 2 курса, 22 года
"""


def second() -> list[str]:
    info = 'Иванов;Иван;Иванович;23 года;Студент 3 курса;_Петров;Семен;Игоревич;22 года;Студент 2 курса'.split(';_')
    ans = ['ФИО                     О студенте']
    for i in info:
        i = i.split(';')
        ans.append((' '.join(i[0:2]) + '                      ' + ' '.join(i[2::])))
    return reversed(ans)


"""
3. Пусть дана строковая переменная, содержащая информацию о студентах
вида: my_string = «ФИО;Возраст;Категория;_Иванов Иван Иванович;23
года;Студент 3 курса;_Петров Семен Игоревич;22 года;Студент 2
курса;_Иванов Семен Игоревич;22 года;Студент 2 курса;_Акибов Ярослав
Наумович;23 года;Студент 3 курса;_Борков Станислав Максимович;21
год;Студент 1 курса;_Петров Семен Семенович;21 год;Студент 1
курса;_Романов Станислав Андреевич;23 года;Студент 3 курса;_Петров
Всеволод Борисович;21 год;Студент 2 курса».
Вариант 4. Выведите построчно информацию о студентах, чьи
фамилии начинаются на букву «А» или «Б»
"""


def third() -> list[str]:
    info = ('Иванов Иван Иванович;23 года;Студент 3 курса;_Петров Семен Игоревич;22 года;Студент 2 курса;_Иванов Семен '
            'Игоревич;22 года;Студент 2 курса;_Акибов Ярослав Наумович;23 года;Студент 3 курса;_Борков Станислав '
            'Максимович;21 год;Студент 1 курса;_Петров Семен Семенович;21 год;Студент 1 курса;_Романов Станислав '
            'Андреевич;23 года;Студент 3 курса;_Петров Всеволод Борисович;21 год;Студент 2 курса').split(';_')
    return [i for i in info if i[0][0] == 'А' or i[0][0] == 'Б']


"""
Пусть дана строка произвольной длины. Выведите информацию о том,
сколько в ней символов и сколько слов.
"""


def fourthy(mas: str) -> tuple[str, str]:
    return f"Количество символов в строке - {len(mas.replace(' ', ''))}", f"Количество слов в строке - {len([i.rstrip('.,/&^%*$)#!?@)(*&') for i in mas.split()])}"


def main(n: int, *, mas: str) -> bool | list[str] | tuple[str, str]:
    if n == '1' and first(mas) is not False: return [f'Слова, в которых последние две буквы "ОВ" {first(mas)}']
    if n == '2' and second() is not False: return second()
    if n == '3' and third() is not False: return [f'Студент с фамилией на "А" или "Б" - {third()}']
    if n == '4' and fourthy(mas) is not False:
        return fourthy(mas)
    else:
        return False


if __name__ == '__main__':
    main()
