import sys

# Оптимизированный порядок ходов по кругу (основан на стратегии Варндорфа)
MOVES = [(2, 1), (1, 2), (-1, 2), (-2, 1),
         (-2, -1), (-1, -2), (1, -2), (2, -1)]

def is_valid(x, y, n, board):
    """ Проверяет, можно ли поставить коня в клетку (x, y) """
    return 0 <= x < n and 0 <= y < n and board[x][y] == -1

def get_possible_moves(x, y, n, board):
    """ Возвращает возможные ходы, отсортированные по стратегии Варндорфа """
    moves = []
    for dx, dy in MOVES:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny, n, board):
            count = sum(is_valid(nx + dx2, ny + dy2, n, board) for dx2, dy2 in MOVES)
            moves.append((count, nx, ny))
    return sorted(moves)  # Сортируем по числу возможных будущих ходов

def solve_knights_tour(n):
    """ Решает задачу обхода коня """
    board = [[-1] * n for _ in range(n)]  # Заполняем доску -1 (не посещено)
    board[0][0] = 1  # Начинаем с (0,0), но с 1

    if not backtrack(0, 0, 2, n, board):  # Начинаем с 2, так как 1 уже стоит
        print(0)  # Если решения нет, выводим 0
    else:
        print(1)
        for row in board:
            print(" ".join(map(str, row)))  # Выводим матрицу

def backtrack(x, y, move_num, n, board):
    """ Рекурсивно находит путь коня по шахматной доске """
    if move_num > n * n:
        return True  # Все клетки посещены

    for _, nx, ny in get_possible_moves(x, y, n, board):
        board[nx][ny] = move_num
        if backtrack(nx, ny, move_num + 1, n, board):
            return True
        board[nx][ny] = -1  # Откат хода (backtracking)

    return False  # Нет возможных ходов

# Читаем входное число n
n = int(sys.stdin.readline().strip())
solve_knights_tour(n)
