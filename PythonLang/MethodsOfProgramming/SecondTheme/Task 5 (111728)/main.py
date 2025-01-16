import bisect
from typing import List, Tuple, Sequence, Union
from collections import deque


def find_first_and_last_occurrences(
        sorted_list: Sequence[int],
        search_list: Sequence[int]
) -> deque[Union[Tuple[int, int], Tuple[int]]]:
    results: deque[Union[Tuple[int, int], Tuple[int]]] = deque()

    for number in search_list:
        first_index = bisect.bisect_left(sorted_list, number)

        if first_index >= len(sorted_list) or sorted_list[first_index] != number:
            results.append((0,))
        else:
            last_index = bisect.bisect_right(sorted_list, number) - 1
            results.append((first_index + 1, last_index + 1))  # +1 для единичной нумерации

    return results


def main() -> None:
    _, _ = map(int, input().split())
    sorted_list: List[int] = list(map(int, input().split()))
    search_list: List[int] = list(map(int, input().split()))

    occurrences = find_first_and_last_occurrences(sorted_list, search_list)

    for result in occurrences:
        print(*result)


if __name__ == "__main__":
    main()