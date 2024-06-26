#!/usr/bin/env python3
import click
import pathlib
from des import des
import functools


def split_list(lst: list, chunk_size: int) -> list[str]:
    return [' '.join(lst[i:i + chunk_size]) for i in range(0, len(lst), chunk_size)]


def file_checker(function):
    @functools.wraps(function)
    def wrapper(file, password):
        if pathlib.Path(file).exists():
            return function(file, password)
        click.echo("Invalid file")

    return wrapper


@click.group()
def mycommands():
    pass


@click.command()
@click.option('-f', '--file', type=click.Path(exists=False), default="file.txt", help='Path to the file')
@click.option('-p', '--password', prompt='Enter password to encryption', help='Password for encryption')
@file_checker
def encryption(file, password):
    with open(file, "r") as f:
        text = f.read()
    with open(file, "w") as f:
        result = des(0, text, password).split()
        result = '\n'.join(block for block in split_list(result, 6))
        f.write(result)


@click.command()
@click.option('-f', '--file', type=click.Path(exists=False), default="file.txt", help='Path to the file')
@click.option('-p', '--password', prompt='Enter password to encryption', help='Password for encryption')
@file_checker
def decryption(file, password):
    with open(file, "r") as f:
        text = f.read().replace('\n', ' ')
    with open(file, "w") as f:
        result = des(1, text, password)
        if result != 'Неверно':
            f.write(result)
        else:
            click.echo("Invalid password")


mycommands.add_command(encryption)
mycommands.add_command(decryption)

if __name__ == '__main__':
    mycommands()
