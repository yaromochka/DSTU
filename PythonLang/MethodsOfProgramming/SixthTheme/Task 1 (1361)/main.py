from collections import deque
from typing import cast, Tuple, List, Iterable, Sequence


def is_available(
        segments: Sequence[int],
        start: int,
        end: int,
        k: int
) -> bool:
    """Проверяет, есть ли хотя бы одно свободное место на участке [x, y)."""
    return all(segments[i] < k for i in range(start, end))


def process_requests(
        count_of_stations: int,
        count_of_seats: int,
        requests: Iterable[Tuple[int, int]]
) -> Iterable[int]:
    """Обрабатывает все запросы на продажу билетов."""
    segments: List[int] = [0] * (count_of_stations + 1)  # Инициализируем массив мест
    results: deque[int] = deque()

    for start_station, end_station in requests:
        if is_available(segments, start_station, end_station, count_of_seats):
            # Если есть свободное место, продаем билет и увеличиваем занятые места
            for i in range(start_station, end_station):
                segments[i] += 1
            results.append(1)
        else:
            results.append(0)

    return results


def main() -> None:
    n, k, m = map(int, input().split())
    requests: List[Tuple[int, int]] = cast(List[Tuple[int, int]], [tuple(map(int, input().split())) for _ in range(m)])

    results = process_requests(n, k, requests)
    print(*results, sep='\n')


if __name__ == "__main__":
    main()
