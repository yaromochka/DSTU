from collections import deque
from typing import Sequence, List, Iterable


def process_queue(actions: Sequence[Sequence[str]]) -> Iterable[str]:
    """
    Почему тут используется несколько очередей?
    Нельзя все делать с одной очередью, потому что у нас есть момент, когда нужно вставлять в центр,
    а данная операция (O(n)), так как под капотом здесь связный список.
    Если будете хранить две очереди примерно равного размера, вставка в середину будет занимать константу.
    """

    q1 = deque()
    q2 = deque()
    results: List[str] = []

    for action in actions:
        if action[0] == '+':
            q2.append(action[1])
        elif action[0] == '*':
            q2.appendleft(action[1])
        else:
            results.append(q1.popleft())

        if len(q1) < len(q2):
            q1.append(q2.popleft())

    return results


def main() -> None:
    n: int = int(input())
    actions: List[List[str]] = []

    for _ in range(n):
        action: List[str] = input().split()
        actions.append(action)

    results: Iterable[str] = process_queue(actions)

    for result in results:
        print(result)


if __name__ == "__main__":
    main()