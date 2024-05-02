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

    new_grammar = defaultdict(list)

    new_grammar["J"].append("S")
    new_grammar["J"].append("e")
    for symbol, rules in grammar.items():
        if any(["e" in rule for rule in rules]):
            set_with_non_terminals = set()
            for rule in rules:
                for s in rule:
                    if not(s.isalpha()):
                        set_with_non_terminals.add(s)
            for non_terminal in set_with_non_terminals:
                new_grammar[symbol].append(non_terminal)
            for rule in rules:
                if rule != "e":
                    new_grammar[symbol].append(rule)
        else:
            for rule in rules:
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