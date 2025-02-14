def can_cut(wires, k, length):
    """Проверяет, можно ли нарезать хотя бы k отрезков длиной length."""
    count = sum(wire // length for wire in wires)
    return count >= k


def max_wire_length(n, k, wires):
    """Бинарный поиск для нахождения максимальной длины куска."""
    low, high = 1, max(wires)  # Границы поиска
    result = 0

    while low <= high:
        mid = (low + high) // 2  # Проверяем среднее значение

        if can_cut(wires, k, mid):
            result = mid  # Обновляем результат
            low = mid + 1  # Пробуем нарезать куски побольше
        else:
            high = mid - 1  # Пробуем нарезать куски поменьше

    return result


# Читаем входные данные
n, k = map(int, input().split())
wires = [int(input()) for _ in range(n)]

# Выводим максимальную возможную длину
print(max_wire_length(n, k, wires))
