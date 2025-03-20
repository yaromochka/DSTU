def minimal_cyclic_shift(kirill: str, dima: str) -> int:

    # Если строки совпадают, сдвиг равен 0
    if kirill == dima:
        return 0

    # Удваиваем строку Димы для поиска циклического сдвига
    doubled_dima = dima * 2
    shift_index = doubled_dima.find(kirill)

    # Если Кириллову строку не удалось найти, значит, Дима ошибся
    return -1 if shift_index == -1 else shift_index


def main() -> None:
    kirill_string: str = input()
    dima_string: str = input()

    result = minimal_cyclic_shift(kirill_string, dima_string)
    print(result)


if __name__ == "__main__":
    main()