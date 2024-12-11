import itertools

import numpy as np

def _array_to_string(array: np.array) -> str:
    return ''.join([str(num) for num in list(array)])

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

class Matrix:
    def __init__(self):
        self._matrix = None
        self._n = None
        self._k = None
        self._count_mistakes = None
        self._dmin = None
        # Словарь (таблица) для хранения кодовых слов
        # и обратная таблица для декодирования
        self._code_table = {}
        self._decode_table = {}
        # Словарь для хранения таблицы синдромов
        self._syndromes = {}

    def get_count_mistakes(self) -> int:
        return self._count_mistakes

    def set_matrix(self, matrix: np.array):
        self._matrix = matrix
        self._n = matrix.shape[1]
        self._k = matrix.shape[0]

    def get_dmin(self):
        return self._dmin

    def get_matrix(self):
        return self._matrix

    def get_n(self) -> int:
        return self._n

    def get_k(self) -> int:
        return self._k

    def fill_info(self):
        self.__make_code_table()
        self.__count_correction()
        self.__make_syndromes()

    def __make_code_table(self):
        for idx in range(2 ** self._k):
            i = format(idx, f'0{self._k}b')
            c = (np.array(list(map(int, i))).tolist() @ self._matrix) % 2
            self._code_table[i] = c
        self._decode_table = {''.join(list(v.astype(str))): k for k, v in self._code_table.items()}

    def __make_syndromes(self):
        self._syndromes['0' * (self._k + 1)] = np.array(list(str(i) for i in '0' * self._n), dtype=int)
        for num_errors in range(1, self._count_mistakes + 1):  # От 1 до количества ошибок
            for error_positions in itertools.combinations(range(self._n), num_errors):
                # Создаем вектор ошибки
                error_vector = np.zeros(self._n, dtype=int)
                for pos in error_positions:
                    error_vector[pos] = 1
                self._syndromes[_array_to_string(error_vector @ self._matrix.T)] = error_vector

    def __count_correction(self):
        min_weight = float('inf')
        for value in self._code_table.values():
            weight = sum(value)
            if weight > 0:
                min_weight = min(weight, min_weight)
        self._dmin = min_weight
        self._count_mistakes = (min_weight - 1) // 2


class MatrixModifications:
    def __init__(self):
        self._matrix_G = Matrix()
        self._matrix_H = Matrix()
        self._modified_matrix = Matrix()

    def set_modified_matrix(self, matrix: np.array):
        self._modified_matrix.set_matrix(matrix)
        self._modified_matrix.fill_info()

    def get_mod_matrix(self):
        return self._modified_matrix

    def get_modified_matrix(self):
        return self._modified_matrix.get_matrix()

    def set_matrix_H(self, matrix: np.array):
        _to_sys_matrix(matrix, matrix_type="H")
        self._matrix_H.set_matrix(matrix)
        self.__get_G_from_H()
        self._matrix_H.fill_info()
        self._matrix_G.fill_info()

    def get_dmin(self):
        return self._matrix_G.get_dmin()

    def get_dmin_modified(self):
        return self._modified_matrix.get_dmin()

    def get_matrix_H(self):
        return self._matrix_H.get_matrix()

    def set_matrix_G(self, matrix: np.array):
        _to_sys_matrix(matrix, matrix_type="G")
        self._matrix_G.set_matrix(matrix)
        self.__get_H_from_G()
        self._matrix_G.fill_info()
        self._matrix_H.fill_info()

    def get_matrix_G(self):
        return self._matrix_G.get_matrix()

    def get_count_mistakes(self):
        return self._matrix_G.get_count_mistakes()

    def __get_H_from_G(self):
        matrix_G = self._matrix_G.get_matrix()
        n, k = matrix_G.shape[1], matrix_G.shape[0]
        self.set_matrix_H(np.concatenate([matrix_G[:, -(n - k):].T, np.identity((n - k), dtype=int)], axis=1))


    def __get_G_from_H(self):
        matrix_H = self._matrix_H.get_matrix()
        n, k = matrix_H.shape[1], matrix_H.shape[0]
        self._matrix_G.set_matrix(np.concatenate([np.identity((n - k), dtype=int), matrix_H[:, :(n - k)].T], axis=1))

    # Укорочение кода
    def shortening_code(self, p=0):
        idx = self._matrix_G.get_k() if p == self._matrix_G.get_k() else p % 4
        new_matrix_G = np.delete(np.delete(self._matrix_G.get_matrix(), idx, axis=0), idx, axis=1)
        self.set_modified_matrix(new_matrix_G)

    # Расширение кода
    def extension_code(self):
        matrix_H = self.get_matrix_H()
        ones_row = np.ones((1, matrix_H.shape[1]), dtype=int)
        matrix_with_ones = np.vstack((ones_row, matrix_H))
        parity_vector = np.sum(matrix_with_ones, axis=1) % 2
        parity_vector = parity_vector.reshape(-1, 1)
        final_matrix = np.hstack((parity_vector, matrix_with_ones))
        self.set_modified_matrix(final_matrix)

    # Перфорация линейных блочных кодов
    def punching_code(self, p=0):
        matrix_H = self.get_matrix_H()
        n, k = matrix_H.shape
        start_column = n - k
        column_to_delete = start_column + p
        matrix_H = np.delete(matrix_H, column_to_delete, axis=1)
        matrix_H = np.delete(matrix_H, p, axis=0)
        self.set_modified_matrix(matrix_H)

    # Пополнение кода
    def add_code(self, p=1):
        # for i in range(p):
        #     vector = np.random.randint(0, 2, self._matrix_G.get_n())
        #     if self.__is_independent(vector):
        #         if self.get_modified_matrix() is None: self.set_modified_matrix(np.vstack([vector, self.get_matrix_G()]))
        #         else: self.set_modified_matrix(np.vstack([vector, self.get_modified_matrix()]))
        matrix_G = self.get_matrix_G()
        ones_row = np.ones((1, matrix_G.shape[1]), dtype=int)
        matrix_with_ones = np.vstack((ones_row, matrix_G))
        self.set_modified_matrix(matrix_with_ones)


    # def __is_independent(self, new_vector: np.array) -> bool:
    #     """
    #     Проверяет, является ли новый вектор линейно независимым от текущих строк порождающей матрицы.
    #     Для этого решаем систему линейных уравнений A * x = new_vector
    #     и проверяем, имеет ли решение только тривиальное решение (все x = 0).
    #     """
    #     if self.get_modified_matrix() is None: matrix = self.get_matrix_G()
    #     else: matrix = self.get_modified_matrix()
    #     augmented_matrix = np.vstack([matrix, new_vector])
    #     # Проводим гауссово исключение и смотрим, увеличился ли ранг
    #     rank_before = np.linalg.matrix_rank(matrix)
    #     rank_after = np.linalg.matrix_rank(augmented_matrix)
    #     return rank_after > rank_before

    # Выбрасывание кодовых слов.
    # В случае систематической матрицы
    # соотвутствует укорочению
    def ejecting_code(self):
        self.shortening_code()

    # Удлинение кода
    def prolongation_code(self):
        # vector = np.ones(self._matrix_G.get_n(), dtype=int)
        # self.set_matrix_H(np.vstack([vector, self.get_matrix_H()]))
        # self.extension_code()
        matrix_H = self.get_matrix_H()
        k, n = matrix_H.shape
        new_row = np.ones(n + 1, dtype=int)
        new_column = np.expand_dims(np.sum(matrix_H, axis=1) % 2, axis=1)
        extended_H = np.hstack((matrix_H, new_column))
        extended_H = np.vstack((extended_H, new_row))
        self.set_modified_matrix(extended_H)