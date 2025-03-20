import sys
from collections import deque, OrderedDict

def main():
    input = sys.stdin.read
    data = input().splitlines()

    # Читаем входные данные
    n, m = map(int, data[0].split())

    # Изначальный порядок солдат
    soldiers = deque(range(1, n + 1))
    positions = OrderedDict((i, i) for i in range(1, n + 1))

    # Обрабатываем команды
    for i in range(1, m + 1):
        l, r = map(int, data[i].split())

        # Находим отряд для перемещения
        moving = []
        for key in list(positions.keys()):
            if l <= positions[key] <= r:
                moving.append(key)
                del positions[key]

        # Перемещаем в начало
        soldiers = deque(moving) + soldiers

        # Обновляем позиции
        new_positions = OrderedDict()
        for idx, soldier in enumerate(soldiers):
            new_positions[soldier] = idx + 1
        positions = new_positions

    # Выводим итоговый порядок
    sys.stdout.write(" ".join(map(str, soldiers)) + "\n")


if __name__ == "__main__":
    main()
