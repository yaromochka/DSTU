from typing import Dict, List, Iterable


def process_students(students: Iterable[str]) -> str:
    """
    Из условия задачи известно, что у нас всего 3 класса, поэтому заранее создал словарь с готовыми ключами.
    Здесь мы принимаем строку, и добавляем по нужному ключу в словарь.
    :param students: Итерируемый объект, который содержит данные о студентах в виде строк.
    :returns: Тот же самый вид строки, как было и в условии.
    """
    classes: Dict[int, List[str]] = {9: [], 10: [], 11: []}

    for student in students:
        class_number, surname = student.split()
        class_number = int(class_number)
        classes[class_number].append(f"{class_number} {surname}")

    result = ""
    for class_number in classes:
        result += "\n".join(student for student in classes[class_number]) + "\n"

    return result


def main() -> None:
    input_file_path = "input.txt"
    output_file_path = "output.txt"

    with open(input_file_path, 'r', encoding='KOI8-r') as file:
        students_by_class = process_students(map(str.strip, file.readlines()))

    with open(output_file_path, 'w', encoding='KOI8-r') as file:
        file.write(students_by_class)


if __name__ == "__main__":
    main()