import tkinter as tk
from tkinter import messagebox
from CyclicCoder import CyclicCoder


class CyclicCodeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Циклический код")

        self.coder = None
        self.encoded = []

        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.root, text="Введите текст для кодирования:").pack()
        self.text_input = tk.Text(self.root, height=4, width=50)
        self.text_input.pack()

        tk.Label(self.root, text="Введите полином (через запятую, например 1,0,1,1):").pack()
        self.poly_entry = tk.Entry(self.root, width=50)
        self.poly_entry.pack()

        tk.Button(self.root, text="Кодировать", command=self.encode_text).pack(pady=5)

        tk.Label(self.root, text="Закодированная битовая последовательность:").pack()
        self.encoded_output = tk.Text(self.root, height=5, width=60)
        self.encoded_output.pack()

        tk.Label(self.root, text="Внести ошибки (позиции через запятую):").pack()
        self.error_entry = tk.Entry(self.root, width=50)
        self.error_entry.pack()

        tk.Button(self.root, text="Внести ошибки", command=self.introduce_errors).pack(pady=5)

        tk.Button(self.root, text="Декодировать", command=self.decode_text).pack(pady=5)

        tk.Label(self.root, text="Результат декодирования:").pack()
        self.decoded_output = tk.Text(self.root, height=4, width=50)
        self.decoded_output.pack()

    def encode_text(self):
        text = self.text_input.get("1.0", tk.END).strip()
        poly_str = self.poly_entry.get().strip()
        try:
            poly = [int(x) for x in poly_str.split(",")]
            self.coder = CyclicCoder(generator_poly=poly)
            self.encoded = self.coder.encode_text(text)
            self.encoded_output.delete("1.0", tk.END)
            self.encoded_output.insert(tk.END, ' '.join(map(str, self.encoded)))
            self.decoded_output.delete("1.0", tk.END)
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    def introduce_errors(self):
        if not self.encoded:
            messagebox.showwarning("Предупреждение", "Сначала выполните кодирование")
            return
        try:
            positions = [int(x) for x in self.error_entry.get().split(",")]
            self.encoded = self.coder.add_manual_errors(self.encoded, positions)
            self.encoded_output.delete("1.0", tk.END)
            self.encoded_output.insert(tk.END, ' '.join(map(str, self.encoded)))
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    def decode_text(self):
        if not self.encoded:
            messagebox.showwarning("Предупреждение", "Нет данных для декодирования")
            return
        try:
            decoded = self.coder.decode_to_text_megitt(self.encoded)
            self.decoded_output.delete("1.0", tk.END)
            self.decoded_output.insert(tk.END, decoded)
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))


if __name__ == '__main__':
    root = tk.Tk()
    app = CyclicCodeApp(root)
    root.mainloop()