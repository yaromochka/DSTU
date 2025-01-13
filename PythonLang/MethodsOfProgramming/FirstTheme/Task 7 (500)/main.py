from typing import List, Tuple


def time_to_minutes(hours: int, minutes: int) -> int:
    return hours * 60 + minutes


def minutes_to_time(minutes: int) -> (int, int):
    return minutes // 60, minutes % 60


def barbershop_schedule(n: int, arrivals: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    master_free = [0, 0, 0]
    results = []
    for arrival in arrivals:
        arrival_minutes = time_to_minutes(*arrival)
        # Находим мастера, который освободится раньше всех
        earliest_master = min(range(3), key=lambda i: master_free[i])
        start_time = max(arrival_minutes, master_free[earliest_master])
        # Обновляем время, когда мастер освободится
        master_free[earliest_master] = start_time + 30
        # Добавляем время выхода клиента
        results.append(minutes_to_time(start_time + 30))
    return results


def main():
    # Чтение входных данных
    n = int(input())
    arrivals = [tuple(map(int, input().split())) for _ in range(n)]
    # Получение результата
    results = barbershop_schedule(n, arrivals)
    # Вывод результата
    for result in results:
        print(result[0], result[1])


if __name__ == "__main__":
    main()
