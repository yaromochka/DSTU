"""
Пример ввода:
R -> T1T
R -> T1U
R -> W
R -> E
T -> U
T -> T01
T -> T10
T -> E
U -> +U
U -> +0
U -> +1
W -> W-W
W -> W+W
V -> *0
V -> /1
end
----------
0 1 + - / *
"""

from itertools import chain
from typing import Mapping, Set, List, AnyStr
from PythonLang.FormalLang.firstLaboratory.main import is_context_independent
from PythonLang.FormalLang.grammatic_reader import grammatic_reader


def check_grammar_existence(grammar: Mapping[AnyStr, List[AnyStr]], set_of_non_terminals: Set[AnyStr]) -> bool:
    """
    Проверка КС грамматики с помощью алгоритма, который описан в методичке
    Args:
        grammar (Mapping[AnyStr, List[AnyStr]]) - правила перехода, которые ввел пользователь
        set_of_non_terminals (Set[AnyStr) - множество не терминалов
    """
    # Стартовый символ всегда в самом начале правил, поэтому так сделал
    start_symbol = next(iter(grammar))

    # Наше множество, в которое мы будем добавлять элементы
    set_with_non_terminals = {start_symbol}

    max_length = 0

    for symbol in chain.from_iterable(rule for rules in grammar.values() for rule in rules):

        if symbol in set_with_non_terminals | set_of_non_terminals:
            set_with_non_terminals.add(symbol)

        if max_length == (length := len(set_with_non_terminals)):
            break
        else:
            max_length = length

    return start_symbol in set_with_non_terminals


def main() -> AnyStr:
    rules = grammatic_reader()
    non_terminals = set(input("Введите множество не терминалов: ").split())

    if is_context_independent(rules):
        return (f"1)Введена КС - грамматика\n2)"
                f"{'Язык существует' if check_grammar_existence(rules, non_terminals) else 'Язык не существует'}")
    return "1)Введенная грамматика не является КС-грамматикой "


if __name__ == "__main__":
    print(main())