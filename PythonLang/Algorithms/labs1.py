import time as t
import random as r


def bubble_sort(array):
    start = t.time()
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array, t.time() - start


def insert_sort(array):
    start = t.time()
    for i in range(1, len(array)):
        current = array[i]
        j = i - 1
        while j >= 0 and current < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = current
    return array, t.time() - start


def selection_sort(array):
    start = t.time()
    for i in range(len(array) - 1):
        m = i
        for j in range(i + 1, len(array)):
            if array[j] < array[m]:
                m = j
        array[i], array[m] = array[m], array[i]
    return array, t.time() - start


def main():
    a = [r.randint(-100, 100) for i in range(r.randrange(1, 40))]
    print(f'Несортированный массив: {a}')
    print(f'Сортировка пузырьком: {bubble_sort(a)}')
    print(f'Сортировка вставкой: {insert_sort(a)}')
    print(f'Сортировка выбором: {selection_sort(a)}')


if __name__ == '__main__':
    main()
