from random import randint


def first(mas):
    if mas.isdigit(): 
        matrix = [[randint(-100000, 100000) for _ in range(int(mas))] for _ in range(int(mas))]
        return reversed(('Изначальная матрица: ', *[' '.join(str(j) for j in i) for i in matrix], f'Сумма элементов - {str(sum([sum(row) for row in matrix]))}'))
    else: return ['Неверно введён размер матрицы']


def second():
    matrix = [randint(-100000, 100000) for _ in range(10)]
    matrix2 = matrix
    for _ in range(5):
        matrix2.append(randint(-100000, 100000))
    return (f'Изначальный рандомный список - {matrix}', f'Список с новыми элементами - {matrix2}', f'Список только нечётных элементов - {[matrix2[i] for i in range(len(matrix2)) if i % 2 == 0]}')


def third():
    my_len = [['БО-331101', ['Акулова Алёна', 'Бабушкина Ксения', 'Алёнова Акула']],
              ['БОВ-421102', ['Алкулова Кулёна', 'Ксеньева Бабушка', 'Не Придумал']],
              ['БО-331103', ['Ковалев Данил', 'Ковалев Данила', 'Ковалев Даня']],
              ['ААА-1151', ['Иван', 'Ваня', 'Кирюха о Кирилл привет ты что здесь делаешь']],
              ['Я РАБОТАЮ ЗА ЕДУ', ['Никто не учится в этой группе']]
             ]

    ans = []
    for lst in my_len:
        if lst[0][:2] == 'БО':
            ans.append(f'{lst[0]}: {lst[1]}')
    return reversed((f'Список студентов, название группы которых начинается на "БО"', *ans))


def fourthy():
    my_len = [['БО-331101', ['Акулова Алёна', 'Бабушкина Ксения', 'Алёнова Акула']],
              ['БОВ-421102', ['Алкулова Кулёна', 'Ксеньева Бабушка', 'Не Придумал']],
              ['БО-331103', ['Ковалев Данил', 'Ковалев Данила', 'Ковалев Даня']],
              ['ААА-1151', ['Иван', 'Ваня', 'Кирюха о Кирилл привет ты что здесь делаешь']],
              ['Я РАБОТАЮ ЗА ЕДУ', ['Никто не учится в этой группе']]
             ]
    ans = []
    for lst in my_len:
        for num, name in enumerate(lst[1]):
            if (num + 1) % 2 == 0:
                ans.append((f'{(name)} {lst[0]}'))
    return reversed(('Студенты, чей порядковый номер - чётное число:', *ans))


def main(n, *, mas):
    if n == '1' and first(mas) is not False: return first(mas)
    if n == '2' and second() is not False: return second()
    if n == '3' and third() is not False: return third()
    if n == '4' and fourthy() is not False: return fourthy()
    else: return False


if __name__ == '__main__':
    main()
