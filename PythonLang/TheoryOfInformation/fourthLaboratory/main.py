import tkinter as tk
from tkinter import ttk, messagebox
from matrix_modifications import MatrixModifications
import numpy as np


class CodeModificationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Методы модификации помехоустойчивых кодов")
        self.matrix = MatrixModifications()

        # Переменные для хранения данных
        self.matrix_type = tk.StringVar(value="G")
        self.modification_type = tk.StringVar(value="Укорочение кода")
        self.rows = tk.IntVar(value=0)
        self.cols = tk.IntVar(value=0)
        self.entries = []  # Для хранения ячеек ввода матрицы

        # Создание интерфейса
        self.create_interface()

    def create_interface(self):
        # Ввод данных: размеры матрицы
        input_frame = tk.Frame(self.root, padx=10, pady=10)
        input_frame.pack(fill="x")

        tk.Label(input_frame, text="Размерность матрицы:").grid(row=0, column=0, sticky="w")

        tk.Label(input_frame, text="n:").grid(row=1, column=0, sticky="e")
        tk.Entry(input_frame, textvariable=self.rows, width=5).grid(row=1, column=1)

        tk.Label(input_frame, text="k:").grid(row=1, column=2, sticky="e")
        tk.Entry(input_frame, textvariable=self.cols, width=5).grid(row=1, column=3)

        # Выбор типа матрицы
        tk.Label(input_frame, text="Тип матрицы:").grid(row=2, column=0, sticky="w")
        matrix_type_menu = ttk.Combobox(input_frame, textvariable=self.matrix_type, values=["G", "H"], state="readonly")
        matrix_type_menu.grid(row=2, column=1, columnspan=2)
        matrix_type_menu.bind("<<ComboboxSelected>>", self.adjust_matrix_dimensions)

        # Кнопка для создания матрицы
        tk.Button(input_frame, text="Создать матрицу", command=self.create_matrix).grid(row=3, column=0, columnspan=4, pady=5)

        # Область для ввода матрицы
        self.matrix_frame = tk.Frame(self.root, padx=10, pady=10)
        self.matrix_frame.pack()

        # Выбор типа модификации
        modification_frame = tk.Frame(self.root, padx=10, pady=10)
        modification_frame.pack(fill="x")

        tk.Label(modification_frame, text="Модификация:").grid(row=0, column=0, sticky="w")
        modification_menu = ttk.Combobox(modification_frame, textvariable=self.modification_type,
                                         values=["Укорочение кода", "Расширение кода", "Перфорация линейных блочных кодов", "Пополнение кода", "Выбрасывание кодовых слов", "Удлинение кода"],
                                         state="readonly")
        modification_menu.grid(row=0, column=1, columnspan=2)

        # Кнопка для применения модификации
        tk.Button(modification_frame, text="Применить модификацию", command=self.apply_modification).grid(row=0, column=3, padx=5)

        # Область для вывода результатов
        result_frame = tk.Frame(self.root, padx=10, pady=10)
        result_frame.pack(fill="both", expand=True)

        tk.Label(result_frame, text="Результаты:").pack(anchor="w")

        self.result_text = tk.Text(result_frame, wrap="word", height=10, width=60)
        self.result_text.pack(fill="both", expand=True)

    def adjust_matrix_dimensions(self, event):
        """
        Обновляет значения колонок в зависимости от выбранного типа матрицы.
        """
        if self.matrix_type.get() == "H":
            n = self.rows.get()
            k = self.cols.get()
            if n > k:
                self.cols.set(n - k)

    def create_matrix(self):
        """
        Создаёт поле для ввода матрицы размером k x n и заполняет его нулями.
        """
        # Очистка предыдущей матрицы
        for widget in self.matrix_frame.winfo_children():
            widget.destroy()
        self.entries = []

        # Получаем размер матрицы (k x n)
        n = self.rows.get()
        k = self.cols.get()

        if n <= 0 or k <= 0:
            messagebox.showerror("Ошибка", "Размеры матрицы должны быть больше 0.")
            return

        # Создаём ячейки для ввода
        tk.Label(self.matrix_frame, text=f"Матрица {self.matrix_type.get()} ({k} x {n}):").grid(row=0, column=0,
                                                                                                columnspan=n)
        r = k if self.matrix_type.get() == "G" else n - k
        for i in range(r):  # k строк
            row_entries = []
            for j in range(n):  # n столбцов
                entry = tk.Entry(self.matrix_frame, width=3, justify="center")
                entry.insert(0, "0")  # Заполняем ячейку нулём
                entry.grid(row=i + 1, column=j)
                row_entries.append(entry)
            self.entries.append(row_entries)

    def apply_modification(self):
        """
        Применяет выбранную модификацию к матрице.
        """
        modification = self.modification_type.get()
        n = self.rows.get()
        k = self.cols.get()

        if n <= 0 or k <= 0:
            messagebox.showerror("Ошибка", "Введите корректные размеры матрицы.")
            return

        if self.matrix_type.get() == "G": self.matrix.set_matrix_G(self.get_matrix())
        else: self.matrix.set_matrix_H(self.get_matrix())

        # Пример модификации (заглушка)
        if modification == "Укорочение кода":
            self.matrix.shortening_code()  # Удаляем последний столбец как пример
        elif modification == "Расширение кода":
            self.matrix.extension_code()
        elif modification == "Перфорация линейных блочных кодов":
            self.matrix.punching_code()
        elif modification == "Пополнение кода":
            self.matrix.add_code()
        elif modification == "Выбрасывание кодовых слов":
            self.matrix.ejecting_code()
        elif modification == "Удлинение кода":
            self.matrix.prolongation_code()

        # Вывод результатов
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, f"Выбранная модификация: {modification}\n")
        self.result_text.insert(tk.END, f"Результат:\n{self.matrix.get_modified_matrix()}\n\n")
        self.result_text.insert(tk.END, f"dmin до:\n{self.matrix.get_dmin()}\n\n")
        self.result_text.insert(tk.END, f"dmin после:\n{self.matrix.get_dmin_modified()}\n\n")

    def get_matrix(self):
        """
        Считывает введённую пользователем матрицу и возвращает её как NumPy массив.
        """
        matrix = []
        for row in self.entries:  # Проходим по строкам
            row_data = [int(entry.get() or 0) for entry in row]  # Считываем каждое значение
            matrix.append(row_data)

        return np.array(matrix)


# Запуск программы
if __name__ == "__main__":
    root = tk.Tk()
    app = CodeModificationApp(root)
    root.mainloop()
