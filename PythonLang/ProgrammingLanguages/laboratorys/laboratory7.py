from csv import reader, writer
import customtkinter as CTk

"""
1. Пусть дан словарь. Посчитайте и выведите сколько в словаре ключей
"""


def first(mas: str) -> reversed[str]:
    diction = dict()
    mas = mas.split(', ')
    for i in range(0, len(mas), 2):
        if mas[i] not in diction.keys():
            diction[mas[i]] = 1
    return reversed([f'Количество ключей в словаре: {str(len(diction.keys()))}'])


"""
2. Пусть дан файл students.csv, в котором содержится информация о
студентах в виде:
№;ФИО;Возраст;Группа
1;Иванов Иван Иванович;23;БО-111111
2;Сидоров Семен Семенович;23;БО-111111
3;Яшков Илья Петрович;24;БО-222222
...
Считайте информацию из файла в структуру: {№: [ФИО, Возраст,
Группа], №: [....], №: [....]} (словарь, где ключи – это порядковые номера
студентов).
Вариант 4. Выведите информацию о студентах, в возрасте старше 22 лет.
"""


def second() -> reversed[str]:
    with open(r'/PythonLang/ProgrammingLanguages/files/student.csv', encoding='mac_roman') as f:
        file, temp, ans = list(reader(f)), {}, {}
        for i in file[1::]:
            i = (''.join(i)).split(';')
            temp[i[0]] = i[1::]
        for row in temp.items():
            if int(row[1][1]) > 22: ans[row[0]] = row[1]
        return reversed(('Изначальный файл', *[' '.join(i) for i in file],
                         'Отсортированные значения', *[f'{k[0]}:{" ".join(k[1])}' for k in ans.items()]))


"""
3. Добавьте к задаче №2 возможность:
Вариант 4. Уменьшить возраст студентов в заданной
пользователем группе на 1.
"""


def third(mas: str) -> list[str] | tuple[str] | reversed[str]:
    group = mas
    with open(r"/PythonLang/ProgrammingLanguages/files/student.csv", encoding='mac_roman') as f:
        file, temp = list(reader(f)), {}
        for i in file[1::]:
            i = (''.join(i)).split(';')
            temp[i[0]] = i[1::]
        groups = set(k[2] for k in temp.values())
        if group not in groups:
            return ['Такой группы нет в файле']
        else:
            for row in temp.values():
                if row[2] == group:
                    row[1] = int(row[1]) - 1
            global toplevel_window
            toplevel_window = None
            if toplevel_window is None or not toplevel_window.winfo_exists():
                toplevel_window = CTk.CTkToplevel()
                toplevel_window.title('Изменения')
                toplevel_window.geometry('300x200')
                toplevel_window.resizable(False, False)
                tplvl_label = CTk.CTkTextbox(master=toplevel_window, font=('Helvetica Bold', 22),
                                             fg_color='transparent', wrap='word', height=120)
                tplvl_label.pack(fill='x')
                tplvl_label.configure(state='normal')
                tplvl_label.insert('0.0', 'Вы хотите перезаписать изменения?')
                tplvl_label.configure(state='disabled')
                yes_but = CTk.CTkButton(master=toplevel_window, text='Да', width=100, command=save)
                yes_but.pack(side='left', anchor='sw', padx=(10, 10), pady=(0, 50))
                no_but = CTk.CTkButton(master=toplevel_window, text='Нет', width=100, command=exit)
                no_but.pack(side='right', anchor='se', padx=(10, 10), pady=(0, 50))
            return reversed(['Отсортированные значения', *[f'{k[0]}:'
                                                           f'{" ".join([str(i) for i in k[1]])}' for k in
                                                           temp.items()]])


"""
4. Добавьте к пользовательскому интерфейсу из задачи №3 возможность
сохранения новых данных в файл.
"""


def save() -> None:
    with open(r"/PythonLang/ProgrammingLanguages/files/student.csv") as f:
        file, temp = list(reader(f)), {}
        for i in file[1::]:
            i = (''.join(i)).split(';')
            temp[i[0]] = i[1::]
        for row in temp.values():
            if row[2] == group:
                row[1] = int(row[1]) - 1
        with open(r"/PythonLang/ProgrammingLanguages/files/new_student.csv", "w") as g:
            wr = writer(g)
            for row in temp.items():
                wr.writerow(row)
    toplevel_window.destroy()


def exit():
    toplevel_window.destroy()


def main(n: int, *, mas: str) -> bool | reversed[str] | tuple[str] | str | None:
    global group
    group = mas
    if n == '1' and first(mas) is not False: return first(mas)
    if n == '2' and second() is not False: return second()
    if n == '3' or n == '4':
        return third(mas)
    else:
        return False


if __name__ == '__main__':
    main()
