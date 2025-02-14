def find_best_outfit():
    # Читаем и сортируем 4 списка цветов
    items = []
    for _ in range(4):
        n = int(input())  # Количество элементов (можно не использовать)
        colors = list(map(int, input().split()))
        items.append(sorted(colors))  # Сортируем список цветов

    # Указатели на текущие элементы в списках
    p1, p2, p3, p4 = 0, 0, 0, 0
    best_diff = float('inf')
    best_combination = (0, 0, 0, 0)

    # Двигаемся по отсортированным спискам
    while p1 < len(items[0]) and p2 < len(items[1]) and p3 < len(items[2]) and p4 < len(items[3]):
        # Текущие выбранные цвета
        c1, c2, c3, c4 = items[0][p1], items[1][p2], items[2][p3], items[3][p4]

        # Найти минимальный и максимальный цвета в текущем наборе
        min_color = min(c1, c2, c3, c4)
        max_color = max(c1, c2, c3, c4)
        diff = max_color - min_color

        # Обновляем лучший найденный комплект
        if diff < best_diff:
            best_diff = diff
            best_combination = (c1, c2, c3, c4)

        # Если разница уже 0, это идеальный случай — прерываемся
        if best_diff == 0:
            break

        # Сдвигаем указатель у списка с минимальным значением
        if min_color == c1:
            p1 += 1
        elif min_color == c2:
            p2 += 1
        elif min_color == c3:
            p3 += 1
        else:
            p4 += 1

    # Выводим лучший найденный комплект
    print(*best_combination)


def main() -> None:
    find_best_outfit()


if __name__ == "__main__":
    main()