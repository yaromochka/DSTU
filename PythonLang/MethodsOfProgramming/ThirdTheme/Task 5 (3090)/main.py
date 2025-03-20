from collections import deque
from itertools import product
from typing import Sequence, Iterable, List


def knapsack(n: int, m: int, weights: Sequence[int], costs: Sequence[int]) -> Iterable[int]:
    # Инициализация таблицы для динамического программирования
    distance_table: List[List[int]] = [[0] * (m + 1) for _ in range(n + 1)]

    # Заполнение таблицы
    for i, j in product(range(1, n + 1), range(m + 1)):
        distance_table[i][j] = distance_table[i - 1][j]  # Не берем текущий предмет
        if j >= weights[i] and distance_table[i - 1][j - weights[i]] + costs[i] > distance_table[i][j]:
            distance_table[i][j] = distance_table[i - 1][j - weights[i]] + costs[i]  # Берем текущий предмет

    # Восстановление набора предметов
    selected_items: deque[int] = deque()
    remaining_weight: int = m
    for i in range(n, 0, -1):
        if distance_table[i][remaining_weight] != distance_table[i - 1][remaining_weight]:  # Если предмет n был выбран
            selected_items.append(i)  # Добавляем номер предмета
            remaining_weight -= weights[i]  # Уменьшаем оставшийся вес

    selected_items.reverse()

    return selected_items


def main() -> None:
    n, m = map(int, input().split())
    weights: List[int] = [0] + list(map(int, input().split()))
    costs: List[int] = [0] + list(map(int, input().split()))

    selected_items = knapsack(n, m, weights, costs)

    # Выводим результат
    print(' '.join(map(str, selected_items)))


if __name__ == "__main__":
    main()