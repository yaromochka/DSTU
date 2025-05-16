from PythonLang.TheoryOfInformation.FirstTerm.thirdLaboratory.coding_logic import BlockCoder
import numpy as np
from enums.matrix import MatrixType
from itertools import product


def hamming_distance(a: np.array, b: np.array) -> int:
    return np.sum(a != b)

def min_distance(G: np.array) -> int:
    k = G.shape[0]
    all_words = []

    # Перебираем все возможные 2^k слов
    for message in product([0, 1], repeat=k):
        word = np.array(message) @ G % 2
        all_words.append(word)

    # Считаем минимальное ненулевое расстояние
    d_min = float('inf')
    for i in range(len(all_words)):
        for j in range(i + 1, len(all_words)):
            d = hamming_distance(all_words[i], all_words[j])
            if d != 0:
                d_min = min(d_min, d)
    return d_min


def generate_code_matrix(n: int, k: int, d_required: int = 5) -> np.ndarray:
    attempts = 0
    while True:
        matrix_left = np.eye(k, dtype=int)
        matrix_right = np.random.randint(0, 2, size=(k, n - k))
        G = np.concatenate([matrix_left, matrix_right], axis=1)

        d = min_distance(G)
        attempts += 1
        if d >= d_required:
            # print(f"Матрица найдена за {attempts} попыток. Минимальное расстояние: {d}")
            return G


class AdaptiveSystem:
    def __init__(self):
        self.bc = BlockCoder()
        self.text = None
        self.errors = None
        self.encoded = False
        self.decoded = False
        self.solved = True
        self.many_errors = None

    def set_matrix(self, matrix: tuple[np.array, MatrixType]) -> None:
        if matrix[1] == MatrixType.MATRIX_G:
            self.bc.set_matrix_G(matrix[0])
        elif matrix[1] == MatrixType.MATRIX_H:
            self.bc.set_matrix_H(matrix[0])

    def set_text(self, text: str) -> None:
        self.text = text
        self.bc.set_text(text)

    def get_decoded_text(self) -> str:
        if self.decoded:
            return self.bc.decode_to_text()
        else:
            return 'Текст ещё не был декодирован'


    def get_encoded_text(self) -> str:
        if self.encoded:
            return self.bc.get_encoded_text()

    def get_count_mistakes(self) -> int:
        if self.bc.get_matrix_G() is not None or self.bc.get_matrix_H() is not None:
            return self.bc.get_count_mistakes()


    def encode(self) -> None:
        if self.text is None:
            return
        self.bc.encode_text()
        self.encoded = True

    def add_errors(self) -> None:
        self.bc.add_mistakes()
        self.solved = False

    def add_manual_errors(self, errors: list[int]) -> None:
        self.errors = errors
        self.bc.add_manual_mistakes(errors)
        self.solved = False

    def count_block_errors(self) -> None:
        if self.errors:
            used = set()
            for error in self.errors:
                n_block = error // self.bc._n
                print(f'Ошибка добавлена в блок {n_block}')
                if n_block not in used:
                    used.add(n_block)
                else:
                    self.many_errors = True
                    return

    def solve_errors(self) -> None:
        self.count_block_errors()
        if self.many_errors:
            print('Не получается исправить ошибки')
            print('Матрица автоматически модернизируется')
            self.modern_matrix()
        else:
            self.bc.solve_mistake()
            self.solved = True


    def modern_matrix(self) -> None:
        try:
            while self.bc.get_count_mistakes() < 2:
                new_matrix_G = generate_code_matrix(n=15, k=5)
                self.bc.set_matrix_G(new_matrix_G)
            self.set_text(self.text)
            self.encode()
            self.add_manual_errors(self.errors)
            self.bc.solve_mistake()
            self.solved = True
        except:
            self.bc._count_mistakes = 1
            self.modern_matrix()


    def decode(self) -> None:
        if self.encoded and self.solved:
            self.bc.decode_text()
            self.decoded = True
        else:
            return


def main() -> None:
    adaptiveSystem = AdaptiveSystem()
    matrix = (np.array([
        [1, 0, 0, 0, 1, 1, 0],
        [0, 1, 0, 0, 1, 0, 1],
        [0, 0, 1, 0, 0, 1, 1],
        [0, 0, 0, 1, 1, 1, 1],
    ]), MatrixType.MATRIX_G)
    adaptiveSystem.set_matrix(matrix)
    print(adaptiveSystem.get_count_mistakes())
    adaptiveSystem.set_text('fsdffsdafsdafdsafdsafsdafjjh3reu124eh12esdfssd')
    adaptiveSystem.encode()
    adaptiveSystem.add_manual_errors([2, 3, 12, 22, 23])
    adaptiveSystem.solve_errors()
    print(adaptiveSystem.get_count_mistakes())
    adaptiveSystem.decode()
    print(adaptiveSystem.get_decoded_text())


if __name__ == "__main__":
    main()