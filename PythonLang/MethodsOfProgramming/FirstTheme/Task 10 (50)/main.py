from collections import deque
from typing import Tuple, Iterable, Dict


def is_first_player_winner(card1: int, card2: int) -> bool:
    return (card1 > card2 and (card2, card1) != (0, 9)) or (card1 == 0 and card2 == 9)


def play_game(
        first_deque: Iterable[int],
        second_deque: Iterable[int]
) -> Tuple[int, int]:
    first_deque: deque[int] = deque(first_deque)
    second_deque: deque[int] = deque(second_deque)
    rounds: int = 0
    max_rounds: int = 10 ** 6
    while first_deque and second_deque:
        rounds += 1
        first_card = first_deque.popleft()
        second_card = second_deque.popleft()
        if is_first_player_winner(first_card, second_card):
            first_deque.extend([first_card, second_card])
        else:
            second_deque.extend([first_card, second_card])
        if rounds >= max_rounds:
            return -1, -1
    return not first_deque, rounds


def main() -> None:
    cases: Dict[int, str] = {-1: "botva", 0: "first", 1: "second"}
    result: Tuple[int, int] = play_game(
        map(int, input().split()),
        map(int, input().split())
    )
    print(cases[result[0]], result[1] if result[1] != -1 else "")


if __name__ == '__main__':
    main()