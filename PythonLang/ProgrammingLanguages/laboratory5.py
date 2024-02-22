import os
from csv import reader, writer
import customtkinter as CTk


def first(mas):
    try: files = os.listdir(mas)
    except: return False
    return [f'Количество файлов в директории: {len(files)}']


def second():
    with open(r'C:\Users\Romochka\PycharmProjects\pythonProject\Learning\2.1_labs_LP\files\student.csv') as f:
        file = [(''.join(i)).split(';') for i in reader(f)]
        ans = []
        ans.append(file[0])
        for row in file[1::]:
             if int(row[2]) > 22: ans.append(row)
        print(ans)
        return reversed(('Изначальный файл', *[' '.join(i) for i in file], 'Отсортированные значения', *[' '.join(i) for i in ans]))


def third(mas):
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
                tplvl_label = CTk.CTkTextbox(master=toplevel_window, font=('Helvetica Bold', 22), fg_color='transparent', wrap='word', height=120)
                tplvl_label.pack(fill='x')
                tplvl_label.configure(state='normal')
                tplvl_label.insert('0.0', 'Вы хотите перезаписать изменения?')
                tplvl_label.configure(state='disabled')
                yes_but = CTk.CTkButton(master=toplevel_window, text='Да', width=100, command=save)
                yes_but.pack(side='left', anchor='sw', padx=(10, 10), pady=(0, 50))
                no_but = CTk.CTkButton(master=toplevel_window, text='Нет', width=100, command=exit)
                no_but.pack(side='right', anchor='se', padx=(10, 10), pady=(0, 50))
            return reversed([*[' '.join((str(j) for j in i)) for i in file]])
        
def save():
    with open(r"C:\Users\Romochka\PycharmProjects\pythonProject\Learning\2.1_labs_LP\files\student.csv") as f:
        file = [(''.join(i)).split(';') for i in reader(f)]
        for row in file:
            if row[3] == group:
                row[2] = int(row[2]) - 1
        with open(r"C:\Users\Romochka\PycharmProjects\pythonProject\Learning\2.1_labs_LP\files\new_student.csv", "w") as g:
            wr = writer(g)
            for row in file:
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