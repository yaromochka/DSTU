from collections import deque


def train_queue(N: int) -> bool:
    queue: deque = deque()
    wagons = map(int, input().split())
    current_number: int = 1 # number to count next wagon
    for wagon in wagons:
        if wagon != current_number: queue.append(wagon)
        else: current_number += 1
        while queue and queue[-1] == current_number:
            queue.pop()
            current_number += 1
    return not queue


def main() -> None:
    N = int(input())
    print('YES' if train_queue(N) else 'NO')


if __name__ == "__main__":
    main()