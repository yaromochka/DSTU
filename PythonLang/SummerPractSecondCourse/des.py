from typing import List, Union

from config import *
from core.enums import Mode
from core.helpers import *


class DES:
    def __init__(self, keys: list[str]) -> None:
        self.keys = keys

    def encrypt(self, message: str) -> str:
        """
        Шифрует сообщение с использованием ключей.

        Args:
            message (List[str]): Сообщение для шифрования.

        Returns:
            str: Зашифрованное сообщение.
        """
        encrypted_chunks = []
        message_chunks = [separate(chunk.encode("utf-8").hex().replace("fffe", ''), 16) for chunk in
                          list(message)]
        for chunk in message_chunks:
            chunk = (''.join(chunk)).zfill(16)
            encrypted_chunks.append(self.__encrypt_block(chunk, self.keys))
        return ' '.join(encrypted_chunks)

    def decrypt(self, message: str) -> str:
        """
        Расшифровывает сообщение с использованием ключей.

        Args:
            message (List[str]): Зашифрованное сообщение.

        Returns:
            str: Расшифрованное сообщение.
        """
        decrypted_chunks = []
        message_chunks = message.split(' ')
        for chunk in message_chunks:
            try:
                decrypted_chunk = (bytes.fromhex(self.__encrypt_block(chunk, self.keys[::-1]))
                                   .decode('utf-8').replace('\x00', ''))
                decrypted_chunks.append(decrypted_chunk)
            except ValueError:
                return 'Неверно'
        return ''.join(decrypted_chunks)

    def __encrypt_block(self, message: str, password: list[str]) -> str:
        """Шифрует сообщение с использованием указанного пароля."""
        message_bin = hex_to_bin(message)
        new_message = permute(message_bin, FIRST_PERMUTATION)

        left_block = new_message[:32]
        right_block = new_message[32:]

        for rnd in range(16):
            right_block_perm = permute(right_block, SECOND_PERMUTATION)
            bin_key = hex_to_bin(password[rnd])

            cipher = xor_strings(bin_key, right_block_perm)
            s_blocks = separate(cipher, 6)
            s_cipher = self.s_block_substitution(s_blocks, CIPHER_S_BLOCKS)

            cipher = permute(s_cipher, LAST_PERMUTATION)
            new_left_block = xor_strings(cipher, left_block)

            if rnd != 15:
                left_block, right_block = right_block, new_left_block
            else:
                left_block = new_left_block

        final_cipher = permute(left_block + right_block, IP_PERMUTATION)
        final_cipher = separate(final_cipher, 4)
        return ''.join(hex(int(block, 2))[2:] for block in final_cipher)

    @staticmethod
    def s_block_substitution(blocks: List[str], s_blocks: dict) -> str:
        """Выполняет замену S-блоков."""
        substituted = []
        for i, block in enumerate(blocks):
            row = int(block[0] + block[-1], 2)
            col = int(block[1:5], 2)
            substituted.append(s_blocks[i + 1][row][col])
        return ''.join(bin(num)[2:].zfill(4) for num in substituted)


class Key:
    def __init__(self, password: str) -> None:
        self.password = password
        self.__round_keys = self.generate_key(password)

    @property
    def round_keys(self) -> List[str]:
        return self.__round_keys

    def generate_key(self, password: str) -> List[str]:
        """
        Генерирует ключи для каждого раунда DES из исходного пароля.

        Args:
            password (str): Исходный пароль.

        Returns:
            List[str]: Список ключей для каждого раунда DES.
        """
        password_hex = password.encode("UTF-8").hex().replace('d0', '').replace('d1', '').zfill(16)
        password_bin = hex_to_bin(password_hex)
        password_permuted = permute(password_bin, KEY_PERMUTATION_FIRST)

        left_pw = password_permuted[:len(password_permuted) // 2]
        right_pw = password_permuted[len(password_permuted) // 2:]

        return self.__get_round_keys(left_pw, right_pw)

    @staticmethod
    def __get_round_keys(left_key: str, right_key: str) -> List[str]:
        """
        Генерация 16 ключей для шифрования DES из левой и правой половин ключа.

        Args:
            left_key (str): Левая половина исходного ключа (в двоичном виде).
            right_key (str): Правая половина исходного ключа (в двоичном виде).

        Returns:
            List[str]: Список из 16 раундовых ключей в шестнадцатеричном виде.
        """
        round_keys = []

        for round_shift in KEY_ROUND:
            left_key = left_key[round_shift:] + left_key[:round_shift]
            right_key = right_key[round_shift:] + right_key[:round_shift]

            combined_key = left_key + right_key
            permuted_key = ''.join(combined_key[i - 1] for i in KEY_PERMUTATION_SECOND)

            hex_key = ''.join(
                hex(int(bits, 2))[2:]
                for bits in separate(permuted_key, 4)
            )

            round_keys.append(hex_key)

        return round_keys