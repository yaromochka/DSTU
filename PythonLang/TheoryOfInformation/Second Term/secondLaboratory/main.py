import tkinter as tk
from tkinter import messagebox
from ConvolutionalCode import ConvolutionalCode


def on_set_adders():
    try:
        num_adders = int(entry_adders_count.get())
        for widget in adders_frame.winfo_children():
            widget.destroy()
        adders_labels.clear()
        adders_entries.clear()
        for i in range(num_adders):
            label = tk.Label(adders_frame, text=f'Положение сумматора {i + 1}:')
            label.pack()
            adders_labels.append(label)
            entry = tk.Entry(adders_frame)
            entry.pack()
            adders_entries.append(entry)
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректное число сумматоров")


def on_process():
    text_to_encode = entry_text.get(1.0, tk.END)
    try:
        adders = [list(map(int, entry.get().split(','))) for entry in adders_entries]
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные значения для сумматоров")
        return

    coder = ConvolutionalCode()
    coder.set_text(text_to_encode)
    coder.set_adders(adders)
    coder.encode()
    coder.decode()

    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, f'Бинарный текст: {coder.binary_bits}\n\n')
    result_text.insert(tk.END, f'Закодированный текст: {coder.encoded_text}\n\n')
    result_text.insert(tk.END, f'Закодированный список: {coder.encoded_list}\n\n')
    for state, transitions in coder.graph.items():
        for next_state, encoded in transitions:
            result_text.insert(tk.END, f'{state} -> {next_state} : {encoded}\n')

    result_text.insert(tk.END, f'Декодированный список: {coder.decoded_list}\n\n')
    result_text.insert(tk.END, f'Декодированный текст: {coder.decoded_text}\n')

    result_text.config(state=tk.DISABLED)


root = tk.Tk()
root.title("Сверточное кодирование")

tk.Label(root, text="Введите текст для кодирования:").pack()
entry_text = tk.Text(root,height=15, width=60)
entry_text.pack()

tk.Label(root, text="Введите количество сумматоров:").pack()
entry_adders_count = tk.Entry(root)
entry_adders_count.pack()
tk.Button(root, text="Задать количество сумматоров", command=on_set_adders).pack()

adders_frame = tk.Frame(root)
adders_frame.pack()

adders_labels = []
adders_entries = []

tk.Button(root, text="Закодировать и декодировать текст", command=on_process).pack()

result_text = tk.Text(root, height=15, width=60, state=tk.DISABLED)
result_text.pack()

root.mainloop()