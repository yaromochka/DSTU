from typing import List, Iterable


def restore_tournament_table(num_teams: int, points: List[int]) -> Iterable[Iterable[int]]:
    # Инициализация таблицы результатов
    tournament_table: List[List[int]] = [[0] * num_teams for _ in range(num_teams)]

    # Индексы команд
    team_indices = range(num_teams)

    for i in range(num_teams - 1):
        # Сортируем команды по очкам
        sorted_points, sorted_indices = zip(*sorted(zip(points, team_indices)))
        sorted_points: List[int] = list(sorted_points)
        sorted_indices: List[int] = list(sorted_indices)

        for j in range(i + 1, num_teams):
            if tournament_table[sorted_indices[i]][sorted_indices[j]] > 0:
                continue
            elif sorted_points[i] > 0:
                # Ничья
                tournament_table[sorted_indices[i]][sorted_indices[j]] = 1
                tournament_table[sorted_indices[j]][sorted_indices[i]] = 1
                sorted_points[i] -= 1
                points[sorted_indices[j]] -= 1
            elif sorted_points[i] == 0:
                # Поражение
                tournament_table[sorted_indices[j]][sorted_indices[i]] = 2
                points[sorted_indices[j]] -= 2
        points[sorted_indices[i]] = -i - 1

    return tournament_table


def main() -> None:
    num_teams: int = int(input())
    points: List[int] = list(map(int, input().split()))

    tournament_table: Iterable[Iterable[int]] = restore_tournament_table(num_teams, points)

    for row in tournament_table:
        print(*row)


if __name__ == "__main__":
    main()