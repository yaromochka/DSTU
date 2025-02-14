def can_place_cows(stalls, k, min_dist):
    count = 1  # Ставим первую корову в первое стойло
    last_placed = stalls[0]

    for i in range(1, len(stalls)):
        if stalls[i] - last_placed >= min_dist:
            count += 1
            last_placed = stalls[i]
            if count == k:
                return True  # Все коровы успешно размещены

    return False

def find_max_min_dist(stalls, k):
    stalls.sort()  # Координаты стойл идут в порядке возрастания
    low, high = 1, stalls[-1] - stalls[0]  # Границы бинарного поиска
    result = 0

    while low <= high:
        mid = (low + high) // 2  # Проверяем текущее среднее расстояние

        if can_place_cows(stalls, k, mid):
            result = mid  # Запоминаем лучший вариант
            low = mid + 1  # Пробуем большее расстояние
        else:
            high = mid - 1  # Пробуем меньшее расстояние

    return result

# Читаем входные данные
n, k = map(int, input().split())
stalls = list(map(int, input().split()))

# Выводим результат
print(find_max_min_dist(stalls, k))
