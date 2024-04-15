import random


def bubble(s):
    n = len(s)
    for i in range(n):
        for j in range(n - i - 1):
            if s[j] > s[j + 1]:
                s[j], s[j + 1] = s[j + 1], s[j]
    return s


def riddle(n):
    s = [i for i in range(n + 1)]
    for i in s:
        if i > 1:
            for j in range(2 * i, len(s), i):
                s[j] = 0
    return s


def binary_search(array, element, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if element == array[mid]:
        return mid + 1
    if element < array[mid]:
        return binary_search(array, element, start, mid - 1)
    else:
        return binary_search(array, element, mid + 1, end)


def second_binary_search(array, element):
    start = step = 0
    end = len(array)

    while (start <= end):
        step += 1
        mid = (start + end) // end

        if element == array[mid]:
            return mid

        if element < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1

#
# el = 52
# arr = [421, 52, 56, 4124, 942]
# print(second_binary_search(arr, el))



# v = int(input())
# t = int(input())