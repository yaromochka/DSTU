#!/usr/bin/env python3
import functools
import pathlib
from typing import Union, List

import click

from core.enums import Mode
from des import Key, DES


def split_list(lst: list, chunk_size: int) -> list[str]:
    return [' '.join(lst[i:i + chunk_size]) for i in range(0, len(lst), chunk_size)]


def checker(function):
    @functools.wraps(function)
    def wrapper(file, password):
        if pathlib.Path(file).exists() and len(password) <= 8:
            return function(file, password)
        click.echo("Invalid file or password length")

    return wrapper


@click.group()
def mycommands():
    pass


@click.command()
@click.option('-f', '--file', type=click.Path(exists=False), default="file.txt", help='Path to the file')
@click.option('-p', '--password', prompt='Enter password to encryption', help='Password for encryption')
@checker
def encryption(file, password):
    with open(file, "r+") as f:
        text = f.read()
        f.seek(0)
        result = start_logic(Mode.ENCRYPTION, text, password).split()
        result = '\n'.join(block for block in split_list(result, 6))
        f.write(result)
        f.truncate()


@click.command()
@click.option('-f', '--file', type=click.Path(exists=False), default="file.txt", help='Path to the file')
@click.option('-p', '--password', prompt='Enter password to encryption', help='Password for encryption')
@checker
def decryption(file, password):
    with open(file, "r+") as f:
        text = f.read()
        f.seek(0)
        result = start_logic(Mode.DECRYPTION, text.replace('\n', ' '), password)
        if result != 'Неверно':
            f.write(result)
        else:
            f.write(text)
            click.echo("Invalid password")
        f.truncate()


def start_logic(mode: Mode, message: str, password: str) -> Union[str, List[str]]:
    """
    Выполняет шифрование или расшифровку сообщения с использованием DES.

    Args:
        mode (Mode): 0 для шифрования, 1 для расшифровки.
        message (str): Сообщение для обработки.
        password (str): Пароль для генерации ключей.

    Returns:
        Union[str, List[str]]: Зашифрованное или расшифрованное сообщение.
    """
    keys = Key(password).round_keys
    cipher = DES(keys)

    if mode == mode.ENCRYPTION:
        encrypted_message = cipher.encrypt(message)
        return encrypted_message

    if mode == mode.DECRYPTION:
        decrypted_message = cipher.decrypt(message)
        return decrypted_message


mycommands.add_command(encryption)
mycommands.add_command(decryption)

if __name__ == '__main__':
    mycommands()
