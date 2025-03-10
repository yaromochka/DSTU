from typing import List, Tuple, Dict
from collections import defaultdict


class ConvolutionalCode:
    def __init__(self, text=None):
        self.text: str = text

        # Adders to encode
        self.adders: List[List[int]] | None = None

        # Count of registers
        self.length_of_register: int = 0

        # Count of adders
        self.count_adders: int = 0

        # Text for encoding
        self.binary_bits: List[str] | None = None
        self.encoded_text: None | str = None
        self.encoded_list: List[str] = []

        # Text for decoding
        self.decoded_list: List[List[str]] = []
        self.decoded_text = None

        # Graph for decoding
        self.graph: Dict[str, List[Tuple[str, str]]] = defaultdict(list)

    def set_text(self, text: str) -> None:
        self.text = text

    def set_adders(self, adders: List[List[int]]) -> None:
        self.adders = adders
        self.length_of_register = max(len(adder) for adder in self.adders)
        self.count_adders = len(adders)

    def encode(self) -> None:
        self._encode_to_binary()
        print(f'Закодированная последовательность битов {self.binary_bits}')
        self.encoded_list = [self._encode_sequence(binary) for binary in self.binary_bits]
        self.encoded_text = ''.join(self.encoded_list)
        print(f'Закодированный список {self.encoded_list}')
        print(f'Закодированный текст {self.encoded_text}')

    def decode(self) -> None:
        for encoded in self.encoded_list:
            window: str = '0' * self.length_of_register
            decoded_list: List[str] = []
            for idx in range(0, len(encoded), self.count_adders):
                encoded_text = encoded[idx:idx + self.count_adders]
                ways: List[Tuple[str, str]] = self.graph[window]
                for num, way in enumerate(ways):
                    state, decode = way[0], way[1]
                    if encoded_text == decode:
                        decoded_list.append(str(num))
                        window = state
            self.decoded_list.append(decoded_list)
        self.decoded_text = ''.join([chr(int(''.join(text), 2)) for text in self.decoded_list])
        print(self.decoded_text)


    def _encode_to_binary(self) -> None:
        """Преобразует входной текст в двоичный код."""
        self.binary_bits = [format(ord(ch), '08b') for ch in self.text]


    def _encode_sequence(self, binary: str) -> str:
        """ Encodes a binary sequence based on the convolutional code """
        length_of_register: int = self.length_of_register
        window: str = '0' * length_of_register
        encoded_list: List[str] = []
        for bit in binary:
            window = bit + window[:-1]
            encoded_list.append(self._generate_encoded_bits(window))
        return ''.join(encoded_list)


    def _generate_encoded_bits(self, window: str) -> str:
        """ Generates the encoded output bits based on the adder configuration """
        return ''.join(
            str(sum(int(window[a]) for a in adder) % 2) for adder in self.adders
        )

    def build_graph(self) -> None:
        """ Builds the state transition graph """
        num_states = 2 ** self.length_of_register
        for state in range(num_states):
            state_str = format(state, f'0{self.length_of_register}b')
            for bit in ['0', '1']:
                next_state = bit + state_str[:-1]
                encoded_output = self._generate_encoded_bits(next_state)
                self.graph[state_str].append((next_state, encoded_output))

    def print_graph(self) -> None:
        """ Prints the state transition graph """
        print(self.graph)


if __name__ == '__main__':
    text_to_encode: str = input('Введите текст для кодирования: ')
    sum_input: int = int(input('Введите количество сумматоров: '))
    adders: List[List[int]] = [list(map(int, input(f'Введите положение сумматора {i + 1}: ').split(','))) for i in
                               range(sum_input)]

    coder = ConvolutionalCode()
    coder.set_text(text_to_encode)
    coder.set_adders(adders)
    coder.encode()
    coder.build_graph()
    coder.decode()
    # coder.print_graph()