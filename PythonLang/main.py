def calculator(expression):
    allowed = '+-/*'
    if not any(sign in expression for sign in allowed):
        raise ValueError(f'Выражение должно содержать хотя бы один знак ({allowed})')
    for sign in allowed:
        if sign in expression:
            try:
                left, right = expression.split(sign)
                left, right = int(left), int(right)
                if sign == '+':
                    return left + right
                elif sign == '-':
                    return left - right
                elif sign == '*':
                    return left * right
                elif sign == '/':
                    return left / right
            except (ValueError, TypeError):
                raise ValueError(f'Выражение должно содержать два целых числа и один знак')


if __name__ == '__main__':
    print(calculator('10 / 5'))