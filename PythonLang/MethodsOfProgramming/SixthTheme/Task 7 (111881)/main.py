from typing import List, Sequence, Iterable


def process_experiment(n: int, particles: str, actions: Sequence[Sequence[str]]) -> Iterable[str]:
    offsets: List[int] = list(range(n))
    results: List[str] = []

    for action in actions:
        if action[0] == 'a':
            # Воздействие: перенос частицы
            i, j = int(action[1]) - 1, int(action[2]) - 1
            element = offsets.pop(i)
            offsets.insert(j, element)
        elif action[0] == 'q':
            # Вопрос: какая частица на позиции k
            k = int(action[1]) - 1
            results.append(particles[offsets[k]])

    return results


def main() -> None:
    n, m = map(int, input().split())
    particles: str = input().strip()
    actions: List[List[str]] = [input().split() for _ in range(m)]

    # Обрабатываем эксперименты
    results = process_experiment(n, particles, actions)

    # Выводим результаты
    print("\n".join(results))


if __name__ == "__main__":
    main()