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
        for j in range(i + 1, len(array) - 1):
            if array[j] < array[m]:
                m = j
        array[i], array[m] = array[m], array[i]
    return array, t.time() - start


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
    end -= 1
    if start > end:
        return 'Элемент в массиве не найден'
    mid = (start + end) // 2
    if element == array[mid]:
        return mid
    elif element < array[mid]:
        return binary_search(array, element, start, mid - 1)
    else:
        return binary_search(array, element, mid + 1, end)


def lab_work1():
    a = [r.randint(-100, 100) for i in range(r.randrange(1, 40))]
    print(f'Несортированный массив: {a}')
    print(f'Сортировка пузырьком: {bubble_sort(a)}')
    print(f'Сортировка вставкой: {insert_sort(a)}')
    print(f'Сортировка выбором: {selection_sort(a)}')



def lab_work2(c):
    if c == 1:
        n, m = map(int, input('Введите два числа: ').split())
        a = [[r.randint(-100, 100) for i in range(n)] for j in range(m)]
        [print(*row) for row in a]
        print()
        b = [[] for j in range(m)]
        for i in range(n):
            temp = []
            for j in range(m):
                temp.append(a[j][i])
            temp = quick_sort(temp)
            for j in range(m):
                b[j].append(temp[j])
        [print(*row) for row in b]
    elif c == 2:
        a = [r.randint(-100, 100) for i in range(50)]
        print(a)
        print(merge_sort(a))
    elif c == 3:
        a = [r.randint(-100, 100) for i in range(50)]
        a = quick_sort(a)
        print(a)
        n = int(input('Введите число, которое хотите найти в массиве'))
        print(binary_search(a, n, 0, len(a)))
    else:
        print('Неверный номер задания: ')


def isDigit(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

def lab_work3(c):
    if c == 1:
        flag = True
        a = []
        s = input('Введите скобочную последовательность: ')
        for i in s:
            if i in '{[(':
                a.append(i)
            elif i in '}])':
                if not a:
                    flag = False
                    break
                temp = a.pop()
                if temp == '(' and i == ')':
                    continue
                if temp == '[' and i == ']':
                    continue
                if temp == '{' and i == '}':
                    continue
                flag = False
                break
        if flag and len(a) == 0:
            print('Скобочная последовательность правильная')
        else:
            print('Скобочная последовательность неправильная')
    elif c == 2:
        s = input('Введите обратную польскую нотацию: ')
        a = []
        flag = True
        for symbol in s.split():
            if isDigit(symbol):
                a.append(float(symbol))
            else:
                if len(a) == 0:
                    flag = False
                    break
                if symbol == '*':
                    a.append(a.pop() * a.pop())
                elif symbol == '+':
                    a.append(a.pop() + a.pop())
                elif symbol == '-':
                    i = a.pop()
                    j = a.pop()
                    a.append(j - i)
                elif symbol == '/':
                    i = a.pop()
                    j = a.pop()
                    a.append(j / i)
        if flag:
            print(*a)

            print(2 + 3.321312 * (8 - 7.32142512 / 2))
        else:
            print('Что-то странное 0_о')
    else:
        print('Неверный номер задания: ')



def main():
    a = int(input('Введите номер лабораторной: '))
    while a != 0:
        if a == 1:
            lab_work1()
        elif a == 2:
            b = int(input('Введите номер задания: '))
            lab_work2(b)
        elif a == 3:
            b = int(input('Введите номер задания: '))
            lab_work3(b)
        else:
            print('Неверный номер лабораторной')
        a = int(input('Введите номер лабораторной: '))

#
# if __name__ == '__main__':
#     main()