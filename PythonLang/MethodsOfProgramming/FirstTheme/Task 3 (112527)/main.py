from itertools import combinations, product
from typing import List, Set, Iterable, Tuple, Sequence


def find_best_broadcast(n: int, k: int, times: Sequence[int]) -> int:
    maximum_number_of_people: int = max(times)
    indexes_of_moments_when_maximum_number_of_people: Set[int] = {index for index, value in enumerate(times)
                                                                  if value == maximum_number_of_people}

    # Проверяем, можно ли транслировать два ролика в максимальные моменты
    for i, j in combinations(indexes_of_moments_when_maximum_number_of_people, 2):
        if abs(i - j) > k - 1:
            return maximum_number_of_people * 2

    # Если не удалось, ищем пред максимальный момент
    all_possible_pairs_with_a_maximum: Iterable[Tuple[int, int]] = product(
        indexes_of_moments_when_maximum_number_of_people,
        range(len(times))
    )

    pre_max_number_of_people: int = max(
        map(
            lambda index_pair: times[index_pair[1]],
            filter(
                lambda index_pair: index_pair[0] != index_pair[1] and abs(index_pair[0] - index_pair[1]) > k - 1,
                all_possible_pairs_with_a_maximum
            )
        ),
        default=0
    )

    if pre_max_number_of_people > 0:
        return maximum_number_of_people + pre_max_number_of_people

    # Если не нашли подходящие моменты, ищем альтернативный вариант
    max_viewers_sum: int = 0

    # Проходим по всем возможным начальным моментам времени для первой рекламы
    for start_time in range(n - k):
        # Вычисляем момент времени, когда может начаться вторая реклама
        second_ad_start_time: int = start_time + k
        if second_ad_start_time < n:
            # Суммируем количество покупателей в момент начала первой рекламы
            # и максимальное количество покупателей в момент времени после первой рекламы
            viewers_sum: int = times[start_time] + max(times[second_ad_start_time:n])
            max_viewers_sum = max(max_viewers_sum, viewers_sum)

    return max_viewers_sum


def main() -> None:
    n, k = map(int, input().split())
    times: List[int] = list(map(int, input().split()))
    result: int = find_best_broadcast(n, k, times)
    print(result)


if __name__ == "__main__":
    main()