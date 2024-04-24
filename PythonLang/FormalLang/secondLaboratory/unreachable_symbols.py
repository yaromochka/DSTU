from collections import defaultdict
from typing import AnyStr, Generator, Any
from PythonLang.FormalLang.firstLaboratory.main import is_context_independent
from PythonLang.FormalLang.grammar_reader import grammar_reader


"""
Пример ввода:
E -> E+T | T
T -> T*F | F
F -> (E) | a
end
----------
a

E -> E+T | T
F -> (E) | a
end
----------
a

Q -> 01A | 01B | A
A -> 0B1 | B | 1 | e
B -> BA0 | B1 | C | e
C -> 0C11 
D -> -D1 | -0 | -1
end
---------
0 1 -
"""


def _processing_terminal_values(grammar_inner: dict[str, list[str]], symbol: str) -> Generator[str, Any, None]:
    """
    Обработка терминальных значений перед добавлением в стек
    """
    if symbol in grammar_inner:
        yield from (char for production in grammar_inner[symbol] for char in production if char.isupper())


def delete_unreachable_symbols(grammar: dict[str, list[str]]) -> dict[str, list[str]]:
    start_symbol = next(iter(grammar))

    # Множество достижимых символов
    reachable = set()
    # Стек для обхода символов
    stack = [start_symbol]

    while stack:
        symbol = stack.pop()
        if symbol not in reachable:
            reachable.add(symbol)
            # Обработка терминальных значений перед добавлением в стек
            if terminal_values := _processing_terminal_values(grammar_inner=grammar, symbol=symbol):
                stack.extend(terminal_values)

    new_grammar: dict[str, list[str]] = {}
    for symbol, productions in grammar.items():
        if symbol in reachable:
            new_productions: list[str] = []
            for production in productions:
                # Включаем только те продукции, которые содержат достижимые символы
                if all(char in reachable or not char.isupper() for char in production):
                    new_productions.append(production)
            if new_productions:
                new_grammar[symbol] = new_productions

    return new_grammar


def main() -> None:
    rules = grammar_reader()

    if is_context_independent(rules):
        print("Новая грамматика без недостижимых символов:")
        print("\n".join(f"{key} -> {' | '.join(value)}" for key, value in delete_unreachable_symbols(rules).items()))
    else:
        print("Грамматика не является контекстно-свободной")


if __name__ == "__main__":
    main()