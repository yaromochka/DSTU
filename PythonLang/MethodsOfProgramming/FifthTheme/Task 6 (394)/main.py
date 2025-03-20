from typing import List, Sequence, Tuple


def hungarian(cost_matrix: Sequence[Sequence[int]]) -> Sequence[Tuple[int, int]]:
    num_tasks = len(cost_matrix)
    row_potentials = [0] * num_tasks  # Потенциалы строк
    col_potentials = [0] * num_tasks  # Потенциалы столбцов
    task_assignment = [-1] * num_tasks  # Связи (назначения) задач для каждого столбца

    for row in range(num_tasks):
        min_costs = [float('inf')] * num_tasks  # Минимальные стоимости для столбцов
        visited_columns = [False] * num_tasks  # Посещённые столбцы
        previous_columns = [-1] * num_tasks  # Предыдущие столбцы в цепочке
        current_row = row
        current_column = -1

        while current_row != -1:
            delta = float('inf')
            next_column = -1

            # Обновляем минимальные стоимости и находим наименьшую стоимость
            for col in filter(lambda x: not visited_columns[x], range(num_tasks)):
                reduced_cost = (
                        cost_matrix[current_row][col]
                        - row_potentials[current_row]
                        - col_potentials[col]
                )
                if reduced_cost < min_costs[col]:
                    min_costs[col] = reduced_cost
                    previous_columns[col] = current_column
                if min_costs[col] < delta:
                    delta = min_costs[col]
                    next_column = col

            # Корректируем потенциалы строк и столбцов
            for col in range(num_tasks):
                if visited_columns[col]:
                    row_potentials[task_assignment[col]] += delta
                    col_potentials[col] -= delta
                else:
                    min_costs[col] -= delta

            row_potentials[row] += delta
            visited_columns[next_column] = True
            current_column = next_column
            current_row = task_assignment[current_column]

        # Обновляем цепочку назначений
        while previous_columns[current_column] != -1:
            task_assignment[current_column] = task_assignment[previous_columns[current_column]]
            current_column = previous_columns[current_column]

        task_assignment[current_column] = row

    # Формируем список назначений
    return [(task_assignment[col], col) for col in range(num_tasks)]


def main() -> None:
    k: int = int(input())
    matrix: List[List[int]] = [list(map(int, input().split())) for _ in range(k)]
    result: Sequence[Tuple[int, int]] = hungarian(matrix)

    # Считаем минимальное время
    total_time: int = sum(matrix[row][col] for row, col in result)
    print(total_time)


if __name__ == "__main__":
    main()