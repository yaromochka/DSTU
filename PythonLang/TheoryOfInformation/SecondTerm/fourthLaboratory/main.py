import tkinter as tk
from tkinter import messagebox
from CyclicCoder import CyclicCoder


class CyclicCodeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Циклический код")

        self.coder = None
        self.encoded = []

        self.input_type = tk.StringVar(value="polynomial")

        self.matrix_entries = []

        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.root, text="Выберите тип ввода:").pack()
        tk.Radiobutton(self.root, text="Полином", variable=self.input_type, value="polynomial", command=self.update_input_fields).pack()
        tk.Radiobutton(self.root, text="Матрица", variable=self.input_type, value="matrix", command=self.update_input_fields).pack()

        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(pady=5)
        self.update_input_fields()

        tk.Label(self.root, text="Введите текст для кодирования:").pack()
        self.text_input = tk.Text(self.root, height=4, width=50)
        self.text_input.pack()

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

    def update_input_fields(self):
        for widget in self.input_frame.winfo_children():
            widget.destroy()

        if self.input_type.get() == "polynomial":
            tk.Label(self.input_frame, text="Введите полином (через запятую, например 1,0,1,1):").pack()
            self.poly_entry = tk.Entry(self.input_frame, width=50)
            self.poly_entry.pack()
        else:
            tk.Label(self.input_frame, text="Размер матрицы:").pack()

            size_frame = tk.Frame(self.input_frame)
            size_frame.pack()

            tk.Label(size_frame, text="Строк:").pack(side=tk.LEFT)
            self.rows_entry = tk.Entry(size_frame, width=5)
            self.rows_entry.pack(side=tk.LEFT, padx=2)

            tk.Label(size_frame, text="Столбцов:").pack(side=tk.LEFT)
            self.cols_entry = tk.Entry(size_frame, width=5)
            self.cols_entry.pack(side=tk.LEFT, padx=2)

            tk.Button(self.input_frame, text="Создать матрицу", command=self.create_matrix_input).pack(pady=2)
            self.matrix_frame = tk.Frame(self.input_frame)
            self.matrix_frame.pack()

    def create_matrix_input(self):
        for widget in self.matrix_frame.winfo_children():
            widget.destroy()
        self.matrix_entries = []

        try:
            rows = int(self.rows_entry.get())
            cols = int(self.cols_entry.get())
            for i in range(rows):
                row_entries = []
                row_frame = tk.Frame(self.matrix_frame)
                row_frame.pack()
                for j in range(cols):
                    e = tk.Entry(row_frame, width=3)
                    e.pack(side=tk.LEFT)
                    row_entries.append(e)
                self.matrix_entries.append(row_entries)
        except Exception as e:
            messagebox.showerror("Ошибка", f"Неверный формат размера матрицы: {e}")

    def encode_text(self):
        text = self.text_input.get("1.0", tk.END).strip()
        try:
            if self.input_type.get() == "polynomial":
                poly_str = self.poly_entry.get().strip()
                poly = [int(x) for x in poly_str.split(",")]
                self.coder = CyclicCoder(generator_poly=poly)
            else:
                matrix = []
                for row in self.matrix_entries:
                    matrix.append([int(e.get()) for e in row])
                self.coder = CyclicCoder(generator_matrix=matrix)

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
