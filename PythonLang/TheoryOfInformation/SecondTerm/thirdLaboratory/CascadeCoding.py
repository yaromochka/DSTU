from typing import List
import cv2
import numpy as np

from PythonLang.TheoryOfInformation.SecondTerm.secondLaboratory.ConvolutionalCode import ConvolutionalCode
from PythonLang.TheoryOfInformation.FirstTerm.thirdLaboratory.coding_logic import BlockCoder


def introduce_errors(data: List[int], error_rate: float) -> List[int]:
    noisy_data = data.copy()
    for i in range(len(noisy_data)):
        if np.random.rand() < error_rate:
            noisy_data[i] ^= 1  # Инвертируем бит
    return noisy_data


def separate(s: str, k: int = 8) -> List[str]:
    return [s[i:i + k] for i in range(0, len(s), k)]


class CascadeCoding:
    def __init__(self):
        self.block_coder = BlockCoder()
        self.conv_coder = ConvolutionalCode()

        self.encoded_data: str = ''
        self.encoded_block: List[str] = []

        self.decoded_data: List[int] = []

    def set_block_matrix(self, matrix: np.array) -> None:
        self.block_coder.set_matrix_G(matrix)

    def set_conv_coder(self, adders: List[List[int]]) -> None:
        self.conv_coder.set_adders(adders)

    def __encode(self):
        self.block_coder.encode_text()
        self.encoded_data: str = self.block_coder.get_encoded_text()
        self.encoded_block: List[str] = separate(self.encoded_data)
        # здесь должен быть перемеживатель
        self.conv_coder.set_binary_bits(self.encoded_block)
        self.conv_coder.encode()


    def __decode(self):
        pass

    def process_image(self, img_path: str, error_rate: float) -> None:
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        binary_data = np.unpackbits(img.flatten())
        self.block_coder.set_text(binary_data)

        self.__encode()
        # noisy_data = introduce_errors(encoded_data, error_rate)
        # decoded_data = self.__decode()
        decoded_data = [1, 0, 0, 1]

        restored_img = np.packbits(np.array(decoded_data, dtype=np.uint8)).reshape(img.shape)
        cv2.imwrite("decoded.png", restored_img)


def main() -> None:
    cascade_code = CascadeCoding()
    matrix: np.array = np.array([
        [1, 0, 0, 0, 1, 1, 0, 1],
        [0, 1, 0, 0, 1, 0, 0, 1],
        [0, 0, 1, 0, 0, 1, 1, 1],
        [0, 0, 0, 1, 1, 1, 0, 1]
    ])
    cascade_code.set_block_matrix(matrix)
    sum_input: int = int(input('Введите количество сумматоров: '))
    adders: List[List[int]] = [list(map(int, input(f'Введите положение сумматора {i + 1}: ').split(','))) for i in
                               range(sum_input)]
    cascade_code.set_conv_coder(adders)

    IMG = 'input.png'
    ERROR_RATE = 0.05  # Вероятность ошибки 5%
    cascade_code.process_image(IMG, ERROR_RATE)


if __name__ == "__main__":
    main()