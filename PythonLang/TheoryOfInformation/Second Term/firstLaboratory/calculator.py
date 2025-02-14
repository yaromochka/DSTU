from collections import deque


def reverse_gcd(a: int, mod: int) -> (int, int, int):
    if a == 0:
        return mod, 0, 1
    gcd, x1, y1 = reverse_gcd(mod % a, a)
    x: int = y1 - (mod // a) * x1
    y: int = x1
    return gcd, x, y


def divide(a: int, b: int, mod: int) -> int:
    gcd, b, _ = reverse_gcd(b, mod)
    return multiply(a, b, mod)


def multiply(a: int, b: int, mod: int) -> int:
    return (a * b) % mod


def minus(a: int, b: int, mod: int) -> int:
    return (a + (b % mod)) % mod


def plus(a: int, b: int, mod: int) -> int:
    return (a + b) % mod


def calculate(expression: str, mod: int) -> int:
    def apply_operator(op: str, a: int, b: int) -> int:
        if op == "+":
            return plus(a, b, mod)
        elif op == "-":
            return minus(a, b, mod)
        elif op == "*":
            return multiply(a, b, mod)
        elif op == "/" or op == "\\":
            return divide(a, b, mod)
        elif op == "^":
            return pow(a, b, mod)

    def precedence(op: str):
        if op in ('+', '-'): return 1
        if op in ('*', '/'): return 2
        return 0

    values: deque[int] = deque()
    operators: deque[str] = deque()
    i: int = 0
    n: int = len(expression)
    while i < n:
        ch: str = expression[i]
        if ch == ' ':
            i += 1
            continue
        if ch.isdigit():
            num: int = 0
            while i < n and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            values.append(num)
        elif ch == '(':
            operators.append(ch)
            i += 1
        elif ch == ')':
            while operators and operators[-1] != '(':
                if len(values) < 2: return -1
                op: str = operators.pop()
                b: int = values.pop()
                a: int = values.pop()
                values.append(apply_operator(op, b, a))
            if operators and operators[-1] == '(':
                operators.pop()
            else:
                return -1
            i += 1
        elif ch in '+-*/^\\':
            while (operators and operators[-1] != '(' and
                   precedence(operators[-1]) >= precedence(ch)):
                if len(values) < 2:
                    return -1
                op = operators.pop()
                b = values.pop()
                a = values.pop()
                values.append(apply_operator(op, b, a))
            operators.append(ch)
            i += 1
        else:
            return -1
    while operators:
        if len(values) < 2: return -1
        op: str = operators.pop()
        b: int = values.pop()
        a: int = values.pop()
        values.append(apply_operator(op, b, a))
    if len(values) == 1:
        return values[0]
    else:
        return -1