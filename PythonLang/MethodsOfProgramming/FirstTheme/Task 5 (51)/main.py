from collections import deque


def check_CBS(s: str) -> bool:
    stack: deque = deque()
    brackets: dict = {
        ')': '(',
        ']': '[',
        '}': '{',
    }
    for c in s:
        if c in '([{': stack.append(c)
        if c in ')]}':
            if stack and stack[-1] == brackets[c]: stack.pop()
            else: return False
    return not stack


def main() -> None:
    s: str = input()
    print('yes' if check_CBS(s) else 'no')


if __name__ == "__main__":
    main()