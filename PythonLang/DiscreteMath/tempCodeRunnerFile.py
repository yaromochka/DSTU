    answer = ''
    if ans_str[0] == '1': answer += '1 ⊕  '
    for i in range(1, len(ans_str)):
        temp = ''
        doub = bin(i)[2::].zfill(int(log2(len(vect))))
        for j in range(len(doub)):
            temp += (f'x{i + 1}' * int(doub[j]))
        temp *= int(ans_str[0])
        if len(temp) != 0:
            answer += f'{temp} ⊕  '
    print(answer)
