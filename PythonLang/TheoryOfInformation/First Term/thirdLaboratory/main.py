import numpy as np
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from coding_logic import BlockCoder

def _array_to_string(array: np.array) -> str:
    return ''.join([str(num) for num in list(array)])

class BlockCodeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Матричное представление блочных кодов")
        self.coder = BlockCoder()

        # Создаем основной контейнер с отступами
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Выбор матрицы (G или H)
        self.matrix_choice = tk.StringVar(value="H")
        matrix_frame = ttk.LabelFrame(main_frame, text="Выбор матрицы", padding="5")
        matrix_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)

        ttk.Radiobutton(matrix_frame, text="Матрица H", variable=self.matrix_choice,
                       value="H", command=self.clear_matrix).grid(row=0, column=0, padx=5)
        ttk.Radiobutton(matrix_frame, text="Матрица G", variable=self.matrix_choice,
                       value="G", command=self.clear_matrix).grid(row=0, column=1, padx=5)

        # Размер матрицы
        size_frame = ttk.LabelFrame(main_frame, text="Размер матрицы", padding="5")
        size_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)

        ttk.Label(size_frame, text="n:").grid(row=0, column=0, padx=5)
        self.n_entry = ttk.Entry(size_frame, width=5)
        self.n_entry.grid(row=0, column=1, padx=5)

        ttk.Label(size_frame, text="k:").grid(row=0, column=2, padx=5)
        self.k_entry = ttk.Entry(size_frame, width=5)
        self.k_entry.grid(row=0, column=3, padx=5)

        ttk.Button(size_frame, text="Создать матрицу",
                  command=self.create_matrix).grid(row=0, column=4, padx=5)

        # Матрица
        self.matrix_input_frame = ttk.LabelFrame(main_frame, text="Ввод матрицы", padding="5")
        self.matrix_input_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        self.matrix_entries = []

        # Поле для ввода текста
        text_frame = ttk.LabelFrame(main_frame, text="Текст для кодирования", padding="5")
        text_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)

        self.text_entry = scrolledtext.ScrolledText(text_frame, width=50, height=5)
        self.text_entry.grid(row=0, column=0, sticky=(tk.W, tk.E))

        # Кнопки управления
        control_frame = ttk.Frame(main_frame)
        control_frame.grid(row=4, column=0, columnspan=2, pady=5)

        ttk.Button(control_frame, text="Закодировать",
                  command=self.encode_text).grid(row=0, column=0, padx=5)
        ttk.Button(control_frame, text="Добавить ошибки",
                  command=self.add_errors).grid(row=0, column=1, padx=5)
        ttk.Button(control_frame, text="Декодировать",
                  command=self.decode_text).grid(row=0, column=2, padx=5)

        # Вывод результатов
        results_frame = ttk.LabelFrame(main_frame, text="Результаты", padding="5")
        results_frame.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)

        self.output_text = scrolledtext.ScrolledText(results_frame, width=60, height=20)
        self.output_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Сохраняем промежуточные результаты
        self.encoded_blocks = None
        self.corrupted_blocks = None
        self.original_bits = None

    def clear_matrix(self):
        """Очищает поле ввода матрицы"""
        for widget in self.matrix_input_frame.winfo_children():
            widget.destroy()
        self.matrix_entries = []

    def create_matrix(self):
        """Создает поля для ввода матрицы"""
        try:
            n = int(self.n_entry.get())
            k = int(self.k_entry.get())

            if n <= 0 or k <= 0 or k >= n:
                raise ValueError("Должно быть: n > k > 0")

            self.clear_matrix()
            matrix_type = self.matrix_choice.get()

            # Определяем размеры матрицы
            if matrix_type == "G":
                rows, cols = k, n  # Матрица G: k x n
            else:  # matrix_type == "H"
                rows, cols = n-k, n  # Матрица H: (n-k) x n

            for i in range(rows):
                row_entries = []
                for j in range(cols):
                    entry = ttk.Entry(self.matrix_input_frame, width=3)
                    entry.grid(row=i, column=j, padx=2, pady=2)
                    entry.insert(0, "0")
                    row_entries.append(entry)
                self.matrix_entries.append(row_entries)

        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))

    def get_matrix(self):
        """Получает матрицу из полей ввода"""
        if not self.matrix_entries:
            raise ValueError("Сначала создайте матрицу")

        matrix = []
        for row in self.matrix_entries:
            matrix_row = []
            for entry in row:
                try:
                    value = int(entry.get())
                    if value not in [0, 1]:
                        raise ValueError
                    matrix_row.append(value)
                except ValueError:
                    raise ValueError("Матрица должна содержать только 0 и 1")
            matrix.append(np.array(matrix_row))
        return np.array(matrix)

    def encode_text(self):
        """Кодирует введенный текст с параметрами, заданными через интерфейс"""
        try:
            # Извлекаем текст для кодирования из текстового поля
            text = self.text_entry.get("1.0", tk.END).strip()
            if not text:
                messagebox.showwarning("Предупреждение", "Введите текст для кодирования")
                return

            if self.matrix_choice.get() == 'G': self.coder.set_matrix_G(self.get_matrix() )
            else: self.coder.set_matrix_H(self.get_matrix())
            self.coder.set_text(text)
            self.coder.encode_text()

            # Отображаем результаты
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, f"Исходный текст:\n{text}\n\n")
            self.output_text.insert(tk.END, f"Таблица кодов:\n")
            self.output_text.insert(tk.END, f"Ключ | Значение | Вес:\n")
            for key, value in self.coder.get_code_table().items():
                self.output_text.insert(tk.END, key + " | " + _array_to_string(value) + " | " + str(sum(value)) + "\n")
            self.output_text.insert(tk.END, f"ρ = {self.coder.get_count_mistakes()}\n\n")
            self.output_text.insert(tk.END, f"Закодированные блоки:\n")
            for i, block in enumerate(self.coder.get_encoded_text()):
                self.output_text.insert(tk.END, f"Блок {i + 1}: {_array_to_string(block)}\n")
            self.output_text.insert(tk.END, f"Закодированный текст:\n")
            self.output_text.insert(tk.END, self.coder.get_string_encoded_text())

        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка при кодировании: {str(e)}")

    def add_errors(self):
        """Добавляет ошибки в закодированные блоки"""
        if self.coder.get_encoded_text() is None:
            messagebox.showerror("Ошибка", "Сначала закодируйте текст")
            return

        if self.coder.get_count_mistakes() == 0:
            messagebox.showerror("Ошибка", "Код не может исправить ни одной ошибки")
            return

        self.coder.add_mistakes()

        self.output_text.insert(tk.END, f"\nБлоки с ошибками:\n")
        for i, block in enumerate(self.coder.get_encoded_text()):
            self.output_text.insert(tk.END, f"Блок {i+1}: {block}\n")
            # Показываем, где именно произошла ошибка

        self.output_text.insert(tk.END, f"\nТаблица синдромов:\n")
        self.output_text.insert(tk.END, f"c    | syndrome\n")
        for key, value in self.coder.get_syndromes().items():
            self.output_text.insert(tk.END, f"{key} | {value}\n")

    def decode_text(self):
        try:
            self.coder.solve_mistake()
            self.coder.decode_text()
            if self.matrix_choice.get() == 'G': self.coder.set_matrix_G(self.get_matrix())
            else: self.coder.set_matrix_H(self.get_matrix())

            if self.coder.get_decoded_text() is not None:
                self.output_text.insert(tk.END, f"\nДекодированный текст (в бинарном виде):\n{self.coder.get_string_decoded_text()}\n")
                self.output_text.insert(tk.END, f"\nДекодированный текст: {self.coder.decode_to_text()}\n")

                original_text = self.text_entry.get("1.0", tk.END).strip()
                if self.coder.decode_to_text() == original_text:
                    messagebox.showinfo("Успех", "Текст успешно декодирован!")
                else:
                    messagebox.showwarning("Внимание", "Декодированный текст отличается от исходного")
            else:
                messagebox.showerror("Ошибка", "Не удалось декодировать текст")

        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка при декодировании: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BlockCodeApp(root)
    root.mainloop()