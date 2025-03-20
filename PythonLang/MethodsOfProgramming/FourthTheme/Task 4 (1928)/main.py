from typing import List, Tuple, Sequence
from collections import deque


def produce_part(
        part_id: int,
        production_times: Sequence[int],
        dependencies: Sequence[Sequence[int]],
        produced: List[bool],
        production_order: deque[int]
) -> int:
    if produced[part_id]:
        return 0

    produced[part_id] = True
    total_time = production_times[part_id]  # Время на изготовление текущей детали

    for dependency in dependencies[part_id - 1]:  # Индексация зависит от 0
        total_time += produce_part(dependency, production_times, dependencies, produced, production_order)

    production_order.append(part_id)
    return total_time


def calculate_minimum_production_time(
        n: int,
        production_times: Sequence[int],
        dependencies: Sequence[Sequence[int]]
) -> Tuple[int, Sequence[int]]:
    produced: List[bool] = [False] * (n + 1)
    production_order: deque[int] = deque()

    total_time: int = produce_part(1, production_times, dependencies, produced, production_order)

    return total_time, production_order


def main() -> None:
    n: int = int(input())
    production_times: List[int] = [0] + list(map(int, input().split()))
    dependencies: List[List[int]] = [list(map(int, input().split()[1:])) for _ in range(n)]

    total_time, order = calculate_minimum_production_time(n, production_times, dependencies)

    print(total_time, len(order))
    print(*order)


if __name__ == "__main__":
    main()