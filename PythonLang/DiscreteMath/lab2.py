from math import log2


def polynom_print(vect):
    answer = ''
    if vect[0] == '1': answer += '1 ⊕  '
    for i in range(1, len(vect)):
        temp = ''
        doub = bin(i)[2::].zfill(int(log2(len(vect))))
        for j in range(len(doub)):
            temp += (f'x{(j + 1) % (int(log2(len(vect))) + 1)}' * int(doub[j]))
        temp *= int(vect[i])
        if len(temp) != 0:
            answer += f'{temp} ⊕  '
    return answer.rstrip('⊕ ')


def vect_polinom(vect):
    rvect = vect[:]
    vectors = []
    vectors.append(rvect)
    for _ in range(len(rvect) - 1):
        temp = ''
        for j in range(len(rvect) - 1):
            temp += str(int(rvect[j]) ^ int(rvect[j + 1]))
        vectors.append(temp)
        rvect = temp
        print(temp)
    return ''.join([i[0] for i in vectors])


def rev_triangle(vect):
    print('--- Построение вектора из полинома Жегалкина ---')
    print(vect_polinom(vect))


def triangle(vect):
    print('--- Нахождение полинома Жегалкина через треугольник ---')
    ans_str = vect_polinom(vect)
    print(polynom_print(ans_str))
    rev_triangle(ans_str)


def fft(vect):
    temp, ans = [i for i in vect], []
    print(*temp)
    for _ in range(1, int(log2(len(vect)) + 1)):
        for i, j in enumerate(temp):
            if i % 2 == 0: b = j
            else: ans.append(b + ''.join(str(int(c) ^ int(d)) for c,d in zip(j, b)))
        temp, ans = ans, []
        print(*temp)
    print(polynom_print(''.join(temp)))
    return temp
    

def main():
    s = input('Введите вектор, полином которого хотите найти: ')
    if any(i not in '10' for i in s) or (log2(len(s)) != int(log2(len(s)))): 
        print('Неверно введён вектор')
        exit()
    triangle(s)
    print('--- Построение полинома Жегалкина через БПФ ---')
    temp = fft(s)
    print('--- Построение вектора из БПФ ---')
    print(fft(''.join(temp)))


if __name__ == '__main__':
    main()