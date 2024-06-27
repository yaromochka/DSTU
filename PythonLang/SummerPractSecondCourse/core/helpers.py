from typing import List


def hex_to_bin(hex_str: str) -> str:
    """Преобразует шестнадцатеричную строку в двоичную строку."""
    return ''.join(bin(int(sym, 16))[2:].zfill(4) for sym in hex_str)


def permute(block: str, permutation: List[int]) -> str:
    """Выполняет перестановку битов в блоке согласно заданной перестановке."""
    return ''.join(block[i - 1] for i in permutation)


def xor_strings(a: str, b: str) -> str:
    """Выполняет побитовый XOR двух строк."""
    return ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))


# разделение текста на блоки по 64 бита
def separate(text: str, chunk_size: int) -> list:
    """Разделяет строку на части по n символов."""
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
