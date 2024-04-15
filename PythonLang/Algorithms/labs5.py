import random as r
import heapq as h


def heapify(numbers, i, n):
    left_i = 2 * i + 1
    right_i = 2 * i + 2
    largest_i = i
    if left_i <= n and numbers[left_i] > numbers[largest_i]:
        largest_i = left_i
    if right_i <= n and numbers[right_i] > numbers[largest_i]:
        largest_i = right_i

    if largest_i == i:
        return numbers
    else:
        numbers[largest_i], numbers[i] = numbers[i], numbers[largest_i]
        heapify(numbers, largest_i, n)


def build_max_heap(numbers):
    middle_i = len(numbers) // 2
    for i in reversed(range(0, middle_i + 1)):
        heapify(numbers, i, len(numbers) - 1)
    return numbers


def heap_sort(numbers):
    build_max_heap(numbers)
    for i in reversed(range(0, len(numbers))):
        numbers[0], numbers[i] = numbers[i], numbers[0]
        heapify(numbers, 0, i - 1)
    return numbers


def heap_create():
    b = []
    for i in range(r.randint(10, 20)):
        h.heappush(b, r.randint(1, 150))
    return b

def main():
    a = [r.randint(1, 150) for i in range(r.randint(10, 20))]
    b = heap_create()

    print(a)
    print()
    print(heap_sort(a))
    print()
    print(b)
    print()
    print(h.nsmallest(len(b), b))


if __name__ == '__main__':
    main()