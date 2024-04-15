import re
from PythonLang.FormalLang.grammatic_reader import grammatic_reader
from typing import AnyStr, Pattern

"""
E -> E+T | T
T -> T*F | F
F -> (F) | a
end
"""


# Проверка правосторонней грамматики
def is_linear_right(args: dict[str, list]) -> bool:
    """
    Пример:
    S -> aS
    S -> aA
    A -> bA
    A -> bZ
    Z -> $
    """
    return _checker(args, re.compile(r"^[A-Z] -> [^A-Z]*[A-Z]?$"))


# Проверка левосторонней грамматики
def is_linear_left(args: dict[str, list]) -> bool:
    """
    Пример:
    S -> Ab
    A -> Ab
    A -> Za
    Z -> Za
    Z -> $
    """
    return _checker(args, re.compile(r"^[A-Z] -> [A-Z]?[^A-Z]*$"))


# Проверка контекстно-независимой грамматики
def is_context_independent(args: dict[str, list]) -> bool:
    """
    Пример:
    S -> aSa
    S -> bSb
    S -> aa
    I -> bb
    """
    return _checker(args, re.compile(r'^[A-Z] -> .*$'))


# Проверка контекстно-зависимой грамматики
def is_context_dependent(args: dict[str, list]) -> bool:
    """
    Пример:
    S -> aAS
    AS -> AAS
    AAA -> ABA
    A -> b
    bBA -> bcdA
    bS -> ba
    """
    return _checker(args, re.compile(r'^.*[A-Z]+.* -> .*.+.*$'))


# Функция для проверки введёных грамматик через соответствующие паттерны
def _checker(grammar: dict[str, list[str]], pattern: Pattern[AnyStr]) -> bool:
    """
    В данную функцию передают саму грамматику, которую пользователь ввел с консоли и паттерн для проверки.
    """
    for first_half, second_half in grammar.items():
        if not all(pattern.fullmatch(f"{first_half} -> {second_half_el}") for second_half_el in second_half):
            return False
    return True


def main(dictionary=None) -> str:
    if dictionary is None:
        dictionary = grammatic_reader()

    if is_linear_left(dictionary):
        return "Тип 3: регулярная левосторонняя грамматика"

    if is_linear_right(dictionary):
        return "Тип 3: регулярная правосторонняя грамматика"

    if is_context_independent(dictionary):
        return "Тип 2: контекстно-свободная грамматика"

    if is_context_dependent(dictionary):
        return "Тип 1: контекстно-зависимая грамматика"

    return "Грамматика типа 0"


if __name__ == "__main__":
    print(main())