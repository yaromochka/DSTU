import sys


def replace_on_the_list(hat, res_list):
    for i in range(len(hat)):
        hat[i] = list(hat[i])
        res_list.append(hat[i])
    return res_list


def check(term, not_term, res_list):
    for k in range(len(res_list)):
        for i in res_list[k]:
            if i not in term or i not in not_term:
                print(f'Ошибка!')
                sys.exit()


def distribution_on_the_part(rules, length, left_part, right_part, ind):
    for i in range(length):
        if rules[i] == '>':
            left_part.append(rules[i - 1])
            ind = i + 1
        elif rules[i] == ',':
            # print(ind, i)
            for j in range(ind, i):
                if rules[j] == '|':
                    continue
                else:
                    right_part.append(rules[j])
            ind -= 2


if __name__ == '__main__':

    left, right, buff_right, buff_left = [], [], [], []
    ind, kz, ks, gen_form, pl, s, count = 1, 0, 0, 0, 0, 0, 0

    not_term = input('Введите нетерминалы: ')
    term = input('Введите терминалы: ')
    buff_rules = input('Введите правило по типу N -> T\n').split('->')
    length = len(buff_rules)
    if buff_rules[0] != 'S':
        print('Первое правило должно начинаться с S')
        sys.exit()
    print(left, right)

    distribution_on_the_part(buff_rules, length, left, right, ind)
    replace_on_the_list(right, buff_right)
    check(term, not_term, buff_right)
    replace_on_the_list(left, buff_left)
    check(term, not_term, buff_left)

    for i in range(len(left)):
        print(left[i], ord(left[i][0]))
        if len(left[i]) <= len(right[i]):
            kz += 1
        if len(left[i][0]) == 1 and 97 > ord(left[i][0]) > 64:
            ks += 1

    for j in range(len(right)):
        print((right[j]))
        if len(right[0]) != 1:
            continue
        k = right[j][0]
        if (97 > ord(k[-1]) > 64) or ord(right[j][0]) == 43 or ord(right[j][0]) == 45:
            pl += 1
        if (97 > ord(right[j][0]) > 64) or ord(right[j][0]) == 43 or ord(right[j][0]) == 45:
            gen_form += 1

    print(kz, ks, gen_form, pl)
    if kz == len(left) and ks == len(left) and (gen_form == len(right) or gen_form == 0) and (
            pl == len(right) or gen_form == 0): print('Тип 3. Регулярная грамматика')

    elif kz == len(left) and ks == len(left) and gen_form < len(right) and pl < len(right): print('Тип 2. Контекстно-свободная грамматика')

    elif kz == (len(left)) and ks < (len(left)) and gen_form < len(right) and pl < len(right):
        print('Тип 1. Контекстно-зависимая грамматика')

    else:
        print('Тип 0. Неограниченная грамматика')
