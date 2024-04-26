from collections import defaultdict

from PythonLang.FormalLang.firstLaboratory.main import is_context_independent
from PythonLang.FormalLang.grammar_reader import grammar_reader


"""
e - epsilon

S -> KNM
K -> ab
N -> Ab
M -> AB
B -> e
A -> e
end

-----------
S -> KNM
K -> ab
N -> Ab
M -> AB
B -> p
B -> e
A -> c | e
end
------------

S -> 01A | 01B | A
A -> 0B1 | B | 1 | e
B -> BA0 | B1 | C | e
C -> 0C11 
D -> -D1 | -0 | -1
end
"""


def delete_eps_rules(grammar: dict[str, list[str]]) -> dict[str, list[str]]:

    set_with_e_terminals = set()
    new_grammar = defaultdict(list)

    start_symbol = next(iter(grammar))

    for symbol, rules in grammar.items():
        for rule in rules:
            if symbol != start_symbol and rule == "e": set_with_e_terminals.add(symbol)

    for symbol, rules in grammar.items():
        for rule in rules:
            if all(s in set_with_e_terminals for s in rule): set_with_e_terminals.add(symbol)

    for symbol, rules in grammar.items():
        if symbol in set_with_e_terminals:
            continue
        for rule in rules:
            if any(s in set_with_e_terminals for s in rule):
                for s in rule:
                    if s in set_with_e_terminals:
                        new_grammar[symbol].append(rule.replace(s, ""))
            elif symbol not in rule:
                new_grammar[symbol].append(rule)
    return new_grammar


def main() -> None:
    rules = grammar_reader()

    if is_context_independent(rules):
        print("Новая грамматика без эпсилон правил:")
        print("\n".join(f"{key} -> {' | '.join(value)}" for key, value in delete_eps_rules(rules).items()))
    else:
        print("Грамматика не является контекстно-свободной")


if __name__ == "__main__":
    main()