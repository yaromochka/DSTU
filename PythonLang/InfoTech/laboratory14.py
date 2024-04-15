from tkinter import *


def clicked():
    T = float(btn1.get())
    TF = 32 + 9 / 5 * T
    res = f'Температура по Фаренгейту равна: {TF}'
    btn1.delete(0, END)
    btn1.insert(0, '0')
    lbl.configure(text=res)




def first():
    wd = Tk()
    wd.title('Задание 1')
    wd.geometry('300x400')
    Label(wd, text='Введите температуру в градусах Цельсия: ', font=('Times New Roman', 12)).grid(stick='wens')
    global btn1
    btn1 = Entry(wd, width=40)
    btn1.insert(0, '0')
    btn1.grid()
    global btn2
    btn2 = Button(text="Ввести значение", command=clicked)
    btn2.grid()
    global lbl
    lbl = Label(wd, text='Температура по Фаренгейту равна: 32', font=('Times New Roman', 12))
    lbl.grid(row=3)
    wd.mainloop()


def click():
    A, B, C = int(btnA.get()), int(btnB.get()), int(btnC.get())
    btnA.delete(0, END)
    btnB.delete(0, END)
    btnC.delete(0, END)
    if all([i > 0 for i in [A, B, C]]):
        lbl2.configure(text=f'Числа {A}, {B} и {C} - положительные')
    else:
        a = []
        for i in [A, B, C]:
            if i < 0:
                a.append(i)
        lbl2.configure(text=f'Отрицательные числа - {a}')
    btnA.insert(0, '0')
    btnB.insert(0, '0')
    btnC.insert(0, '0')


def second():
    wd = Tk()
    wd.title('Задание 2')
    wd.geometry('300x400')
    global btnA, btnB, btnC
    btnA = Entry(wd)
    Label(wd, text='Введите значение A: ', font=('Times New Roman', 12)).grid(stick='', row=1)
    btnA.grid(row=1, column=2, pady=0)
    btnA.insert(0, '0')
    Label(wd, text='Введите значение B: ', font=('Times New Roman', 12)).grid(stick='wens')
    btnB = Entry(wd)
    btnB.insert(0, '0')
    btnB.grid(row=2, column=2, pady=20)
    Label(wd, text='Введите значение C: ', font=('Times New Roman', 12)).grid(stick='wens')
    btnC = Entry(wd)
    btnC.insert(0, '0')
    btnC.grid(row=3, column=2, pady=5)
    btnEnt = Button(text="Ввести значение", command=click)
    btnEnt.grid(columnspan=3)
    global lbl2
    lbl2 = Label(wd, text='Введите числовые значения', font=('Times New Roman', 12))
    lbl2.grid(columnspan=3)

    wd.mainloop()


def clicker():
    N = int(btnN.get())
    K = 0
    while 2 ** K != N:
        if K >= N ** 0.5:
            lbl3.configure(text=f'Число {N} не является степенью числа 2')
            break
        K += 1
    else:
        lbl3.configure(text=f'Число {N} равно числу 2 в степени {K}')
    btnN.delete(0, END)
    btnN.insert(0, '0')


def third():
    global wd3
    wd3 = Tk()
    wd3.title('Карпов Роман ВКБ12')
    wd3.geometry('300x400')
    Label(wd3, text='Введите число N', font=('Times New Roman', 12)).grid(columnspan=2, pady=5)
    global btnN
    btnN = Entry(wd3)
    btnN.insert(0, '0')
    btnN.grid(columnspan=2)
    btnEnt = Button(text="Ввести значение", command=clicker)
    btnEnt.grid()
    global lbl3
    lbl3 = Label(wd3, text=f'', font=('Times New Roman', 12))
    lbl3.grid()


    wd3.mainloop()


def main():
    try:
        a = int(input('Введите номер задания: '))
    except ValueError:
        print('Неверный номер задания')
        exit()
    if a == 1:
        first()
    elif a == 2:
        second()
    elif a == 3:
        third()
    else:
        print('Неверный номер задания')


if __name__ == '__main__':
    main()