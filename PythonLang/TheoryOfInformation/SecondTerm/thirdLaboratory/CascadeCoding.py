from PIL import Image
import numpy as np

from PythonLang.TheoryOfInformation.FirstTerm.thirdLaboratory.coding_logic import BlockCoder
from PythonLang.TheoryOfInformation.SecondTerm.secondLaboratory.ConvolutionalCode import ConvolutionalCode


def array_to_eight(arr: str, num: int = 8) -> list[list[str]]:
    result = []
    for i in range(0, len(arr), num):
        result.append(list(arr[i:i + num]))
    return result


def bit_array_to_image(bits: list[str], size: tuple) -> None:
    pixels = []
    for i in range(0, len(bits), 3):
        byte = list(bits[i:i + 3])
        pixel = []
        for b in byte:
            pixel.append(int(''.join(b), 2))
        pixels.append(tuple(pixel))
    print(len(pixels))
    img = Image.new('RGB', size)
    img.putdata(pixels)
    img.show()
    img.save('output.png')


def array_to_string(sequence: list[list[int]]) -> list[str]:
    return [''.join([str(i) for i in b]) for b in sequence]


def image_to_bit_array(image: Image.Image) -> list:
    pixels = list(image.getdata())
    bits = []
    for pixel in pixels:
        bits.extend([format(b, '08b') for b in pixel])
    return bits


def block_interleave(data: list[str], n: int) -> list[str]:
    # Определяем количество строк
    rows = len(data)
    cols = n
    matrix = [list(codeword) for codeword in data]

    interleaved = []
    for col in range(cols):
        for row in range(rows):
            interleaved.append(matrix[row][col])
    return [''.join([str(b) for b in interleaved[i:i+cols]]) for i in range(0, len(interleaved), cols)]


def block_deinterleave(data: list[str], n: int) -> list[str]:
    cols = n
    rows = len(data)
    flat = [''.join(d) for d in data]
    matrix = [[''] * cols for _ in range(rows)]

    index = 0
    for col in range(cols):
        for row in range(rows):
            if index < len(flat):
                matrix[row][col] = flat[index]
                index += 1

    return [''.join(row) for row in matrix]


class CascadeCoder:
    def __init__(self):
        self.block_coder = BlockCoder()
        self.convolutional_coder = ConvolutionalCode()
        self.image_bits_to_encode: list[str] = []
        self.encoded_sequence = ''
        self.decoded_bits: list[str] = []
        self.n = None  # длина кодового слова
        self.size = None

    def set_adders(self, adders: list[list[int]]) -> None:
        self.convolutional_coder.set_adders(adders)

    def set_matrix_G(self, matrix: np.array) -> None:
        self.block_coder.set_matrix_G(matrix)
        self.n = matrix.shape[1]

    def set_matrix_H(self, matrix: np.array) -> None:
        self.block_coder.set_matrix_H(matrix)
        self.n = matrix.shape[0]

    def set_size(self, size: tuple) -> None:
        self.size = size

    def set_image_bits_to_encode(self, bits: list[str]) -> None:
        self.image_bits_to_encode = bits

    def encode(self) -> None:
        print('Encoding...')
        print(f'Длина до блочного кодера {len(''.join(self.image_bits_to_encode))}')
        self.block_coder.set_text(''.join(self.image_bits_to_encode))
        self.block_coder.encode_text()
        encoded_words = self.block_coder.get_encoded_text()
        print(f'Длина после кодирования блочного кодера {len(encoded_words)}')
        interleaved = block_interleave(encoded_words, self.n)
        print(f'Длина после перемежителя {len(interleaved)}')
        self.convolutional_coder.set_text(''.join(interleaved))
        self.convolutional_coder.set_binary_bits(interleaved)
        self.convolutional_coder.encode()
        self.encoded_sequence = self.convolutional_coder.encoded_text
        print(f'Длина после кодирования свёрточного кодера {len(self.encoded_sequence)}')

    def decode(self) -> None:
        print('Decoding...')
        self.convolutional_coder.set_text(self.encoded_sequence)
        self.convolutional_coder.decode()
        print(f'Длина после декодирования свёрточного кодера {len(self.convolutional_coder.decoded_list)}')
        deinterleaved = block_deinterleave(self.convolutional_coder.decoded_list, self.n)
        print(f'Длина после деперемежителя {len(deinterleaved)}')
        self.block_coder.string_encoded_text = ''.join(deinterleaved)
        self.block_coder.decode_text()
        decoded_text = self.block_coder.get_decoded_text()
        print(f'Длина после декодирования блочного кода {len(decoded_text)}')
        # Сгруппировать в тройки битов RGB
        temp_text = ''.join([''.join(t) for t in decoded_text])
        decoded_list = array_to_eight(temp_text)
        bit_array_to_image(decoded_list, self.size)



if __name__ == '__main__':
    cc = CascadeCoder()
    matrix_G = np.array([
        [1, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 1, 1],
        [0, 0, 1, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 1, 0],
    ])
    image = Image.open('input.jpg')
    cc.set_size(image.size)
    image_bits = image_to_bit_array(image)
    cc.set_matrix_G(matrix_G)
    adders = [[0, 1, 2], [1, 2], [0, 2]]
    cc.set_adders(adders)
    cc.set_image_bits_to_encode(image_bits)
    cc.encode()
    cc.decode()
