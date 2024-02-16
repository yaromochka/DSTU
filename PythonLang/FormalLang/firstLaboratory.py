def zero_type(string):
    pass


def regular_right(string):
    pass


def regular_left(string):
    pass


def context_freedom(string):
    pass


def context_dependet(string):
    pass


def main():
    countOfRules = int(input("Введите количество правил: "))
    print("Введите правила грамматики через ->: ")
    rules = []
    for i in range(countOfRules):
        rules.append(input())
    start = "S"
    for rule_index in range(len(rules)):
        for _ in range(16):
            start = start.replace(rules[rule_index].split(" -> ")[0], rules[rule_index].split(" -> ")[1])
            print(start)
    print(start)
    # if regular_rigth(start): print("Тип 3. Правосторонняя регулярная грамматика")
    # elif regular_left(start): print("Тип 3. Левосторонняя регулярная грамматика")
    # elif context_dependet(start): print("Тип 2. Контекстно зависимая грамматика")
    # elif context_freedom(start): print("Тип 1. Контекстно свободная грамматика")
    # elif zero_type(start): print("Тип 0. Грамматика типа 0")


if __name__ == "__main__":
    main()