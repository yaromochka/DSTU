"""
Q -> 01A | 01B | A
A -> 0B1 | B | 1 | e
B -> BA0 | B1 | C | e
C -> 0C11
D -> -D1 | -0 | -1
end
---------
0 1 -
Существует

Пример ввода:
E -> E+T | T
T -> T*F | F
F -> (E) | a
end
----------
a
СУЩЕСТВУЕТ


E -> E+T | T
T -> T*A
F -> (E) | a
end
----------
a
НЕ СУЩЕСТВУЕТ

E -> E+T | T
A -> T*F | F
F -> (E) | a
end
----------
a
НЕ СУЩЕСТВУЕТ


E -> E+T | T
F -> (E) | a
end
-------
a
НЕ СУЩЕСТВУЕТ
"""

from PythonLang.FormalLang.firstLaboratory.main import is_context_independent
from PythonLang.FormalLang.grammar_reader import grammar_reader


def check_grammar_exist(grammar: dict[str, list[str]], set_of_non_terminals: set[str], key="exist")\
        -> bool | set[str]:

    # Стартовый символ всегда в самом начале правил, поэтому так сделал
    start_symbol = next(iter(grammar))

    flag = False

    for non_terminal in set_of_non_terminals:
        # Наше множество, в которое мы будем добавлять элементы
        set_with_non_terminals = set()
        temporary_non_terminal = non_terminal
        for symbol, rules in reversed(grammar.items()):

            if any(temporary_non_terminal in rule for rule in rules) or any(non_terminal in rule for rule in rules):
                set_with_non_terminals.add(symbol)
            else:
                continue
            temporary_non_terminal = symbol

        if start_symbol in set_with_non_terminals:
            if key == "exist":
                flag = True
                break
            else:
                return set_with_non_terminals
    return flag


def main() -> str:
    rules = grammar_reader()
    non_terminals = set(input("Введите множество не терминалов: ").split())

    if is_context_independent(rules):
        return (f"1)Введена КС - грамматика\n2)"
                f"{'Язык существует' if check_grammar_exist(rules, non_terminals) else 'Язык не существует'}")
    return "Введенная грамматика не является КС-грамматикой "


if __name__ == "__main__":
    print(main())