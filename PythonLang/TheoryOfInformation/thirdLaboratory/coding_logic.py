import itertools
from typing import Generator

import numpy as np
from random import randint

def _array_to_string(array: np.array) -> str:
    return ''.join([str(num) for num in list(array)])

def _add_to_text(k: int, binary_text: str) -> str:
    if all([symbol in '01' for symbol in binary_text]):
        while len(binary_text) % k != 0:
            binary_text = '0' + binary_text
    return binary_text

def _separate_text(binary_text: str, separate_num: int) -> Generator[np.array, None, None]:
    if all([symbol in '01' for symbol in binary_text]):
        for i in range(0, len(binary_text), separate_num):
            yield np.array(list(binary_text[i:i + separate_num]))

def _to_sys_matrix(matrix: np.array, matrix_type="G") -> np.array:
    """
    Создает систематическую матрицу на основе типа.
    """
    sys_matrix = None
    rows, cols = matrix.shape
    columns_to_delete = [i for i in range(cols) if np.sum(matrix[:, i] == 1) == 1]
    matrix_reduced = np.delete(matrix, columns_to_delete, axis=1)
    identity_matrix = np.eye(rows, dtype=int)

    if matrix_type == "G":
        sys_matrix = np.hstack((identity_matrix, matrix_reduced)).tolist()
    elif matrix_type == "H":
        sys_matrix = np.hstack((matrix_reduced, identity_matrix)).tolist()
    return sys_matrix if sys_matrix is None else np.zeros((rows, cols), dtype=int)


class BlockCoder:
    def __init__(self):
        self._matrix_G = None
        self._matrix_H = None
        self._text = None
        self._n = None
        self._k = None
        self._count_mistakes = None
        self._encoded_text = None
        self._decoded_text = None
        # Словарь (таблица) для хранения кодовых слов
        # и обратная таблица для декодирования
        self._code_table = {}
        self._decode_table = {}
        # Словарь для хранения таблицы синдромов
        self._syndromes = {}


    """
    Геттеры и сеттеры для добавления
    текста, матрицы и типа матрицы,
    а также получения этих данных для
    дальнейшего использования
    """
    def set_text(self, message) -> None:
        self._text = message

    def get_text(self) -> str:
        return self._text

    def get_code_table(self) -> dict:
        return self._code_table

    def get_syndromes(self) -> dict:
        return self._syndromes

    def set_decoded_text(self, decode_text):
        self._decoded_text = decode_text

    def get_decoded_text(self) -> str:
        return self._decoded_text

    def set_encoded_text(self, encode_text) -> None:
        self._encoded_text = encode_text

    def get_encoded_text(self) -> str:
        return self._encoded_text

    def set_count_mistakes(self, count_mistakes) -> None:
        self._count_mistakes = count_mistakes

    def get_count_mistakes(self) -> int:
        return self._count_mistakes

    def get_matrix_G(self) -> np.array:
        return self._matrix_G

    def set_matrix_G(self, matrix: np.array) -> None:
        _to_sys_matrix(matrix, matrix_type="G")
        self._matrix_G = matrix
        self.__get_H_from_G()
        self.__fill_info()

    def get_matrix_H(self) -> np.array:
        return self._matrix_H

    def set_matrix_H(self, matrix: np.array) -> None:
        _to_sys_matrix(matrix, matrix_type="H")
        self._matrix_H = matrix
        self.__get_G_from_H()
        self.__fill_info()

    """ 
        Одна из основных функций.
        Заполняет все необходимые для вычислений данные/таблицы
        в зависимости от матрицы G.
        Запускается сразу после того, как в класс передаётся
        матрица G либо H. 
    """
    def __fill_info(self) -> None:
        self._n = self._matrix_G.shape[1]
        self._k = self._matrix_G.shape[0]
        self.__fill_code_table()
        self.__count_correction()
        self.__fill_syndromes()

    def __fill_code_table(self) -> None:
        for idx in range(2 ** self._k):
            i = format(idx, f'0{self._k}b')
            c = (np.array(list(map(int, i))).tolist() @ self._matrix_G) % 2
            self._code_table[i] = c
        self._decode_table = {''.join(list(v.astype(str))): k for k, v in self._code_table.items()}

    def __fill_syndromes(self) -> None:
        self._syndromes['0' * (self._k + 1)] = np.array(list(str(i) for i in '0' * self._n), dtype=int)
        for num_errors in range(1, self._count_mistakes + 1):  # От 1 до количества ошибок
            for error_positions in itertools.combinations(range(self._n), num_errors):
                # Создаем вектор ошибки
                error_vector = np.zeros(self._n, dtype=int)
                for pos in error_positions:
                    error_vector[pos] = 1
                self._syndromes[_array_to_string(error_vector @ self._matrix_H.T)] = error_vector

    """
    Приватные вспомогательные методы
    Их названия описывают то, что они делают
    """
    def __get_H_from_G(self):
        n, k = self._matrix_G.shape[1], self._matrix_G.shape[0]
        self._matrix_H = np.concatenate([self._matrix_G[:, (n - k - 1):].T, np.identity(k + 1).astype(int)], axis=1)

    def __get_G_from_H(self):
        n, k = self._matrix_H.shape[1], self._matrix_H.shape[0]
        self._matrix_G = np.concatenate([np.identity(n - k).astype(int), self._matrix_H[:, :(n - k)].T], axis=1)

    # Добавление нулей спереди,
    # чтобы блоки можно было разбить
    # на k символов
    def __added(self) -> None:
        self._text = _add_to_text(self._k, self._text)

    # Перевод текста в бинарную строку
    def __text_to_bin(self) -> None:
        if all([symbol.isalpha for symbol in self._text]):
            self._text = ''.join([format(ord(symbol), '016b') for symbol in self._text])


    def __count_correction(self) -> None:
        min_weight = float('inf')
        for value in self._code_table.values():
            weight = sum(value)
            if weight > 0:
                min_weight = min(weight, min_weight)
        self._count_mistakes = (min_weight - 1) // 2

    def get_string_encoded_text(self) -> str:
        return ''.join(_array_to_string(i) for i in self._encoded_text)

    def get_string_decoded_text(self) -> str:
        return ''.join(''.join(i) for i in self._decoded_text)


    """ 
     Блок для перевода текста
     в закодированную бинарную последовательность.
     Текст разделяется на блоки по k символов
     и каждый блок отправляется на кодировку.
     Врзвращаемым значением является последовательность блоков
     с добавочными символами
     """
    def encode_text(self) -> None:
        self.__text_to_bin()
        self.__added()
        blocks = np.array(list(_separate_text(self._text, self._k)))
        self._encoded_text = list(self.__encode_blocks(blocks))

    def __encode_blocks(self, blocks: np.array) -> []:
        for block in blocks:
            yield list(self.__encode(block))

    def __encode(self, binary_block) -> np.array:
        return self._code_table[''.join(binary_block)]


    """ 
        Блок для добавления ошибок в 
        закодированную последовательность бит.
        А также для последующего исправления
        этих ошибок
    """
    def add_mistakes(self):
        if self._encoded_text is not None and self._count_mistakes > 0:
            for block in self._encoded_text:
                # Добавление ошибки с вероятностью 0.5
                chance = randint(0, 1)
                if chance == 1:
                    for _ in range(self._count_mistakes):
                        block[randint(0, len(block) - 1)] ^= 1

    def solve_mistake(self):
        if self._encoded_text is not None and self._count_mistakes > 0:
            for idx, block in enumerate(self._encoded_text):
                mistake = (block @ self._matrix_H.T) % 2
                self._encoded_text[idx] = np.array(block) ^ self._syndromes[_array_to_string(mistake)]

    """
        Блок для декодирования текста
        обратно в последовательность бит, а после
        разбиение на n элементов и перевод
        обратно в символы (в соответствии с 
        таблицой ASCII)
    """
    def decode_text(self) -> None:
        blocks = np.array(list(_separate_text(self.get_string_encoded_text(), self._n)))
        self._decoded_text = list(self.__decode_blocks(blocks))

    def __decode_blocks(self, blocks: np.array) -> []:
        for block in blocks:
            yield list(self.__decode(block))

    def __decode(self, binary_block) -> np.array:
        return self._decode_table[''.join(binary_block)]

    """
    Метод для перевода бинарного декодированного текста в 
    символьный декодированный текст
    """
    def decode_to_text(self) -> str:
        text = self.get_string_decoded_text()
        decoded_text = ''
        if self._decoded_text is not None:
            for i in range(len(text), 0, -16):
                temp_bin_code = text[max(0, i-16):i]
                if len(temp_bin_code) == 16: decoded_text += chr(int(temp_bin_code, 2))
                else: break
        return decoded_text[::-1]