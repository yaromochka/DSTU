def matr(m):
    matr = {}
    for i in range(1, m + 1):
        for j in range(i + 1, m + 1):
            a = input(f'Введите расстояние между вершиной {chr(ord("A") + i - 1)} и {chr(ord("A") + j - 1)} (если связи нет введите {0}): ')
            if a != '0':
                try:
                    matr[chr(ord("A") + i - 1)].update({f'{chr(ord("A") + j - 1)}': int(a)})
                except KeyError:
                    matr[chr(ord("A") + i - 1)] = {f'{chr(ord("A") + j - 1)}': int(a)}
                try:
                    matr[chr(ord("A") + j - 1)].update({f'{chr(ord("A") + i - 1)}': int(a)})
                except KeyError:
                    matr[chr(ord("A") + j - 1)] = {f'{chr(ord("A") + i - 1)}': int(a)}
    # print('  ', end='')
    # [print(chr(ord('A') + i), end=' ') for i in range(m)]
    # print()
    # [print(chr(ord('A') + i)) for i in range(m)]
    return matr


def graph():
    global n
    n = int(input('Введите количесиво вершин: '))
    matr = [['0' for i in range(1, n + 1)] for j in range(1, n + 1)]
    lst = {}
    temp = [[] * width for width in range(n)]
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            a = input(f'Есть связь между вершиной {i} и {j}? (yes/no): ')
            if a.lower() == 'да' or a.lower() == 'yes':
                matr[i - 1][j - 1] = '1'
                matr[j - 1][i - 1] = '1'
                temp[i - 1].append(j)
                temp[j - 1].append(i)
    for i in range(n):
        for j in range(n):
            lst[i + 1] = temp[i]
            lst[j + 1] = temp[j]
    print('  ', end='')
    [print(chr(ord('A') + i), end=' ') for i in range(n)]
    print()
    [print(chr(ord('A') + i), *matr[i]) for i in range(n)]
    return lst


def depth_first_search(start, end, graph, way, visited):
    if len(way) == 0:
        way.append(start)
        visited.add(start)

    if start == end:
        return print(f'{way}, а количество рёбер - {len(way) - 1}')

    for next in set(graph[start]) - visited:
        way.append(next)
        visited.add(next)
        depth_first_search(next, end, graph, way, visited)
        way.pop()
        visited.remove(next)
        

def alg_dejikstra(start, end, graph):
    shortest = {i: float('inf') for i in graph}
    shortest[start] = 0
    path = {}
    travel = []

    while len(graph) > 0:
        minimal = None
        for current in graph:
            if minimal == None:
                minimal = current
            elif shortest[minimal] > shortest[current]:
                minimal = current
        for node, value in graph[minimal].items():
            if value + shortest[minimal] < shortest[node]:
                shortest[node] = value + shortest[minimal]
                path[node] = minimal
        graph.pop(minimal)

    while end != start:
        try:
            travel.insert(0, end)
            end = path[end]
        except:
            print('Связи между точками нет')
            break
    travel.insert(0, start)
    if shortest[minimal] != float('inf'):
        return print(f'Минимальный путь - {travel}, а самая минимальная сумма - {shortest[minimal]}')



def main():
    try:
        number = int(input('Введите номер задания: '))
    except ValueError:
        print('ВВОДИТЬ ЧИСЛО НАДО')
        exit()
    if number == 1:
        l = graph()
        print(l)
        first = int(input(f'Введите точку начала (от 1 до {n}): '))
        second = int(input(f'Введите точку конца (от 1 до {n}): '))
        depth_first_search(first, second, l, [], set())
    elif number == 2:
        try:
            m = int(input('Введите количесиво вершин: '))
            l = matr(m)
            print(l)
            first = input(f'Введите точку начала (от A до {(chr(ord("A") + m - 1))}): ')
            second = input(f'Введите точку конца (от A до {(chr(ord("A") + m - 1))}): ')
            alg_dejikstra(first, second, l)
        except ValueError:
            print('ВВОДИТЬ ЧИСЛО НАДО')
    else:
        print('Неверный номер задания')


if __name__ == '__main__':
    main()