from collections import defaultdict


# Функция для ввода грамматик
def grammatic_reader():
    print("Для окончания ввода введите end\nВведите грамматику вида S -> aSb: ")

    dictionary = defaultdict(list)

    while (args := input()) != "end":
        key, value = map(lambda x: x.strip().rstrip("|E"), args.split("->"))
        dictionary[key].append(value)

    return dictionary