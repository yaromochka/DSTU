"""
Здесь реализовано 1 задание, где просят с помощью программного решения создать замену строк, создав свою грамматику.
L(G) = {(ac)^n, n>=0, a in {b, d}, c in {+, -}}
"""
from typing import Final

RULES: Final = {
        "S": {"1": "Ab+", "2": "Bd+"},
        "A": {"1": "ABd-", "2": "d-"},
        "B": {"1": "d+", "2": "b-"}
    }


# Функция, которая порождает цепочку, учитывая грамматики
def chain_generator(string: str) -> None:
    # Проходимся поэлементно, проверяя, что символы для замены есть в словаре
    for char in string:
        if char in RULES:
            string = string.replace(char, RULES[char][choice_in_dictionary(char)], 1)
            print(" --> ", string)

    # Рекурсивный вызов, если еще есть символы для замены
    if any(char in string for char in RULES.keys()):
        chain_generator(string)


def choice_in_dictionary(char: str) -> str:
    """
    Задействована логика проверки
    """
    replacement = None

    while replacement not in RULES[char]:
        replacement = input(f"Выберите на что заменить {char}? {RULES[char]}: ")

        if replacement not in RULES[char]:
            print("Неправильный ввод")

    return replacement


if __name__ == "__main__":
    # Всегда замена начинается с "S"
    chain_generator("S")