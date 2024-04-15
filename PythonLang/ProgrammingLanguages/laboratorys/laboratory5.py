import os
from csv import reader, writer
import customtkinter as CTk

"""
1. Пусть дана некоторая директория (папка). Посчитайте количество файлов
в данной директории (папке) и выведите на экран. 
"""


def first(mas: str) -> bool | list[str]:
    try:
        files = os.listdir(mas)
    except:
        return False
    return [f'Количество файлов в директории: {len(files)}']


"""
2. Пусть дан файл students.csv, в котором содержится информация о
студентах в виде:
№;ФИО;Возраст;Группа
1;Иванов Иван Иванович;23;БО-111111
2;Сидоров Семен Семенович;23;БО-111111
3;Яшков Илья Петрович;24;БО-222222
Считайте информацию из файла в структуру: [[№, ФИО, Возраст,
Группа],[№, ФИО, Возраст, Группа],[№, ФИО, Возраст, Группа]] (список
списков).
Вариант 4. Выведите информацию о студентах, в возрасте
старше 22 лет.
"""


def second() -> reversed[str]:
    with open(r'C:\Users\Romochka\PycharmProjects\pythonProject\Learning\2.1_labs_LP\files\student.csv') as f:
        file = [(''.join(i)).split(';') for i in reader(f)]
        ans = [file[0]]
        for row in file[1::]:
            if int(row[2]) > 22:
                ans.append(row)
        return reversed(
            ('Изначальный файл', *[' '.join(i) for i in file], 'Отсортированные значения', *[' '.join(i) for i in ans]))


"""
3. Добавьте к задаче №2 пользовательский интерфейс:
Вариант 4. По уменьшению возраста студентов в заданной
пользователем группе на 1.
"""


def third(mas: str) -> reversed[str] | list[str]:
    group = mas
    with open(r"C:\Users\Romochka\PycharmProjects\pythonProject\Learning\2.1_labs_LP\files\student.csv") as f:
        file = [(''.join(i)).split(';') for i in reader(f)]
        groups = [i[3] for i in file[1::]]
        if group not in groups:
            return ['Такой группы нет в файле']
        else:
            for row in file:
                if row[3] == group:
                    row[2] = int(row[2]) - 1
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
            return reversed([*[' '.join((str(j) for j in i)) for i in file]])


"""
4. Добавьте к пользовательскому интерфейсу из задачи №3 возможность
сохранения новых данных обратно в файл.
"""


def save() -> None:
    with open(r"C:\Users\Romochka\PycharmProjects\pythonProject\Learning\2.1_labs_LP\files\student.csv") as f:
        file = [(''.join(i)).split(';') for i in reader(f)]
        for row in file:
            if row[3] == group:
                row[2] = int(row[2]) - 1
        with open(r"C:\Users\Romochka\PycharmProjects\pythonProject\Learning\2.1_labs_LP\files\new_student.csv",
                  "w") as g:
            wr = writer(g)
            for row in file:
                wr.writerow(row)
    toplevel_window.destroy()


def exit():
    toplevel_window.destroy()


def main(n: int, *, mas: str) -> bool | reversed[str] | list[str] | None:
    global group
    group: str = mas
    if n == '1' and first(mas) is not False: return first(mas)
    if n == '2' and second() is not False: return second()
    if n == '3' or n == '4':
        return third(mas)
    else:
        return False


if __name__ == '__main__':
    main()
