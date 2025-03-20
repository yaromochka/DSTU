def longest_palindromic_subsequence(s):
    n = len(s)
    if n == 0:
        return 0, ""

    # DP-таблица для хранения длины подпалиндромов
    dp = [[0] * n for _ in range(n)]
    # Заполняем базу: одиночные символы - палиндромы длины 1
    for i in range(n):
        dp[i][i] = 1

    # Заполняем DP-таблицу
    for length in range(2, n + 1):  # Длина подстроки
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    # Восстанавливаем ответ
    i, j = 0, n - 1
    palindromic_subseq = []

    while i <= j:
        if s[i] == s[j]:
            if i != j:
                palindromic_subseq.append(s[i])
            i += 1
            j -= 1
        elif dp[i + 1][j] >= dp[i][j - 1]:
            i += 1
        else:
            j -= 1

    # Добавляем вторую половину в обратном порядке
    full_palindrome = "".join(palindromic_subseq + palindromic_subseq[::-1])
    if dp[0][n - 1] % 2 == 1:  # Если палиндром нечётной длины, добавляем центральный символ
        full_palindrome = full_palindrome[:len(full_palindrome) // 2] + s[i - 1] + full_palindrome[
                                                                                   len(full_palindrome) // 2:]

    return dp[0][n - 1], full_palindrome


# Чтение строки
s = input().strip()
length, palindrome = longest_palindromic_subsequence(s)
print(length)
print(palindrome)
