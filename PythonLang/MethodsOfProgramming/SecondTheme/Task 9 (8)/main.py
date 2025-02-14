def solve():
    s = input().strip()
    n = len(s)
    x = [int(c) for c in s]

    blocks = [[]]
    cur_block = 0
    cnt = [False] * 10

    # Разбиваем число на блоки
    for i in range(n - 1, -1, -1):
        cnt[x[i]] = True
        blocks[cur_block].append(x[i])

        if all(cnt):  # Если все цифры встречены хотя бы раз
            cur_block += 1
            blocks.append([])
            cnt = [False] * 10

    # Разворачиваем каждый блок
    for i in range(cur_block + 1):
        blocks[i].reverse()

    # Заполняем последний блок
    cnt = [False] * 10
    for num in blocks[cur_block]:
        cnt[num] = True

    # Определяем первую цифру результата
    first_digit = next((j for j in range(1, 10) if not cnt[j]), 0)

    if first_digit == 0:
        print(10, end="")
    else:
        print(first_digit, end="")

    cur_digit = first_digit

    # Обрабатываем оставшиеся блоки
    for i in range(cur_block - 1, -1, -1):
        cnt = [False] * 10
        found = False

        for digit in blocks[i]:
            if not found:
                if digit == cur_digit:
                    found = True
                continue
            cnt[digit] = True

        next_digit = next(j for j in range(10) if not cnt[j])
        print(next_digit, end="")
        cur_digit = next_digit


# Вызов функции
solve()
