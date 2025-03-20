def min_lamp_groups():
    k, n, m = map(int, input().split())

    # Хеш-таблица для группировки состояний лампочек
    unique_patterns = set()

    # Читаем иероглифы и собираем состояния для каждой лампочки (i, j)
    lamp_states = {}  # (i, j) -> строка из k символов (* или .)

    for glyph in range(k):
        for i in range(n):
            row = input().strip()
            for j in range(m):
                if (i, j) not in lamp_states:
                    lamp_states[(i, j)] = []
                lamp_states[(i, j)].append(row[j])  # Добавляем текущее состояние

    # Уникальные состояния всех лампочек
    for state in lamp_states.values():
        unique_patterns.add(tuple(state))  # Кортеж уникален и удобен для set()

    # Количество уникальных групп = размер множества уникальных состояний
    print(len(unique_patterns))


# Запуск решения
min_lamp_groups()
