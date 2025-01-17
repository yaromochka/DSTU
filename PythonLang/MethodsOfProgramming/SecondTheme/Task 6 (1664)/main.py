from collections import Counter
from typing import List, Generator


def count_partitions(numbers: List[int]) -> Generator[int, None, None]:
    count_map = Counter(numbers)  # Подсчитываем количество каждого числа

    for number in numbers:
        count = sum(
            count_map[x] * (count_map[x] - 1) // 2 if x == (number - x) else count_map[x] * count_map.get(number - x, 0)
            for x in count_map
            if x <= number // 2  # Условие для x, чтобы избежать дублирования
        )
        yield count


def main():
    n = int(input())
    numbers = [int(input()) for _ in range(n)]

    partitions = count_partitions(numbers)

    for result in partitions:
        print(result)


if __name__ == "__main__":
    main()