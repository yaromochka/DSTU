from collections import deque

# Все возможные ходы коня
MOVES = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
         (1, -2), (1, 2), (2, -1), (2, 1)]


def to_coords(pos):
    """Преобразует шахматную нотацию в координаты (x, y)."""
    return ord(pos[0]) - ord('a'), int(pos[1]) - 1


def bfs(start):
    """Запускает BFS от заданной клетки и возвращает словарь минимальных расстояний."""
    queue = deque([(start[0], start[1], 0)])  # (x, y, шаги)
    visited = {start: 0}

    while queue:
        x, y, steps = queue.popleft()

        for dx, dy in MOVES:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8 and (nx, ny) not in visited:
                visited[(nx, ny)] = steps + 1
                queue.append((nx, ny, steps + 1))

    return visited


def min_meeting_steps(start1, start2):
    """Находит минимальное количество шагов, за которое оба коня могут оказаться на одной клетке."""
    dist1 = bfs(start1)
    dist2 = bfs(start2)

    # Ищем минимальный шаг, на котором оба коня могут встретиться
    min_steps = float('inf')

    for pos in dist1:
        if pos in dist2:
            max_time = max(dist1[pos], dist2[pos])
            if dist1[pos] == dist2[pos]:  # Должны попасть в одно время
                min_steps = min(min_steps, max_time)

    return min_steps if min_steps != float('inf') else -1


# Читаем входные данные
start1, start2 = input().split()
coords1, coords2 = to_coords(start1), to_coords(start2)

# Выводим ответ
print(min_meeting_steps(coords1, coords2))
