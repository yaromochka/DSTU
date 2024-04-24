from collections import defaultdict
from typing import AnyStr, Set
from PythonLang.FormalLang.grammar_reader import grammar_reader
from PythonLang.FormalLang.firstLaboratory.main import is_context_independent
from grammar_exist import check_grammar_exist


"""
Q -> 01A | 01B | A
A -> 0B1 | B | 1 | e
B -> BA0 | B1 | C | e
C -> 0C11 
D -> -D1 | -0 | -1
end
---------
0 1 -


S -> a | A
A -> AB
B -> b
end
---------
a b


S -> A
A -> b
B -> b
end
---------
b


S -> A
A -> B
B -> b
end
----------
b
"""


def delete_useless(grammar: dict[str, list[str]], set_of_non_terminals: set[str]) -> dict[str, list[str]]:
    """
    Данная функция удаляет бесполезные символы, проверяя, что элемент грамматики входит во множество терминалов
    """
    set_without_useless_terminals = check_grammar_exist(grammar, set_of_non_terminals, key="don't exist")
    grammar_without_useless_terminals = defaultdict(list)
    for symbol, rules in grammar.items():
        for rule in rules:
            if symbol in set_without_useless_terminals and any(s in set_of_non_terminals for s in rule):
                grammar_without_useless_terminals[symbol].append(rule)
    return grammar_without_useless_terminals


def main() -> None:
    rules = grammar_reader()
    non_terminals = set(input('Введите множество не терминалов: ').split())

    if is_context_independent(rules) and check_grammar_exist(rules, non_terminals):
        print("Новая грамматика без бесполезных символов:")
        print("\n".join(f"{key} -> {'|'.join(value)}" for key, value in delete_useless(rules, non_terminals).items()))
    else:
        print("Грамматика не является контекстно-свободной или язык не существует")


if __name__ == "__main__":
    main()