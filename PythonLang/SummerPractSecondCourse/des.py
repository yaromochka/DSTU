from typing import List, Union

from config import *


class DES:
    def __init__(self, text: str, password: str) -> None:
        self.text = text
        self.password = password


def hex_to_bin(hex_str: str) -> str:
    """Преобразует шестнадцатеричную строку в двоичную строку."""
    return ''.join(bin(int(sym, 16))[2:].zfill(4) for sym in hex_str)


def permute(block: str, permutation: List[int]) -> str:
    """Выполняет перестановку битов в блоке согласно заданной перестановке."""
    return ''.join(block[i - 1] for i in permutation)


def xor_strings(a: str, b: str) -> str:
    """Выполняет побитовый XOR двух строк."""
    return ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))


def s_block_substitution(blocks: List[str], s_blocks: dict) -> str:
    """Выполняет замену S-блоков."""
    substituted = []
    for i, block in enumerate(blocks):
        row = int(block[0] + block[-1], 2)
        col = int(block[1:5], 2)
        substituted.append(s_blocks[i + 1][row][col])
    return ''.join(bin(num)[2:].zfill(4) for num in substituted)


def encrypt(message: str, password: list[str]) -> str:
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
        s_cipher = s_block_substitution(s_blocks, CIPHER_S_BLOCKS)

        cipher = permute(s_cipher, LAST_PERMUTATION)
        new_left_block = xor_strings(cipher, left_block)

        if rnd != 15:
            left_block, right_block = right_block, new_left_block
        else:
            left_block = new_left_block

    final_cipher = permute(left_block + right_block, IP_PERMUTATION)
    final_cipher = separate(final_cipher, 4)
    return ''.join(hex(int(block, 2))[2:] for block in final_cipher)


# разделение текста на блоки по 64 бита
def separate(text: str, chunk_size: int) -> list:
    """Разделяет строку на части по n символов."""
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]


def get_round_keys(left_key: str, right_key: str) -> List[str]:
    """
    Generate 16 round keys for DES encryption from left and right key halves.

    Args:
        left_key (str): Left half of the initial key (in binary form).
        right_key (str): Right half of the initial key (in binary form).

    Returns:
        List[str]: List of 16 round keys in hexadecimal form.
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


def generate_key(password: str) -> List[str]:
    """
    Генерирует ключи для каждого раунда DES из исходного пароля.

    Args:
        password (str): Исходный пароль.

    Returns:
        List[str]: Список ключей для каждого раунда DES.
    """
    password_hex = password.encode("utf-8").hex().upper().zfill(16)
    password_bin = hex_to_bin(password_hex)
    password_permuted = permute(password_bin, KEY_PERMUTATION_FIRST)

    left_pw = password_permuted[:len(password_permuted) // 2]
    right_pw = password_permuted[len(password_permuted) // 2:]

    return get_round_keys(left_pw, right_pw)


def encrypt_message(message: List[str], keys: List[str]) -> str:
    """
    Шифрует сообщение с использованием ключей.

    Args:
        message (List[str]): Сообщение для шифрования.
        keys (List[str]): Ключи для каждого раунда DES.

    Returns:
        str: Зашифрованное сообщение.
    """
    encrypted_chunks = []
    for chunk in message:
        chunk = chunk.zfill(16)
        encrypted_chunks.append(encrypt(chunk, keys))
    return ' '.join(encrypted_chunks)


def decrypt_message(message: List[str], keys: List[str]) -> str:
    """
    Расшифровывает сообщение с использованием ключей.

    Args:
        message (List[str]): Зашифрованное сообщение.
        keys (List[str]): Ключи для каждого раунда DES.

    Returns:
        str: Расшифрованное сообщение.
    """
    decrypted_chunks = []
    for chunk in message:
        try:
            decrypted_chunk = bytes.fromhex(encrypt(chunk, keys[::-1])).decode('utf-8').replace('\x00', '')
            decrypted_chunks.append(decrypted_chunk)
        except ValueError:
            return 'Неверно'
    return ''.join(decrypted_chunks)


def des(turn: int, message: str, password: str) -> Union[str, List[str]]:
    """
    Выполняет шифрование или расшифровку сообщения с использованием DES.

    Args:
        turn (int): 0 для шифрования, 1 для расшифровки.
        message (str): Сообщение для обработки.
        password (str): Пароль для генерации ключей.

    Returns:
        Union[str, List[str]]: Зашифрованное или расшифрованное сообщение.
    """
    keys = generate_key(password)

    if turn == 0:
        message_chunks = [separate(chunk.encode("utf-8").hex().upper().replace("FFFE", ''), 16) for chunk in
                          list(message)]
        encrypted_message = [encrypt_message(chunk, keys) for chunk in message_chunks]
        return ' '.join(encrypted_message)

    elif turn == 1:
        message_chunks = message.split(' ')
        return decrypt_message(message_chunks, keys)

    else:
        return 'Вводить надо либо 0, либо 1'
