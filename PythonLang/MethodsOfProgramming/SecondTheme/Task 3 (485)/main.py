from itertools import permutations


def main():
    # Ввод количества тараканов и ставок
    k, n = map(int, input().split())

    # Считываем ставки
    rates = [tuple(map(int, input().split())) for _ in range(n)]

    # Генерируем начальную перестановку тараканов
    cockroaches = list(range(1, k + 1))

    # Перебираем все перестановки
    for perm in permutations(cockroaches):
        # Создаем массив позиций для текущей перестановки
        positions = {cockroach: idx for idx, cockroach in enumerate(perm)}

        valid = True  # Флаг валидности текущей перестановки

        # Проверяем каждую ставку
        for a, b, c, d in rates:
            # Индексы тараканов в текущей перестановке
            index_a = positions[a]
            index_b = positions[b]
            index_c = positions[c]
            index_d = positions[d]

            # Условия ставок
            condition1 = index_a < index_b  # Таракан A раньше B
            condition2 = index_c < index_d  # Таракан C раньше D

            # Условие: ровно одно из утверждений должно быть истинным
            if condition1 == condition2:
                valid = False
                break

        # Если все ставки выполнены, выводим результат
        if valid:
            print(" ".join(map(str, perm)))
            return

    # Если ни одна перестановка не удовлетворяет условиям
    print(0)


if __name__ == "__main__":
    main()