"""
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

from typing import Mapping, Set, List, AnyStr
from PythonLang.FormalLang.firstLaboratory.main import is_context_independent
from PythonLang.FormalLang.grammar_reader import grammar_reader


def check_grammar_exist(grammar: Mapping[AnyStr, List[AnyStr]], set_of_non_terminals: Set[AnyStr]) -> bool:

    # Стартовый символ всегда в самом начале правил, поэтому так сделал
    start_symbol = next(iter(grammar))

    flag = False

    for non_terminal in set_of_non_terminals:
        # Наше множество, в которое мы будем добавлять элементы
        set_with_non_terminals = set()
        temporary_non_terminal = non_terminal
        for symbol, rules in reversed(grammar.items()):
            if any(temporary_non_terminal in rule for rule in rules):
                set_with_non_terminals.add(symbol)
            else:
                break
            temporary_non_terminal = symbol

        if start_symbol in set_with_non_terminals:
            flag = True
            break
    return flag


def main() -> AnyStr:
    rules = grammar_reader()
    non_terminals = set(input("Введите множество не терминалов: ").split())

    if is_context_independent(rules):
        return (f"1)Введена КС - грамматика\n2)"
                f"{'Язык существует' if check_grammar_exist(rules, non_terminals) else 'Язык не существует'}")
    return "Введенная грамматика не является КС-грамматикой "


if __name__ == "__main__":
    print(main())