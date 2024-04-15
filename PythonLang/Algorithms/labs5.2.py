from labs1 import selection_sort
from labs2 import binary_search
from labs3 import lab_work3
from labs4 import alg_dejikstra, matr
from labs5 import heap_sort
import random as r


def main():
    a = [r.randint(10, 150) for i in range(r.randint(10, 20))]
    print(a)
    print(selection_sort(a))
    try:
        print(a)
        n = int(input('Введите число, которое ищем: '))
        print(binary_search(a, n, 0, len(a)))
    except ValueError:
        print('ЧИСЛО ВВОДИТЬ НАДО')
    lab_work3(1) # 2 3 8 7 2 / - * +
    try:
        m = int(input('Введите количесиво вершин: '))
        l = matr(m)
        print(l)
        first = input(f'Введите точку начала (от A до {(chr(ord("A") + m - 1))}): ')
        second = input(f'Введите точку конца (от A до {(chr(ord("A") + m - 1))}): ')
        alg_dejikstra(first, second, l)
    except ValueError:
        print('ВВОДИТЬ ЧИСЛО НАДО')
    b = [r.randint(10, 150) for i in range(r.randint(10, 20))]
    print(b)
    print(heap_sort(b))

if __name__ == '__main__':
    main()