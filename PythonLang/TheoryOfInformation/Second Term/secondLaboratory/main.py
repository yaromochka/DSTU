from typing import List


class ConvolutionalCode:
    def __init__(self, text=None):
        # text for encoding
        self.text: str = text
        self.binary_text: List[str] | None = None
        self.encoded_text = []

        # text for decoding
        self.decoded_bits = None
        self.decoded_text = None

        # adders to encode
        self.adders: List[List[int]] | None = None


    def set_text(self, text: str) ->  None:
        self.text = text


    def set_adders(self, adders: List[List[int]]) -> None:
        self.adders = adders


    def encode(self) -> None:
        self.__encode_to_binary()
        print(self.binary_text)
        if self.adders:
            length_of_register : int = max(len(adder) for adder in self.adders)
            encoded_list: List[str] = []
            for binary in self.binary_text:
                window: str = '0' * length_of_register
                for bit in binary:
                    window = bit + window[0:length_of_register - 1]
                    for adder in self.adders:
                        code: int = 0
                        for a in adder:
                            code ^= int(window[a])
                        encoded_list.append(str(code))
                self.encoded_text = ''.join(encoded_list)
        print(self.encoded_text)


    def __encode_to_binary(self) -> None:
        self.binary_text = [format(ord(ch), '08b') for ch in self.text]



def main() -> None:
    text_to_encode: str = input('Введите текст для кодирования: ')
    sum_input: int = int(input('Введите количество сумматоров: '))
    adders: List[List[int]] = []
    for _ in range(sum_input):
        adder = [int(a) for a in input('Введите положение сумматоров через запятую: ').split(',')]
        adders.append(adder)
    coder: ConvolutionalCode = ConvolutionalCode()
    coder.set_text(text_to_encode)
    coder.set_adders(adders)
    coder.encode()


if __name__ == '__main__':
    main()