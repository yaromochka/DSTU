import customtkinter as CTk
import CTkListbox
import configparser
import laboratory1, laboratory2, laboratory3, laboratory4, laboratory5, laboratory7, laboratory8, laboratory9, laboratory10, laboratory11, laboratory12, laboratory13, laboratory14


class App(CTk.CTk):

    def __init__(self):
        super().__init__()

        CTk.set_appearance_mode('dark')
        CTk.set_default_color_theme('green')

        self.geometry('900x600')
        self.title('SuperProgramm')
        self.resizable(False, False)
        self.main_frame()


    def main_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

        """ФРЕЙМ И ТРИ ПЕРВОНАЧАЛЬНЫЕ КНОПКИ"""
        self.buttons_frame = CTk.CTkFrame(master=self, fg_color='transparent')
        self.buttons_frame.pack(expand=True, anchor='center')

        self.start_button = CTk.CTkButton(master=self.buttons_frame, text='Начало', width=200, height=50, font=('Helvetica Bold', 25), command=self.start)
        self.start_button.pack(pady=(0, 20))

        self.settings_button = CTk.CTkButton(master=self.buttons_frame, text='Настройки', width=200, height=50, font=('Helvetica Bold', 25), command=self.settings)
        self.settings_button.pack(pady=(0, 20))

        self.exit_button = CTk.CTkButton(master=self.buttons_frame, text='Выход', width=200, height=50, font=('Helvetica Bold', 25), command=self.exit)
        self.exit_button.pack(pady=(0, 20))


    def start(self):
        self.buttons_frame.destroy()
        self.task_desc = None

        """КНОПКА <<НАЗАД>>"""
        self.back_button = CTk.CTkButton(master=self, text='Назад', width=200, height=50, font=('Helvetica Bold', 25), command=self.main_frame)
        self.back_button.pack(side='top', anchor='nw', padx=(20, 20), pady=(10, 10))

        """ВЕРТИКАЛЬНЫЙ СПИСОК"""
        self.lis = CTkListbox.CTkListbox(master=self, font=('Helvetica Bold', 20), command=self.lists_com)
        self.lis.pack(side='left', fill='y')
        for i in range(1, 15):
            self.lis.insert('END', f'Лабораторная №{i}')
        
        """ВЫВОД ОПИСАНИЯ ЗАДАНИЯ"""
        self.task_frame = CTk.CTkFrame(master=self, fg_color='transparent', height=300)
        self.task_frame.pack(side='top', fill='x')
        self.task_frame.pack_propagate(False)

        self.task_desc = CTk.CTkTextbox(master=self.task_frame, height=150, fg_color='transparent', font=('Helvetica Bold', 24), text_color='ivory3', wrap='word', state='disabled')
        self.task_desc.pack(padx=(15, 15), side='top', fill='both', anchor='n', expand=True)

        """ВЫПАДАЮЩИЙ СПИСОК ЗАДАНИЙ"""
        self.tasks_menu = CTk.CTkOptionMenu(master=self.task_frame, values=[f'Задание {i + 1}' for i in range(4)], width=200, height=50, font=('Helvetica Bold', 25), dropdown_font=('Helvetica Bold', 18), state='disabled', command=self.lists_com)
        self.tasks_menu.pack(pady=(10, 10), padx=(0, 10), side='right', anchor='se')

        """КНОПКА ПОЛУЧЕНИЯ ДАННЫХ"""
        self.button = CTk.CTkButton(master=self.task_frame, text='Ввести данные', width=500, height=50, font=('Helvetica Bold', 25), state='disabled', command=self.button_click_event)
        self.button.pack(pady=(10, 10), side='right', padx=(10, 10), anchor='s')

        self.ans_frame = CTk.CTkFrame(master=self, fg_color='gray20', height=250)
        self.ans_frame.pack(side='bottom', anchor='s', fill='x')
        self.ans_frame.pack_propagate(False)

        self.ans_label = CTk.CTkTextbox(master=self.ans_frame, height=150, fg_color='transparent', font=('Helvetica Bold', 24), text_color='ivory3', wrap='word', state='disabled')
        self.ans_label.pack(padx=(15, 15), fill='both', anchor='center', expand=True)

        self.toplevel_window = None


    def button_click_event(self):
        """ДИАЛОГОВОЕ INPUT-ОКНО ДЛЯ КНОПКИ"""
        self.dialog = CTk.CTkInputDialog(text="Введите даные (если их несколько, вводить надо через запятую) ", title="Ввод данных")
        self.a = self.dialog.get_input()

        if self.a is not None:
            """ПОЛУЧЕНИЕ ТЕКУЩЕЙ ЛАБОРАТОРНОЙ И ЗАДАНИЯ"""
            self.lab_num = str(self.lis.curselection() + 1)
            self.task_num =  str(self.tasks_menu.get()).split(' ')[1]
            self.ans_num = self.lab_num + self.task_num
            """RETURN ЛАБОРАТОРНОЙ"""
            self.ret = self.labors(self.lab_num)
            if self.ret is not False and self.ret is not None:
                """ ВЫВОД ДАННЫХ """
                for txt in self.ret:
                    self.ans_label.configure(state='normal')
                    self.ans_label.insert('0.0', txt + '\n\n')
                    self.ans_label.configure(state='disabled')
            else:
                """ ОКНО С ОШИБКОЙ"""
                if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                        self.toplevel_window = CTk.CTkToplevel(self)
                        self.toplevel_window.title('Ошибка')
                        self.toplevel_window.geometry('300x200')
                        self.toplevel_window.resizable(False, False)
                        self.tplvl_label = CTk.CTkLabel(master=self.toplevel_window, text='Неверно введены данные', font=('Helvetica Bold', 22))
                        self.tplvl_label.pack(expand=True, anchor='center')
                else:
                    self.toplevel_window.focus()           


    def lists_com(self, event):
        """ОЖИВЛЕНИЕ КНОПКИ И СПИСКА"""
        self.tasks_menu.configure(state='normal')
        self.button.configure(state='normal')
        if (int(self.lis.curselection()) + 1) == 10: self.tasks_menu.configure(values=[f'Задание {i + 1}' for i in range(8)])
        elif (int(self.lis.curselection()) + 1) == 11: self.tasks_menu.configure(values=[f'Задание {i + 1}' for i in range(5)])
        elif (int(self.lis.curselection()) + 1) == 14: self.tasks_menu.configure(values=[f'Задание {i + 1}' for i in range(6)])
        elif (int(self.lis.curselection()) + 1) == 13: self.tasks_menu.configure(values=[f'Задание {i + 1}' for i in range(13)])
        elif (int(self.lis.curselection()) + 1) == 8 or (int(self.lis.curselection()) + 1) == 12: self.tasks_menu.configure(values=[f'Задание {i + 1}' for i in range(3)])
        else: self.tasks_menu.configure(values=[f'Задание {i + 1}' for i in range(4)])

        """УДАЛЕНИЕ ОТВЕТА ПРОШЛОГО ЗАДАНИЯ"""
        self.ans_label.configure(state='normal')
        if self.ans_label is not None:
            self.ans_label.delete("0.0", "end")
        self.ans_label.configure(state='disabled')

        """ПОЛУЧЕНИЕ ДАННЫХ О ТЕКУЩЕЙ ЛАБОРАТОРНОЙ И ЗАДАНИИ"""
        self.lab_num = str(self.lis.curselection() + 1)
        self.task_num = str(self.tasks_menu.get()).split(' ')[1]

        """ВЫВОД ОПИСАНИЯ ЗАДАНИЯ"""
        self.task_desc.configure(state='normal')
        if self.task_desc is not None:
            self.task_desc.delete("0.0", "end")
        self.task_pars = configparser.ConfigParser()
        self.task_pars.read(r'tasks.ini', encoding="utf-8")
        self.task_desc.insert('0.0', self.task_pars.get('Tasks',  f'{self.lab_num + self.task_num}', fallback='Ещё не сделано =((').replace('"', ''))
        self.task_desc.configure(state='disabled')

    def settings(self):
        for widget in self.winfo_children():
            widget.destroy()

    def exit(self):
        self.toplevel_window = None
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = CTk.CTkToplevel()
            self.toplevel_window.title('Изменения')
            self.toplevel_window.geometry('300x200')
            self.toplevel_window.resizable(False, False)
            self.tplvl_label = CTk.CTkTextbox(master=self.toplevel_window, font=('Helvetica Bold', 22), fg_color='transparent', wrap='word', height=120)
            self.tplvl_label.pack(fill='x')
            self.tplvl_label.configure(state='normal')
            self.tplvl_label.insert('0.0', '\nВы точно хотите выйти?')
            self.tplvl_label.configure(state='disabled')
            self.yes_but = CTk.CTkButton(master=self.toplevel_window, text='Да', width=100, command=self.yes)
            self.yes_but.pack(side='left', anchor='sw', padx=(10, 10), pady=(0, 50))
            self.no_but = CTk.CTkButton(master=self.toplevel_window, text='Нет', width=100, command=self.no)
            self.no_but.pack(side='right', anchor='se', padx=(10, 10), pady=(0, 50))
    def yes(self): exit()
    def no(self): self.toplevel_window.destroy()


    """МЕТОД ОБРАЩЕНИЯ К ЛАБОРАТОРНЫМ"""
    def labors(self, num):
        """УДАЛЕНИЕ ОТВЕТА ПРЕДЫДУЩЕГО ЗАДАНИЯ"""
        self.ans_label.configure(state='normal')
        if self.ans_label is not None:
            self.ans_label.delete("0.0", "end")
        self.ans_label.configure(state='disabled')
        if num == '1': return laboratory1.main(self.task_num, mas=self.a)
        if num == '2': return laboratory2.main(self.task_num, mas=self.a)
        if num == '3': return laboratory3.main(self.task_num, mas=self.a)
        if num == '4': return laboratory4.main(self.task_num, mas=self.a)
        if num == '5': return laboratory5.main(self.task_num, mas=self.a)
        if num == '7': return laboratory7.main(self.task_num, mas=self.a)
        if num == '8': return laboratory8.main(self.task_num, mas=self.a)
        if num == '9': return laboratory9.main(self.task_num, mas=self.a)
        if num == '10': return laboratory10.main(self.task_num, mas=self.a)
        if num == '11': return laboratory11.main(self.task_num, mas=self.a)
        if num == '12': return laboratory12.main(self.task_num, mas=self.a)
        if num == '13': return laboratory13.main(self.task_num, mas=self.a)
        if num == '14': return laboratory14.main(self.task_num, mas=self.a)


if __name__ == '__main__':
    app = App()
    app.mainloop()