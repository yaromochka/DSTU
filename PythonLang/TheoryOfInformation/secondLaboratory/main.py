import csv
import tkinter as tk
from tkinter import filedialog, messagebox
import heapq
import os
from collections import Counter

# Алгоритм Хаффмана
class HuffmanNode:
    def __init__(self, symbol, frequency):
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency

def build_huffman_tree(frequency):
    heap = [HuffmanNode(symbol, freq) for symbol, freq in frequency.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.frequency + right.frequency)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    return heap[0]

def build_huffman_codes(node, code="", codes={}):
    if node is not None:
        if node.symbol is not None:
            codes[node.symbol] = code
        build_huffman_codes(node.left, code + "0", codes)
        build_huffman_codes(node.right, code + "1", codes)
    return codes

def huffman_encode(text):
    frequency = Counter(text)
    tree = build_huffman_tree(frequency)
    codes = build_huffman_codes(tree)
    encoded_text = ''.join(codes[symbol] for symbol in text)
    return codes, encoded_text

def huffman_decode(encoded_text, codes):
    reverse_codes = {v: k for k, v in codes.items()}
    current_code = ""
    decoded_text = ""
    for bit in encoded_text:
        current_code += bit
        if current_code in reverse_codes:
            decoded_text += reverse_codes[current_code]
            current_code = ""
    return decoded_text

# Алгоритм LZ78
def lz78_encode(text):
    dictionary = {}
    for i in range(256):
        dictionary[chr(i)] = 0
    next_code = 1
    result = []
    current_string = ""
    for char in text:
        current_string += char
        if current_string not in dictionary:
            if current_string[:-1]:
                result.append((dictionary[current_string[:-1]], current_string[-1]))
            else:
                result.append((0, current_string))
            dictionary[current_string] = next_code
            next_code += 1
            current_string = ""
    if current_string:
        result.append((dictionary[current_string], ""))
    return result

# Алгоритм LZW
def lzw_encode(text):
    dictionary = {chr(i): i for i in range(256)}
    next_code = 256
    result = []
    current_string = ""
    for char in text:
        current_string += char
        if current_string not in dictionary:
            if current_string[:-1] in dictionary:
                result.append(dictionary[current_string[:-1]])
            dictionary[current_string] = next_code
            next_code += 1
            current_string = char
    if current_string:
        result.append(dictionary[current_string])
    return dictionary, result


# Интерфейс
class CompressionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Сжатие данных")

        self.file_path = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Выберите файл:").pack()
        tk.Entry(self.root, textvariable=self.file_path, width=50).pack()
        tk.Button(self.root, text="Выбрать файл", command=self.browse_file).pack()

        tk.Button(self.root, text="Кодировать Хаффманом", command=self.huffman_encode_file).pack()
        tk.Button(self.root, text="Декодировать Хаффманом", command=self.huffman_decode_file).pack()
        tk.Button(self.root, text="Кодировать LZ78", command=self.lz78_encode_file).pack()
        tk.Button(self.root, text="Кодировать LZW", command=self.lzw_encode_file).pack()

    def browse_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.file_path.set(file_path)

    def huffman_encode_file(self):
        file_path = self.file_path.get()
        if not file_path:
            messagebox.showerror("Ошибка", "Выберите файл")
            return

        with open(file_path, 'r') as file:
            text = file.read()

        codes, encoded_text = huffman_encode(text)

        with open('Haffman_encoded.txt', 'w') as file:
            file.write(encoded_text)

        with open('Haffman_table.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Symbol', 'Code'])
            for symbol, code in codes.items():
                writer.writerow([symbol, code])

        messagebox.showinfo("Успех", "Файл закодирован алгоритмом Хаффмана")

    def huffman_decode_file(self):
        file_path = 'Haffman_encoded.txt'
        if not os.path.exists(file_path):
            messagebox.showerror("Ошибка", "Файл 'Haffman_encoded.txt' не найден")
            return

        with open(file_path, 'r') as file:
            encoded_text = file.read()

        codes = {}
        with open('Haffman_table.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                codes[row['Symbol']] = row['Code']

        decoded_text = huffman_decode(encoded_text, codes)

        with open('Haffman_decoded.txt', 'w') as file:
            file.write(decoded_text)

        messagebox.showinfo("Успех", "Файл декодирован алгоритмом Хаффмана")

    def lz78_encode_file(self):
        file_path = self.file_path.get()
        if not file_path:
            messagebox.showerror("Ошибка", "Выберите файл")
            return

        with open(file_path, 'r') as file:
            text = file.read()

        encoded_text = lz78_encode(text)

        with open('LZ78_encoded.txt', 'w') as file:
            file.write(str(encoded_text))

        messagebox.showinfo("Успех", "Файл закодирован алгоритмом LZ78")

    def lzw_encode_file(self):
        file_path = self.file_path.get()
        if not file_path:
            messagebox.showerror("Ошибка", "Выберите файл")
            return

        with open(file_path, 'r') as file:
            text = file.read()

        dictionary, encoded_text = lzw_encode(text)

        with open('LZW_encoded.txt', 'w') as file:
            file.write(str(encoded_text))

        with open('LZW_table.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Symbol', 'Code'])
            for symbol, code in dictionary.items():
                writer.writerow([symbol, code])

        messagebox.showinfo("Успех", "Файл закодирован алгоритмом LZW")


if __name__ == "__main__":
    root = tk.Tk()
    app = CompressionApp(root)
    root.mainloop()
