from typing import List, Sequence


def fill_matrix(n: int, m: int) -> Sequence[Sequence[int]]:
    matrix: List[List[int]] = [[0 for _ in range(m)] for _ in range(n)]
    count: int = 0

    for index_of_diagonal in range(n + m - 1):
        start_col: int
        start_row: int

        if index_of_diagonal < m:
            start_col = index_of_diagonal
            start_row = 0
        else:
            start_col = m - 1
            start_row = index_of_diagonal - m + 1

        while start_col >= 0 and start_row < n:
            matrix[start_row][start_col] = count
            count += 1
            start_col -= 1
            start_row += 1

    return matrix


def main() -> None:
    n, m = map(int, input().strip().split())
    matrix = fill_matrix(n, m)

    for row in matrix:
        print(' '.join(f'{num:3d}' for num in row))


if __name__ == "__main__":
    main()