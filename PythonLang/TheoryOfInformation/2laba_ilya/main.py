import tkinter as tk
from tkinter import messagebox
import numpy as np
import random

def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

def binary_to_text(binary_str):
    binary_values = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
    return ''.join(chr(int(binary_value, 2)) for binary_value in binary_values)

def generate_random_error(block, n):
    error_position = random.randint(0, n-1)
    block[error_position] = 1 - block[error_position]
    return block

def encode_block(block, G):
    return np.dot(block, G) % 2

def decode_block(block, H):
    syndrome = np.dot(block, H.T) % 2
    error_vector = syndrome_table.get(tuple(syndrome), np.zeros(len(syndrome)))
    corrected_block = (block + error_vector) % 2
    return corrected_block[:k]

def on_encode():
    global G, H, syndrome_table, k, n, dmin
    text = text_entry.get()
    binary_str = text_to_binary(text)
    print(f"Binary string: {binary_str}")

    # Разбиваем бинарную строку на блоки длиной k
    blocks = [binary_str[i:i+k] for i in range(0, len(binary_str), k)]
    encoded_blocks = []

    for block in blocks:
        block = [int(bit) for bit in block]
        encoded_block = encode_block(block, G)
        encoded_block = generate_random_error(encoded_block, n)
        encoded_blocks.append(encoded_block)

    encoded_binary_str = ''.join(''.join(str(bit) for bit in block) for block in encoded_blocks)
    print(f"Encoded binary string: {encoded_binary_str}")

    decoded_blocks = []
    for encoded_block in encoded_blocks:
        decoded_block = decode_block(encoded_block, H)
        decoded_blocks.append(decoded_block)

    decoded_binary_str = ''.join(''.join(str(bit) for bit in block) for block in decoded_blocks)
    print(f"Decoded binary string: {decoded_binary_str}")

    decoded_text = binary_to_text(decoded_binary_str)
    print(f"Decoded text: {decoded_text}")

    result_label.config(text=f"Decoded text: {decoded_text}")

def on_set_matrix():
    global G, H, syndrome_table, k, n, dmin
    try:
        G_str = G_entry.get()
        H_str = H_entry.get()

        G = np.array([list(map(int, row.split())) for row in G_str.split(';')])
        H = np.array([list(map(int, row.split())) for row in H_str.split(';')])

        k = G.shape[0]
        n = G.shape[1]
        dmin = 3  # Минимальное расстояние Хемминга (можно изменить)

        # Создаем таблицу синдромов
        syndrome_table = {}
        for i in range(2**(n-k)):
            error_vector = np.array(list(map(int, format(i, f'0{n-k}b'))))
            syndrome = np.dot(error_vector, H.T) % 2
            syndrome_table[tuple(syndrome)] = error_vector

        print(f"G matrix:\n{G}")
        print(f"H matrix:\n{H}")
        print(f"Syndrome table:\n{syndrome_table}")
        print(f"Parameters: n={n}, k={k}, dmin={dmin}")

        messagebox.showinfo("Success", "Matrices set successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Создаем графический интерфейс
root = tk.Tk()
root.title("Error-Correcting Code Encoder/Decoder")

text_label = tk.Label(root, text="Enter text:")
text_label.pack()

text_entry = tk.Entry(root, width=50)
text_entry.pack()

G_label = tk.Label(root, text="Enter G matrix (rows separated by ';', elements by space):")
G_label.pack()

G_entry = tk.Entry(root, width=50)
G_entry.pack()

H_label = tk.Label(root, text="Enter H matrix (rows separated by ';', elements by space):")
H_label.pack()

H_entry = tk.Entry(root, width=50)
H_entry.pack()

set_matrix_button = tk.Button(root, text="Set Matrices", command=on_set_matrix)
set_matrix_button.pack()

encode_button = tk.Button(root, text="Encode/Decode", command=on_encode)
encode_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()