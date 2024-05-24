import tkinter as tk
from tkinter import messagebox


def button_solve() -> None:
    try:
        first_number = int(first_number_entry.get())
        second_number = int(second_number_entry.get())
        text.delete(1.0, tk.END)
        text.insert(1.0, f"{first_number} + {second_number} = {first_number + second_number}\n")
        text.insert(2.0, f"{first_number} * {second_number} = {first_number * second_number}\n")
        text.insert(3.0, f"{first_number} / {second_number} = {first_number / second_number}\n")
    except:
        messagebox.showerror(title="Ошибка", message="Неверное введены данные")


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Зачёт")

    root.geometry("500x300")
    root.resizable(False, False)

    # Первое поле ввода
    first_number_entry = tk.Entry()
    first_number_entry.pack(anchor="nw", padx=8, pady=8)

    # Второе поле ввода
    second_number_entry = tk.Entry()
    second_number_entry.pack(anchor="nw", padx=8, pady=8)

    # Кнопка "Отправить"
    send_button = tk.Button(text="Посчитать", command=button_solve)
    send_button.pack(anchor="nw", padx=8, pady=8)

    # Textbox ниже кнопки
    text = tk.Text(root)
    text.pack(anchor="nw", padx=8, pady=8)

    root.mainloop()
