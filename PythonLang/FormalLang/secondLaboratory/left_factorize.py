from collections import defaultdict

from PythonLang.FormalLang.firstLaboratory.main import is_context_independent
from PythonLang.FormalLang.grammar_reader import grammar_reader


def left_factorize(grammar: dict[str, list[str]]) -> dict[str, list[str]]:
    new_grammar = defaultdict(list)

    for symbol, rules in grammar.items():
        # Найти общий префикс среди производств текущего не терминала
        common_prefix = _find_common_prefix(rules)
        if common_prefix:

            # Если существует общий префикс, создаем для него новый нетерминальный символ
            new_non_terminal_symbol = symbol + "`"

            # Обновляем грамматику, чтобы отразить лево-факторные правила
            new_grammar[symbol].append(common_prefix + new_non_terminal_symbol)
            new_grammar[new_non_terminal_symbol].extend([rule[len(common_prefix):] for rule in rules])

        else:
            new_grammar[symbol].extend(filter(None, rules))

    return new_grammar


def _find_common_prefix(rules: list[str]) -> str:
    if not rules:
        return ""

    common_prefix = []
    for chars in zip(*rules):
        # Проверяем, то что совпадают ли все символы в одной позиции
        if len(set(chars)) == 1:
            # Если все символы одинаковы, добавляем их к общему префиксу
            common_prefix.append(chars[0])
        else:
            break

    return ''.join(common_prefix)


def main() -> None:
    rules = grammar_reader()

    if is_context_independent(rules):
        print("Новая грамматика с факторизацией1 правил:")
        print("\n".join(f"{key} -> {' | '.join(value)}" for key, value in left_factorize(rules).items()))
    else:
        print("Грамматика не является контекстно-свободной")


if __name__ == "__main__":
    main()