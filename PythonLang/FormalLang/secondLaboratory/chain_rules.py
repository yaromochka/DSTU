"""
Q -> 01A | 01B | A
A -> 0B1 | B | 1 | e
B -> BA0 | B1 | C | e
C -> 0C11
D -> -D1 | -0 | -1
end
--------
A -> B | ab
B -> a | C
C -> b
end
"""


from typing import Any, Generator

from unreachable_symbols import delete_unreachable_symbols
from eps_rules import delete_eps_rules
from PythonLang.FormalLang.grammar_reader import grammar_reader


def delete_chains(rules: dict[str, list[str]]) -> dict[str, list[str]]:

    # Получаем список нетерминальных символов
    not_terminals = set(rules.keys())

    # Создаем пары символов
    pairs = [(char_not_terminal, char_not_terminal) for char_not_terminal in not_terminals]

    # Расширяем пары символов для учета новых возможных пар
    for char in not_terminals:
        pairs.extend(_expand_pairs(pairs, rules, not_terminals, char))

    return _configure_new_rules(rules, pairs)


def _expand_pairs(
        pairs: list[tuple[str, str]],
        rules: dict[str, list[str]],
        not_terminals: set[str],
        char: str) -> Generator[tuple[str, str], Any, None]:

    for left, right in pairs:
        if right == char:
            yield from ((left, elem) for elem in rules[char] if elem in not_terminals and elem != char)


def _configure_new_rules(rules: dict[str, list[str]], pairs: list[tuple[str, str]]) -> dict[str, list[str]]:
    """
    Здесь происходит конфигурация данных правил в результате алгоритма
    """
    new_rules = {char: [elem for elem in rules.get(char) if elem not in rules.keys()] for char in rules}

    for left, right in pairs:
        if left != right:
            new_rules[left].extend(new_rules[right])

    return new_rules


def main() -> None:
    grammar = grammar_reader()
    new_grammar = delete_unreachable_symbols(delete_chains(grammar))
    print("Новая грамматика без цепных правил:")
    print("\n".join(f"{key} -> {' | '.join(value)}".rstrip("|") for key, value in new_grammar.items()))


if __name__ == '__main__':
    main()