from csv import reader, writer
import customtkinter as CTk


def first(mas):
    diction = dict()
    mas = mas.split(', ')
    for i in range(0, len(mas), 2):
        if mas[i] not in diction.keys():
            diction[mas[i]] = 1
    return reversed([f'Количество ключей в словаре: {str(len(diction.keys()))}'])


def second():
    with open(r'/Users/yaromochka/IdeaProjects/DSTU/PythonLang/ProgrammingLanguages/files/student.csv', encoding='mac_roman') as f:
        file, temp, ans = list(reader(f)), {}, {}
        for i in file[1::]:
            i = (''.join(i)).split(';')
            temp[i[0]] = i[1::]
        for row in temp.items():
            if int(row[1][1]) > 22: ans[row[0]] = row[1]
        return reversed(('Изначальный файл', *[' '.join(i) for i in file], 'Отсортированные значения', *[f'{k[0]}:{" ".join(k[1])}' for k in ans.items()]))


def third(mas):
    group = mas
    with open(r"/Users/yaromochka/IdeaProjects/DSTU/PythonLang/ProgrammingLanguages/files/student.csv", encoding='mac_roman') as f:
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
                tplvl_label = CTk.CTkTextbox(master=toplevel_window, font=('Helvetica Bold', 22), fg_color='transparent', wrap='word', height=120)
                tplvl_label.pack(fill='x')
                tplvl_label.configure(state='normal')
                tplvl_label.insert('0.0', 'Вы хотите перезаписать изменения?')
                tplvl_label.configure(state='disabled')
                yes_but = CTk.CTkButton(master=toplevel_window, text='Да', width=100, command=save)
                yes_but.pack(side='left', anchor='sw', padx=(10, 10), pady=(0, 50))
                no_but = CTk.CTkButton(master=toplevel_window, text='Нет', width=100, command=exit)
                no_but.pack(side='right', anchor='se', padx=(10, 10), pady=(0, 50))
            return reversed(['Отсортированные значения', *[f'{k[0]}:{" ".join([str(i) for i in k[1]])}' for k in temp.items()]])
        
def save():
    with open(r"/Users/yaromochka/IdeaProjects/DSTU/PythonLang/ProgrammingLanguages/files/student.csv") as f:
        file, temp = list(reader(f)), {}
        for i in file[1::]:
            i = (''.join(i)).split(';')
            temp[i[0]] = i[1::]
        for row in temp.values():
            if row[2] == group:
                row[1] = int(row[1]) - 1
        with open(r"/Users/yaromochka/IdeaProjects/DSTU/PythonLang/ProgrammingLanguages/files/new_student.csv", "w") as g:
            wr = writer(g)
            for row in temp.items():
                wr.writerow(row)
    toplevel_window.destroy()



def exit():
    toplevel_window.destroy()


def main(n, *, mas):
    global group
    group = mas
    if n == '1' and first(mas) is not False: return first(mas)
    if n == '2' and second() is not False: return second()
    if (n == '3' or n == '4'): return third(mas)
    else: return False


if __name__ == '__main__':
    main()