import random as r


def quick_sort(a):
    if len(a) <= 1:
        return a
    else:
        q = r.choice(a)
        lnum = []
        mnum = []
        rnum = []
        for i in a:
            if i < q:
                lnum.append(i)
            elif i == q:
                mnum.append(i)
            else:
                rnum.append(i)
        return quick_sort(lnum) + mnum + quick_sort(rnum)


def merge(left, right):
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    result += left[l:]
    result += right[r:]

    return result


def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)


def binary_search(array, element, start, end):
    # end -= 1
    if start > end:
        return 'Элемент в массиве не найден'
    mid = (start + end) // 2
    if element == array[mid]:
        return mid
    elif element < array[mid]:
        return binary_search(array, element, start, mid - 1)
    else:
        return binary_search(array, element, mid + 1, end)

""" ЗАДАНИЕ 1"""
# n, m = map(int, input().split())
# a = [[r.randint(-100, 100) for i in range(n)] for j in range(m)]
# [print(*row) for row in a]
# print()
# b = [[] for j in range(m)]
# for i in range(n):
#     temp = []
#     for j in range(m):
#         temp.append(a[j][i])
#     temp = quick_sort(temp)
#     for j in range(m):
#         b[j].append(temp[j])
# [print(*row) for row in b]

""" ЗАДАНИЕ 2 """
# a = [r.randint(-100, 100) for i in range(50)]
# print(a)
# print(merge_sort(a))

# """ ЗАДАНИЕ 3 """
# a = [r.randint(-100, 100) for i in range(r.randint(10, 50))]
# a = quick_sort(a)
# print(a)
# n = int(input())
# print(binary_search(a, n, 0, len(a)))