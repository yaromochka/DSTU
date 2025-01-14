from typing import List


def decode_cipher(cipher: str) -> str:
    result: List[str] = list(cipher)
    n: int = len(cipher) // 2
    for i in range(n):
        result[2 * i: 2 * i + 2] = cipher[i + n], cipher[i]
    return ''.join(result)


def main() -> None:
    cipher: str = input()
    decode_message = decode_cipher(cipher)
    print(decode_message)


if __name__ == "__main__":
    main()