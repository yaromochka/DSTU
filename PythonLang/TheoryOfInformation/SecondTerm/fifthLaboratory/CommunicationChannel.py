import math
import random

from PythonLang.TheoryOfInformation.SecondTerm.fifthLaboratory.enums.ChannelType import ChannelType
from PythonLang.TheoryOfInformation.SecondTerm.secondLaboratory.ConvolutionalCode import ConvolutionalCode


class CommunicationChannel:
    def __init__(self, channel_type: ChannelType):
        self.text = ''
        self.adders = []
        self.encoded_data = None
        self.new_encoded_data = None
        self.channel_type = channel_type

        self.coder = ConvolutionalCode()

    def set_text(self, text: str) -> None:
        self.text = text
        self.coder.set_text(text)

    def set_adders(self, adders: list[list[int]]) -> None:
        self.adders = adders
        self.coder.set_adders(adders)

    def get_encoded_text(self) -> str:
        return self.coder.encoded_text

    def encode(self):
        self.coder.encode()
        self.encoded_data = self.coder.encoded_list

    def add_mistakes(self):
        new_encoded_data: list[str] = []
        for encode in self.encoded_data:
            is_error = random.random() < 0.5
            if is_error:

                if self.channel_type == ChannelType.DSK:
                    for _ in range(random.randint(1, len(encode))):
                        place = random.randint(0, len(encode) - 1)
                        if encode[place] == '0':
                            encode = encode[:place] + '1' + encode[place + 1:]
                        else:
                            encode = encode[:place] + '0' + encode[place + 1:]
                    new_encoded_data.append(encode)


                elif self.channel_type == ChannelType.DSKS:
                    is_skip = random.random() < 0.5
                    for i in range(random.randint(1, len(encode))):
                        if is_skip:
                            encode = encode[:i] + encode[i + 1:]
                            continue
                        place = random.randint(0, len(encode) - 1)
                        if encode[place] == '0':
                            encode = encode[:place] + '1' + encode[place + 1:]
                        else:
                            encode = encode[:place] + '0' + encode[place + 1:]
                    new_encoded_data.append(encode)


                elif self.channel_type == ChannelType.Z:
                    for _ in range(random.randint(1, len(encode))):
                        place = random.randint(0, len(encode) - 1)
                        if encode[place] == '0':
                            continue
                        else:
                            encode = encode[:place] + '0' + encode[place + 1:]
                    new_encoded_data.append(encode)
            else:
                new_encoded_data.append(encode)
        self.new_encoded_data = new_encoded_data

    def count_p_errors(self) -> int:
        global throughput
        if self.channel_type in (ChannelType.DSK, ChannelType.Z):
            total_bits = 0
            error_bits = 0

            for o, r in zip(self.encoded_data, self.new_encoded_data):
                for bit_o, bit_r in zip(o, r):
                    total_bits += 1
                    if bit_o != bit_r:
                        error_bits += 1
            error_probability = error_bits / total_bits
            if self.channel_type == ChannelType.DSK:
                throughput = 1 + error_probability * math.log2(error_probability) + (1 - error_probability) * math.log2(1 - error_probability)
            elif self.channel_type == ChannelType.Z:
                throughput = math.log2(1 + (1 - error_probability) * (error_probability ** (error_probability / (error_probability ** (1 - error_probability)))))
            return (error_probability, throughput)

        elif self.channel_type == ChannelType.DSKS:
            total_bits = 0
            error_bits = 0
            erasure_bits = 0

            for o, r in zip(self.encoded_data, self.new_encoded_data):
                min_len = min(len(o), len(r))
                total_bits += len(o)

                for i in range(min_len):
                    if o[i] != r[i]:
                        error_bits += 1

                if len(r) < len(o):
                    erasure_bits += len(o) - len(r)

            error_prob = error_bits / total_bits
            erasure_prob = erasure_bits / total_bits
            throughput = 1 - erasure_prob + (1 - error_prob - erasure_prob) * math.log2((1 - error_prob - erasure_prob) / (1 - error_prob)) + error_prob * math.log2(error_prob / (1 - error_prob))
            return (error_prob, erasure_prob, throughput)


def main() -> None:
    original_text = "Hello, world!"
    sum_input: int = int(input('Введите количество сумматоров: '))
    adders: list[list[int]] = [list(map(int, input(f'Введите положение сумматора {i + 1}: ').split(','))) for i in
                               range(sum_input)]

    # Создание канала
    channel = CommunicationChannel(ChannelType.DSKS)
    channel.set_text(original_text)
    channel.set_adders(adders)

    channel.encode()
    channel.add_mistakes()
    print(channel.count_p_errors())


if __name__ == '__main__':
    main()