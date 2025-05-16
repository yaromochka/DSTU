import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import numpy as np
from AdaptiveSystem import AdaptiveSystem
from enums.matrix import MatrixType

class AdaptiveSystemGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Адаптивная система кодирования")
        self.adaptiveSystem = AdaptiveSystem()
        self.encoded_data = []

        self.setup_widgets()

    def setup_widgets(self):
        frame_top = ttk.Frame(self.root)
        frame_top.pack(pady=5)

        ttk.Label(frame_top, text="n:").grid(row=0, column=0)
        self.n_entry = ttk.Entry(frame_top, width=5)
        self.n_entry.grid(row=0, column=1)

        ttk.Label(frame_top, text="k:").grid(row=0, column=2)
        self.k_entry = ttk.Entry(frame_top, width=5)
        self.k_entry.grid(row=0, column=3)

        self.matrix_type = tk.StringVar(value="G")
        ttk.Radiobutton(frame_top, text="G", variable=self.matrix_type, value="G").grid(row=0, column=4)
        ttk.Radiobutton(frame_top, text="H", variable=self.matrix_type, value="H").grid(row=0, column=5)

        ttk.Button(self.root, text="Загрузить из файла", command=self.load_text_from_file).pack(pady=5)

        self.create_matrix_button = ttk.Button(frame_top, text="Создать матрицу", command=self.create_matrix_grid)
        self.create_matrix_button.grid(row=0, column=6, padx=5)

        self.set_matrix_button = ttk.Button(frame_top, text="Установить матрицу", command=self.set_matrix)
        self.set_matrix_button.grid(row=0, column=7, padx=5)

        self.matrix_frame = ttk.Frame(self.root)
        self.matrix_frame.pack(pady=5)

        self.text_input = tk.Text(self.root, height=3, width=50)
        self.text_input.pack(pady=5)

        frame_buttons = ttk.Frame(self.root)
        frame_buttons.pack(pady=5)

        ttk.Button(frame_buttons, text="Кодировать", command=self.encode).grid(row=0, column=0, padx=5)
        ttk.Button(frame_buttons, text="Добавить случайные ошибки", command=self.add_random_errors).grid(row=0, column=1, padx=5)
        ttk.Button(frame_buttons, text="Добавить ошибки вручную", command=self.add_manual_errors).grid(row=0, column=2, padx=5)
        ttk.Button(frame_buttons, text="Декодировать", command=self.decode).grid(row=0, column=3, padx=5)

        self.output_area = tk.Text(self.root, height=15, width=80)
        self.output_area.pack(pady=5)

    def load_text_from_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read().strip()
                    self.adaptiveSystem.set_text(content)
                    self.text_input.delete(1.0, tk.END)
                    self.text_input.insert('1.0', content)
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось прочитать файл:\n{e}")

    def create_matrix_grid(self):
        for widget in self.matrix_frame.winfo_children():
            widget.destroy()

        try:
            n = int(self.n_entry.get())
            k = int(self.k_entry.get())
        except:
            messagebox.showerror("Ошибка", "Введите корректные значения n и k")
            return

        self.matrix_entries = []
        rows = k if self.matrix_type.get() == "G" else n
        cols = n if self.matrix_type.get() == "G" else n - k

        for i in range(rows):
            row_entries = []
            for j in range(cols):
                entry = ttk.Entry(self.matrix_frame, width=3)
                entry.grid(row=i, column=j, padx=2, pady=2)
                entry.insert(0, "0")
                row_entries.append(entry)
            self.matrix_entries.append(row_entries)

    def get_matrix(self) -> np.array:
        try:
            return np.array([[int(cell.get()) for cell in row] for row in self.matrix_entries])
        except:
            messagebox.showerror("Ошибка", "Матрица должна содержать только 0 и 1")
            return

    def set_matrix(self):
        try:
            n = int(self.n_entry.get())
            k = int(self.k_entry.get())
        except:
            messagebox.showerror("Ошибка", "Введите корректные значения n и k")
            return

        matrix = self.get_matrix()
        if matrix is None:
            return

        m_type = MatrixType.MATRIX_G if self.matrix_type.get() == "G" else MatrixType.MATRIX_H
        self.adaptiveSystem.set_matrix((matrix, m_type))

        self.output_area.insert(tk.END, f"\n[Матрица установлена]\nТип: {self.matrix_type.get()}, Размер: {matrix.shape[::-1]}\n")

    def encode(self):
        text = self.text_input.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Внимание", "Введите текст для кодирования")
            return
        try:
            self.adaptiveSystem.set_text(text)
            print('текст установлен')
            self.adaptiveSystem.encode()
            print('закодировано')
            self.encoded_data = self.adaptiveSystem.get_encoded_text()
            self.output_area.insert(tk.END, f"\n[Ввод: {text}]\n[Закодировано: {''.join(map(str, self.encoded_data))}]\n")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка при кодировании:\n{str(e)}")

    def decode(self):
        if not self.adaptiveSystem or not self.encoded_data:
            messagebox.showwarning("Внимание", "Сначала закодируйте данные")
            return
        try:
            self.adaptiveSystem.solve_errors()
            self.adaptiveSystem.decode()
        except:
            messagebox.showwarning("Ошибка", "Не удалось подобрать матрицу. Попробуйте ещё раз")
            return
        self.output_area.insert(tk.END, f"\n[Декодировано: {self.adaptiveSystem.get_decoded_text()}]\n")

    def add_random_errors(self):
        if not self.encoded_data:
            messagebox.showwarning("Внимание", "Сначала закодируйте данные")
            return
        self.adaptiveSystem.add_errors()
        self.output_area.insert(tk.END, "\n[Добавлены 3 случайные ошибки]\n")

    def add_manual_errors(self):
        if not self.encoded_data:
            messagebox.showwarning("Внимание", "Сначала закодируйте данные")
            return

        def apply_errors():
            try:
                positions = list(map(int, error_entry.get().split()))
                self.adaptiveSystem.add_manual_errors(positions)
                self.output_area.insert(tk.END, f"\n[Добавлены ошибки в позиции: {positions}]\n")
                error_win.destroy()
            except:
                messagebox.showerror("Ошибка", "Введите позиции через пробел (например: 0 2 5)")

        error_win = tk.Toplevel(self.root)
        error_win.title("Ввод ошибок вручную")
        ttk.Label(error_win, text="Введите позиции битов с ошибками (через пробел):").pack(padx=10, pady=5)
        error_entry = ttk.Entry(error_win, width=40)
        error_entry.pack(padx=10, pady=5)
        ttk.Button(error_win, text="Применить", command=apply_errors).pack(padx=10, pady=10)

# --- Запуск ---
if __name__ == "__main__":
    root = tk.Tk()
    app = AdaptiveSystemGUI(root)
    root.mainloop()
