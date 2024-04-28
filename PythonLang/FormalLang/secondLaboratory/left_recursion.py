from collections import defaultdict
from typing import Iterator

from PythonLang.FormalLang.firstLaboratory.main import is_context_independent
from PythonLang.FormalLang.grammar_reader import grammar_reader

"""
A -> BC | a
B -> CA | Ab
C -> AB | cC | a
end

-----------

S -> 01A | 01B | A
A -> 0B1 | B | 1 | e
B -> BA0 | B1 | C | e
C -> 0C11 
D -> -D1 | -0 | -1
end
"""


def _split_rules(rules: list[str], non_terminal: str) -> tuple[Iterator[str], Iterator[str]]:
    alpha_rules = (rule[len(non_terminal):] for rule in rules if rule.startswith(non_terminal))

    beta_rules = (rule for rule in rules if not rule.startswith(non_terminal))

    return alpha_rules, beta_rules


def _generate_new_rules(non_terminal: str,
                        alpha_rules: Iterator[str],
                        beta_rules: Iterator[str]) -> tuple[Iterator[str], Iterator[str], str]:

    new_non_terminal = non_terminal + "'"

    new_rules_non_terminal = (rule + new_non_terminal for rule in beta_rules)

    new_rules_new_non_terminal = iter([rule + new_non_terminal for rule in alpha_rules] + ["E"])

    return new_rules_non_terminal, new_rules_new_non_terminal, new_non_terminal


def delete_left_recursion(rules: dict[str, list[str]]) -> dict[str, list[str]]:

    non_terminals = defaultdict(list, rules)

    for non_terminal in rules:

        if any(rule.startswith(non_terminal) for rule in rules[non_terminal]):
            alpha_rules, beta_rules = _split_rules(non_terminals[non_terminal], non_terminal)

            if not alpha_rules:
                continue

            new_rules_non_terminal, new_rules_new_non_terminal, new_non_terminal = _generate_new_rules(non_terminal,
                                                                                                       alpha_rules,
                                                                                                       beta_rules)

            non_terminals[non_terminal] = list(new_rules_non_terminal)
            non_terminals[new_non_terminal] = list(new_rules_new_non_terminal)

    return non_terminals


def main() -> None:
    rules = grammar_reader()

    if is_context_independent(rules):
        print("Новая грамматика с удалённой левой рекурсией:")
        print("\n".join(f"{key} -> {' | '.join(value)}" for key, value in delete_left_recursion(rules).items()))
    else:
        print("Грамматика не является контекстно-свободной")


if __name__ == "__main__":
    main()
