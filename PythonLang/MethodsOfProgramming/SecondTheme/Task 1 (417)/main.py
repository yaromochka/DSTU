from itertools import permutations


def generate_permutations(license_plate: str):
    unique_permutations = set(filter(lambda x: all([x[0].isalpha(), x[4].isalpha(), x[5].isalpha()]) and all([x[1].isdigit(), x[2].isdigit(), x[3].isdigit()]), set(''.join(p) for p in permutations(license_plate))))
    return unique_permutations


def main():
    license_plate = input().strip()
    unique_permutations = generate_permutations(license_plate)

    # Вывод результата
    print(len(unique_permutations))
    for perm in unique_permutations:
        print(perm)


if __name__ == "__main__":
    main()