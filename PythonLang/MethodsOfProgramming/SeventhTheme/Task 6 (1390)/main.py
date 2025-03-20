def count_symmetric_submatrices():
    # Читаем ввод
    N, M = map(int, input().split())
    grid = [input().strip() for _ in range(N)]

    count = 0  # Счётчик симметричных частей

    # Перебираем все возможные центры симметрии
    for r in range(N):
        for c in range(M):
            # Проверяем симметричные прямоугольники, расширяя их
            for size in range(min(N - r, M - c)):  # Размер увеличиваем до границ
                r1, c1 = r - size, c - size  # Верхний левый угол
                r2, c2 = r + size, c + size  # Нижний правый угол
                if r1 < 0 or c1 < 0 or r2 >= N or c2 >= M:
                    break  # Выходим, если вышли за границы
                # Проверяем симметричность
                symmetric = True
                for i in range((r2 - r1 + 1) // 2):
                    if grid[r1 + i][c1:c2 + 1] != grid[r2 - i][c1:c2 + 1][::-1]:  # Строки
                        symmetric = False
                        break
                for j in range((c2 - c1 + 1) // 2):
                    for i in range(r1, r2 + 1):
                        if grid[i][c1 + j] != grid[i][c2 - j]:  # Столбцы
                            symmetric = False
                            break
                if symmetric:
                    count += 1

    print(count)


# Запуск
count_symmetric_submatrices()
