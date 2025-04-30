import random
from typing import Sequence, Sized
import numpy as np


class CyclicCoder:
    def __init__(self, generator_poly=None, generator_matrix=None):
        if generator_poly:
            self.generator_poly = np.array(generator_poly, dtype=int)
        elif generator_matrix is not None:
            self.generator_matrix = np.array(generator_matrix, dtype=int)
            self.k, self.n = self.generator_matrix.shape
            self.generator_poly = self.matrix_to_poly(self.generator_matrix)
        else:
            raise ValueError("Нужно ввести либо полином, либо матрицу.")

        self.k = None
        self.n = None

    def poly_degree(self, poly: Sized) -> int:
        return len(poly) - 1

    def poly_div(self, dividend, divisor):
        dividend = dividend.copy()
        divisor = np.trim_zeros(divisor, 'f')
        while len(dividend) >= len(divisor):
            if dividend[0] == 1:
                for i in range(len(divisor)):
                    dividend[i] ^= divisor[i]
            dividend = dividend[1:]
        return dividend

    def encode_polynomial(self, message_bits):
        self.k = len(message_bits)
        r = self.poly_degree(self.generator_poly)
        self.n = self.k + r

        padded = np.append(message_bits, np.zeros(r, dtype=int))
        remainder = self.poly_div(padded.tolist(), self.generator_poly)

        remainder = np.array(remainder, dtype=int)
        if len(remainder) < r:
            remainder = np.concatenate((np.zeros(r - len(remainder), dtype=int), remainder))

        codeword = np.append(message_bits, remainder)
        return codeword.astype(int)

    def matrix_to_poly(self, G):
        first_row = G[0]
        idx = np.argmax(first_row)
        return first_row[idx:].tolist()

    def text_to_bits(self, text: str) -> Sequence[int]:
        return [int(bit) for char in text.encode('utf-8') for bit in format(char, '08b')]

    def bits_to_text(self, bits: Sequence[str]) -> bytes | str:
        chars = [bits[i:i + 8] for i in range(0, len(bits), 8)]
        bytes_list = [int(''.join(map(str, b)), 2) for b in chars if len(b) == 8]
        print(""" Полученное информационное слово """)
        print(chars)
        try:
            return bytes(bytes_list).decode('utf-8')
        except UnicodeDecodeError:
            return "<декодирование не удалось>"

    def encode_text(self, text):
        bitstream = self.text_to_bits(text)
        self.k = 4  # фиксированный размер блока
        blocks = [bitstream[i:i + self.k] for i in range(0, len(bitstream), self.k)]
        if len(blocks[-1]) < self.k:
            blocks[-1] += [0] * (self.k - len(blocks[-1]))

        encoded = []
        for block in blocks:
            encoded_block = self.encode_polynomial(block)
            encoded.extend(encoded_block)
        return encoded

    def decode_to_text_megitt(self, encoded):
        blocks = [encoded[i:i + self.n] for i in range(0, len(encoded), self.n)]
        corrected = []
        syndromes = []

        for block in blocks:
            syndrome = self.poly_div(block.copy(), self.generator_poly)
            syndromes.append(syndrome)

            if sum(syndrome) == 0:
                corrected_block = block
            else:
                for i in range(len(block)):
                    temp = block.copy()
                    temp[i] ^= 1
                    if sum(self.poly_div(temp.copy(), self.generator_poly)) == 0:
                        print(f'В блоке {block}. Ошибка была в символе {i + 1}')
                        block = temp
                        print(f'Исправленный блок {block}')
                        break
                corrected_block = block
            corrected.extend(corrected_block[:self.k])
        print(""" Таблица синдромов """)
        for s in syndromes:
            if sum(s) == 0:
                print('Ошибок нет')
            else:
                print(f'Полученный синдром {s}')
        return self.bits_to_text(corrected)

    def add_manual_errors(self, encoded, positions):
        corrupted = encoded.copy()
        for pos in positions:
            if 0 <= pos < len(corrupted):
                corrupted[pos] ^= 1
        return corrupted

    def add_random_errors(self, encoded, count=1):
        corrupted = encoded.copy()
        positions = random.sample(range(len(encoded)), count)
        for pos in positions:
            corrupted[pos] ^= 1
        return corrupted, positions
