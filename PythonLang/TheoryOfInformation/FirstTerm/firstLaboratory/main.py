import tkinter as tk
from tkinter import filedialog
from collections import Counter
import math
import os
from docx import Document
import PyPDF2


def read_docx(file_path):
    doc = Document(file_path)
    text = []
    for paragraph in doc.paragraphs:
        text.append(paragraph.text)
    return '\n'.join(text)


def read_pdf(file_path):
    text = []
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text.append(page.extract_text())
    return '\n'.join(text)


class TextAnalyzer:
    def __init__(self, master):
        self.master = master
        self.master.title("Энтропия файлов")

        self.label = tk.Label(master, text="Выберите файл для анализа:")
        self.label.pack(pady=10)

        self.select_button = tk.Button(master, text="Выбрать файл", command=self.load_file)
        self.select_button.pack(pady=5)

        self.analyze_button = tk.Button(master, text="Анализировать", command=self.analyze_file, state=tk.DISABLED)
        self.analyze_button.pack(pady=5)

        self.file_path = ""
        self.file_data = None

        self.canvas_frame = tk.Frame(master)
        self.canvas_frame.pack(expand=True, fill=tk.BOTH)

        self.canvas = tk.Canvas(self.canvas_frame, width=1000, height=500)
        self.canvas.pack(pady=20, expand=True, fill=tk.BOTH)

    def load_file(self):
        self.file_path = filedialog.askopenfilename(title="Выберите файл",
                                                    filetypes=[("All files", "*.*")])
        if self.file_path:
            with open(self.file_path, 'rb') as file:
                self.file_data = file.read()
            self.analyze_button.config(state=tk.NORMAL)

    def analyze_file(self):
        file_extension = os.path.splitext(self.file_path)[1].lower()

        # Сначала подсчитываем энтропию бит файла
        entropy_bits = self.calculate_entropy(self.file_data)

        # Переменные для энтропии текста и текста
        entropy_text = 0.0
        text_data = ""

        # Если файл текстовый, считаем также энтропию текста
        if file_extension in ['.txt', '.docx', '.pdf']:
            if file_extension == '.txt':
                text_data = self.file_data.decode('utf-8', errors='ignore')
            elif file_extension == '.docx':
                text_data = read_docx(self.file_path)
            elif file_extension == '.pdf':
                text_data = read_pdf(self.file_path)

            entropy_text = self.calculate_entropy(text_data.encode('utf-8'))

            # Строим гистограмму для текста
            self.plot_histogram(text_data)

        # Стриом гистограмму для бит
        self.plot_histogram(self.file_data, is_binary=True)

        # Отображение энтропии текста и бит
        self.display_entropy(entropy_text, entropy_bits)

    def calculate_entropy(self, data):
        char_counts = Counter(data)
        total_chars = len(data)
        entropy = -sum((count / total_chars) * math.log2(count / total_chars) for count in char_counts.values())
        return entropy

    def plot_histogram(self, data, is_binary=False):
        self.canvas.delete("all")
        char_counts = Counter(data)

        if is_binary:
            most_common = char_counts.most_common(10)
            chars, counts = zip(*most_common)
        else:
            # Для текстовых файлов
            clean_text = ''.join(c for c in data if c.isalnum() or c.isspace())
            char_counts = Counter(clean_text)
            most_common = char_counts.most_common(10)
            chars, counts = zip(*most_common)

        max_count = max(counts)
        canvas_height = 500
        bar_width = 30
        padding = 10

        self.canvas.create_line(120, 450, 120, 10, arrow=tk.LAST, fill="white")
        self.canvas.create_line(120, 450, 760, 450, arrow=tk.LAST, fill="white")

        for i in range(0, max_count + 1, max(1, max_count // 10)):
            y_position = 450 - (i / max_count) * canvas_height * 0.8
            self.canvas.create_text(100, y_position, text=str(i), anchor=tk.E, fill="white")

        self.canvas.create_text(50, 225, text="Количество повторений", anchor=tk.W, fill="white", angle=90)
        self.canvas.create_text(275, 495, text="Символы" if not is_binary else "Байты", anchor=tk.S, fill="white")

        for i, (char, count) in enumerate(zip(chars, counts)):
            bar_height = 0.8 * (count / max_count) * canvas_height

            x0 = 130 + i * (bar_width + padding)
            y0 = 450 - bar_height
            x1 = x0 + bar_width
            y1 = 450

            self.canvas.create_rectangle(x0, y0, x1, y1, fill="cyan")
            self.canvas.create_text((x0 + x1) / 2, 470, text=repr(char), fill="white")

    def display_entropy(self, entropy_text, entropy_bits):
        # Отображаем энтропию текста и бит
        self.canvas.create_text(800, 150, text="Энтропия текста: ", anchor=tk.S, fill="white")
        self.canvas.create_text(800, 180, text=str(entropy_text), anchor=tk.S, fill="white")
        self.canvas.create_text(800, 210, text="Энтропия бит: ", anchor=tk.S, fill="white")
        self.canvas.create_text(800, 240, text=str(entropy_bits), anchor=tk.S, fill="white")


if __name__ == "__main__":
    root = tk.Tk()
    app = TextAnalyzer(root)
    root.mainloop()
