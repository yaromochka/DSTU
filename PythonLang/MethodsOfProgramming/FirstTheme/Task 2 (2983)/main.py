from collections import deque
from typing import Deque, List


def error_check(actions: List[Deque[int]], action: str, number_tank: int, number_fill: int, count_in_boat: int, P: int) -> bool:
    if number_tank < 1 or count_in_boat > P or number_tank > len(actions): return False
    if action == '-':
        if not actions[number_tank - 1] or actions[number_tank - 1][-1] != number_fill: return False
    return True


def process_docs() -> str:
    # N - количество пройденных доков и действий на них
    # K - количество грузовых отсеков
    # P - максимальное количество бочек на барже
    N, K, P = map(int, input().split())
    count_in_boat: int = 0
    max_in_boat: int = 0
    actions: List[Deque[int]] = [deque() for _ in range(K)]
    for _ in range(N):
        action, number_tank, number_fill = input().split()
        number_tank, number_fill = int(number_tank), int(number_fill)
        if error_check(actions, action, number_tank, number_fill, count_in_boat, P):
            if action == '+':
                actions[number_tank - 1].append(number_fill)
                count_in_boat += 1
            elif action == '-':
                actions[number_tank - 1].pop()
                count_in_boat -= 1
            max_in_boat = max(count_in_boat, max_in_boat)
        else: return 'Error'
    return max_in_boat if count_in_boat == 0 else 'Error'


def main() -> None:
    print(process_docs())


if __name__ == '__main__':
    main()