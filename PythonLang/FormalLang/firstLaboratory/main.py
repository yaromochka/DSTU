import re
from collections import defaultdict
from typing import AnyStr


# Проверка правосторонней грамматики
def is_linear_right(args: defaultdict[str, list]) -> bool:
    pattern = re.compile("^[A-Z] -> (?:[A-Z]*[^A-Z]|\w+)")
    return _checker(args, pattern)


def is_linear_left(args: defaultdict[str, list]) -> bool:
    pattern = re.compile("^[A-Z] -> (?:[^A-Z]*[A-Z]|\w+)")
    return _checker(args, pattern)


def is_context_dependent(args: defaultdict[str, list]) -> bool:
    return True


def is_context_independent(args: defaultdict[str, list]) -> bool:
    return True


def _checker(grammar: dict[str, list[str]], pattern: re.Pattern[AnyStr]) -> bool:
    """
    В данную функцию передают саму грамматику, которую пользователь ввел с консоли и паттерн для проверки.
    """
    for first_half, second_half in grammar.items():
        if not all(pattern.fullmatch(f"{first_half} -> {second_half_el}") for second_half_el in second_half):
            return False
    return True


def main():
    print("Для окончания ввода введите end\nВведите грамматику вида S -> aSb:")

    dictionary = defaultdict(list)

    while (args := input()) != "end":
        key, value = map(lambda x: x.strip().rstrip("|E"), args.split("->"))
        dictionary[key].append(value)

    if is_linear_left(dictionary):
        return "Тип 3: регулярная лево линейная грамматика"

    if is_linear_right(dictionary):
        return "Тип 3: регулярная право линейная грамматика"

    if is_context_independent(dictionary):
        return "Тип 2: контекстно-свободная грамматика"

    if is_context_dependent(dictionary):
        return "Тип 1: контекстно-зависимая грамматика"

    # xAbCD -> xHD
    return "Грамматика типа 0"


if __name__ == "__main__":
    print(main())