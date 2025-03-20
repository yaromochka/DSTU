from typing import List


def max_gold_weight(capacity: int, weights: list) -> int:
    # Инициализация массива для хранения достижимых весов
    achievable_weights: List[int] = [0] * (capacity + 1)
    achievable_weights[0] = 1  # Нулевой вес всегда достижим

    # Проходим по каждому слитку
    for weight in weights:
        # Обновляем массив достижимых весов в обратном порядке
        for current_capacity in range(capacity, weight - 1, -1):
            if achievable_weights[current_capacity - weight] == 1:
                achievable_weights[current_capacity] = 1

    # Находим максимальный вес, который можно унести
    for i in range(capacity, -1, -1):
        if achievable_weights[i] == 1:
            return i  # Возвращаем максимальный вес

    return 0  # Если ничего не удалось унести


def main() -> None:
    capacity, n = map(int, input().split())
    weights: List[int] = list(map(int, input().split()))

    max_weight: int = max_gold_weight(capacity, weights)
    print(max_weight)


if __name__ == "__main__":
    main()