import tkinter as tk
import random
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import numpy as np
from CascadeCoding import CascadeCoder, bit_array_to_image, image_to_bit_array  # Убедись, что этот модуль доступен

class CascadeCoderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Каскадное кодирование изображения")

        self.cc = CascadeCoder()

        self.matrix_frame = tk.Frame(root)
        self.matrix_frame.pack(pady=5)

        self.controls_frame = tk.Frame(root)
        self.controls_frame.pack(pady=5)

        self.image_label = tk.Label(root)
        self.image_label.pack(pady=5)

        self.result_label = tk.Label(root)
        self.result_label.pack(pady=5)

        # Размер матрицы
        tk.Label(self.controls_frame, text="Размер матрицы G (n x m):").grid(row=0, column=0)
        self.n_entry = tk.Entry(self.controls_frame, width=5)
        self.n_entry.grid(row=0, column=1)
        self.m_entry = tk.Entry(self.controls_frame, width=5)
        self.m_entry.grid(row=0, column=2)
        self.create_matrix_btn = tk.Button(self.controls_frame, text="Задать матрицу", command=self.create_matrix_fields)
        self.create_matrix_btn.grid(row=0, column=3)

        # Сумматоры
        tk.Label(self.controls_frame, text="Кол-во сумматоров:").grid(row=1, column=0)
        self.adders_count_entry = tk.Entry(self.controls_frame, width=5)
        self.adders_count_entry.grid(row=1, column=1)
        self.adders_btn = tk.Button(self.controls_frame, text="Задать сумматоры", command=self.create_adders_fields)
        self.adders_btn.grid(row=1, column=2)

        self.adders_entries = []

        # Кнопки
        tk.Button(self.controls_frame, text="Загрузить изображение", command=self.load_image).grid(row=2, column=0)
        tk.Button(self.controls_frame, text="Закодировать", command=self.encode_image).grid(row=2, column=1)
        tk.Button(self.controls_frame, text="Добавить ошибки", command=self.add_errors).grid(row=2, column=2)
        tk.Button(self.controls_frame, text="Декодировать", command=self.decode_image).grid(row=2, column=3)

        # Вывод битов после кодирования
        self.bit_output_label = tk.Label(self.controls_frame, text="Биты после кодирования:")
        self.bit_output_label.grid(row=3, column=0, columnspan=4)

        self.bit_output_text = tk.Text(self.controls_frame, height=5, width=50)
        self.bit_output_text.grid(row=4, column=0, columnspan=4, pady=5)

        # Ввод индексов для изменения битов
        self.error_indexes_label = tk.Label(self.controls_frame, text="Индексы для изменения битов (через запятую):")
        self.error_indexes_label.grid(row=5, column=0, columnspan=4)

        self.error_indexes_entry = tk.Entry(self.controls_frame, width=50)
        self.error_indexes_entry.grid(row=6, column=0, columnspan=4)

    def create_matrix_fields(self):
        for widget in self.matrix_frame.winfo_children():
            widget.destroy()
        self.n = int(self.n_entry.get())
        self.m = int(self.m_entry.get())
        self.matrix_entries = []

        for i in range(self.n):
            row_entries = []
            for j in range(self.m):
                entry = tk.Entry(self.matrix_frame, width=3)
                entry.grid(row=i, column=j)
                row_entries.append(entry)
            self.matrix_entries.append(row_entries)

    def create_adders_fields(self):
        for entry in self.adders_entries:
            entry.destroy()
        self.adders_entries = []

        count = int(self.adders_count_entry.get())
        for i in range(count):
            label = tk.Label(self.controls_frame, text=f"Сумматор {i+1} (через запятую):")
            label.grid(row=7 + i, column=0)
            entry = tk.Entry(self.controls_frame, width=20)
            entry.grid(row=7 + i, column=1, columnspan=3, sticky='we')
            self.adders_entries.append(entry)

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Images", "*.jpg *.png *.bmp")])
        if file_path:
            self.image = Image.open(file_path).convert("RGB")
            pixels = list(self.image.getdata())
            corrupted_pixels = []

            for r, g, b in pixels:
                # Выбираем случайный канал
                channel = random.choice(['r', 'g', 'b'])
                if channel == 'r':
                    bit_index = random.randint(0, 7)
                    r ^= 1 << bit_index
                elif channel == 'g':
                    bit_index = random.randint(0, 7)
                    g ^= 1 << bit_index
                else:
                    bit_index = random.randint(0, 7)
                    b ^= 1 << bit_index
                corrupted_pixels.append((r % 256, g % 256, b % 256))

            # Обновляем изображение
            bad_image = Image.new("RGB", (self.image.width, self.image.height))
            bad_image.putdata(corrupted_pixels)
            self.display_image(bad_image, self.image_label)
            self.cc.set_size(self.image.size)

    def display_image(self, image, label):
        resized_image = image.resize((300, 300))
        tk_image = ImageTk.PhotoImage(resized_image)
        label.configure(image=tk_image)
        label.image = tk_image

    def get_matrix_G(self):
        G = np.zeros((self.n, self.m), dtype=int)
        for i in range(self.n):
            for j in range(self.m):
                val = self.matrix_entries[i][j].get()
                G[i, j] = int(val)
        return G

    def get_adders(self):
        adders = []
        for entry in self.adders_entries:
            try:
                indices = list(map(int, entry.get().split(',')))
                adders.append(indices)
            except ValueError:
                messagebox.showerror("Ошибка", "Ошибка в формате ввода сумматора.")
                return []
        return adders

    def encode_image(self):
        try:
            image_bits = image_to_bit_array(self.image)
            G = self.get_matrix_G()
            adders = self.get_adders()

            self.cc.set_matrix_G(G)
            self.cc.set_adders(adders)
            self.cc.set_image_bits_to_encode(image_bits)
            self.cc.encode()

            self.bit_output_text.delete(1.0, tk.END)  # Очищаем поле
            self.bit_output_text.insert(tk.END, self.cc.encoded_sequence[0:300])  # Вставляем биты

        except Exception as e:
            messagebox.showerror("Ошибка при кодировании", str(e))

    def add_errors(self):
        try:
            # Получаем индексы для изменения битов
            error_indexes_input = self.error_indexes_entry.get()
            if error_indexes_input:
                error_indexes = list(map(int, error_indexes_input.split(',')))

            s = list(self.cc.encoded_sequence)
            for error_index in error_indexes:
                if s[error_index] == '0':
                    s[error_index] = '1'
                else:
                    s[error_index] = '0'
            self.cc.encoded_sequence = ''.join(s)

            # Обновляем биты в текстовом поле
            self.bit_output_text.delete(1.0, tk.END)  # Очищаем поле
            self.bit_output_text.insert(tk.END, self.cc.encoded_sequence[0:300])

        except Exception as e:
            messagebox.showerror("Ошибка при добавлении ошибок", str(e))

    def decode_image(self):
        try:
            self.cc.decode()
            decoded_image = bit_array_to_image(self.cc.decoded_bits, self.image.size)

            # Отображаем восстановленное изображение
            self.display_image(decoded_image, self.result_label)

        except Exception as e:
            messagebox.showerror("Ошибка при декодировании", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = CascadeCoderApp(root)
    root.mainloop()
