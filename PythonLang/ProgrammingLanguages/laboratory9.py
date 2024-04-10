from csv import reader


def dictor():
    with open(r"/Users/yaromochka/IdeaProjects/DSTU/PythonLang/ProgrammingLanguages/files/student.csv", encoding='utf-16') as f:
        file, temp = list(reader(f)), {}
        for i in file[1::]:
            i = (''.join(i)).split(';')
            temp[i[0]] = i[1::]
    return temp


def first(mas):
    temp = dictor()
    mas = mas.split(', ')
    if mas[0] in list(temp.keys()):
        mas[0] = str(int(list(temp.keys())[-1]) + 1)
    temp[mas[0]] = mas[1::]
    return reversed([f'{k[0]}:{" ".join([str(i) for i in k[1]])}' for k in temp.items()])
    # else: return ['Человек с таким номером уже есть в таблице!']



def second(mas):
    temp = dictor()
    mas = mas.split(', ')
    if mas[0] in list(temp.keys()):
        temp[mas[0]] = mas[1::]
        return reversed(['Данные успешно изменены!', *[f'{k[0]}:{" ".join([str(i) for i in k[1]])}' for k in temp.items()]])
    else: return ['Человека с таким номером нет в таблице']


def third(mas):
    temp = dictor()
    if all([i in '0123456789' for i in mas]) and mas in list(temp.keys()):
        del temp[str(mas)]
        return reversed(['Данные успешно удалены!', *[f'{k[0]}:{" ".join([str(i) for i in k[1]])}' for k in temp.items()]])
    else: return False


def fourthy(mas):
    temp = dictor()
    if all([i in '0123456789' for i in mas]) and mas in list(temp.keys()):
        return reversed([f'Информация о студенте №{mas}', f'{mas}: {temp[mas]}'])
    else: return False


def main(n, *, mas):
    if n == '1' and first(mas) is not False: return first(mas)
    if n == '2' and second(mas) is not False: return second(mas)
    if n == '3' and third(mas) is not False: return third(mas)
    if n == '4' and fourthy(mas) is not False: return fourthy(mas)
    else: return False


if __name__ == '__main__':
    main()