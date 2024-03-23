package programmingLanguages.laboratories.fourthLaboratory;

import programmingLanguages.laboratories.fourthLaboratory.Classes.Book;

import java.util.*;
import java.util.stream.Collectors;

public class HelpClassFourth {
    public static String pointOfStart(int numberOfTask, String arg) {
        switch (numberOfTask) {
            case (1) -> {
                return firstQuestion();
            }
            case (2) -> {
                return secondQuestion();
            }
            case (3) -> {
                return thirdQuestion();
            }
            case (4) -> {
                return fourthQuestion();
            }
            case (5) -> {
                return fifthQuestion();
            }
            case (6) -> {
                return sixthQuestion();
            }
            case (7) -> {
                return seventhQuestion();
            }
            case (8) -> {
                return eighthQuestion();
            }
            case (9) -> {
                return ninthQuestion();
            }
            case (10) -> {
                return tenthQuestion(arg);
            }
            case (11) -> {
                return eleventhQuestion();
            }
            case (12) -> {
                return twelfthQuestion(arg);
            }
            case (13) -> {
                return thirteenthQuestion(arg);
            }
            case (14) -> {
                return fourteenthQuestion(arg);
            }
            case (15) -> {
                return fifteenthQuestion();
            }
            case (16) -> {
                return sixteenthQuestion();
            }
            case (17) -> {
                return seventeenthQuestion();
            }
            case (18) -> {
                return eighteenthQuestion();
            }
            case (19) -> {
                return nineteenthQuestion();
            }
            case (20) -> {
                return twentiethQuestion();
            }
            case (21) -> {
                return twentyFirstQuestion();
            }
            case (22) -> {
                return twentySecondQuestion();
            }
            case (23) -> {
                return twentyThirdQuestion();
            }
            case (24) -> {
                return twentyFourthQuestion();
            }
            case (25) -> {
                return twentyFifthQuestion();
            }
            case (26) -> {
                return twentySixthQuestion();
            }
            case (27) -> {
                return twentySeventhQuestion();
            }
            case (28) -> {
                return twentyEighthQuestion();
            }
            case (29) -> {
                return twentyNinthQuestion();
            }
            case (30) -> {
                return thirtyQuestion(arg);
            }
            case (31) -> {
                return thirtyFirstQuestion();
            }
            case (32) -> {
                return thirtySecondQuestion(arg);
            }
            case (33) -> {
                return thirtyThirdQuestion(arg);
            }
            case (34) -> {
                return thirtyFourthQuestion(arg);
            }
            case (35) -> {
                return thirtyFifthQuestion();
            }
            case (36) -> {
                return thirtySixthQuestion();
            }
            case (37) -> {
                return thirtySeventhQuestion();
            }
            case (38) -> {
                return thirtyEighthQuestion();
            }
            case (39) -> {
                return thirtyNinthQuestion();
            }
            case (40) -> {
                return fortiethQuestion();
            }
            case (41) -> {
                return fortyFirstQuestion(arg);
            }
            case (42) -> {
                return fortySecondQuestion();
            }
            case (43) -> {
                return fortyThirdQuestion();
            }
            case (44) -> {
                return fortyFourthQuestion();
            }
            case (45) -> {
                return fortyFifthQuestion();
            }
            case (46) -> {
                return fortySixthQuestion();
            }
            case (47) -> fortySeventhQuestion();
            case (48) -> fortyEighthQuestion();
            case (49) -> fortyNinthQuestion();
            default -> {
                return "Неверно введён номер задания";
            }
        }
        return null;
    }

    static SingleLinkedList<Integer> singleList = new SingleLinkedList<>();
    static DoubleLinkedList<Integer> doubleList = new DoubleLinkedList<>();

    /* 1. Инициализация списка */
    private static String firstQuestion() {
        var LinkedList = new SingleLinkedList<>();
        return "Односвязный список успешно инициализирован";
    }

    /* 2. Добавление элемента в начало списка */
    private static String secondQuestion() {
        singleList.addFirst(10);
        singleList.addFirst(20);
        singleList.addFirst(22);
        singleList.addFirst(10);
        singleList.addFirst(15);
        singleList.addFirst(13);
        singleList.addFirst(10);

        return String.format("Список - %s", singleList.toString());
    }

    /* 3. Добавление элемента в конец списка */
    private static String thirdQuestion() {
        singleList.addLast(10);
        singleList.addLast(20);
        singleList.addLast(22);
        singleList.addLast(10);
        singleList.addLast(15);
        singleList.addLast(13);
        singleList.addLast(10);

        return String.format("Список - %s", singleList.toString());
    }

    /* 4. Показ всех элементов списка */
    private static String fourthQuestion() {
        return String.format("Список - %s", singleList.toString());
    }

    /* 5. Удаление всех элементов списка */
    private static String fifthQuestion() {
        singleList.clear();
        return String.format("Элементы списка успешно удалены\nСписок - %s", singleList.toString());
    }

    /* 6. Определение количества элементов списка */
    private static String sixthQuestion() {
        return String.format("Количество элементов в списке - %s", singleList.size());
    }

    /* 7. Проверка списка на пустоту */
    private static String seventhQuestion() {
        return singleList.isEmpty() ? "Список является пустым" : "Список не является пустым";
    }

    /* 8. Удаление первого элемента */
    private static String eighthQuestion() {
        singleList.removeFirst();
        return String.format("Первый элемент успешно удалён\nСписок - %s", singleList.toString());
    }

    /* 9. Удаление последнего элемента */
    private static String ninthQuestion() {
        singleList.removeLast();
        return String.format("Последний элемент успешно удалён\nСписок - %s", singleList.toString());
    }

    /* 10. Поиск данного значения в списке */
    private static String tenthQuestion(String arg) {
        var index = singleList.indexOf(Integer.parseInt(arg));
        return index == -1 ? "Нет такого значения в списке" : String.format("Индекс элемента в списке - %s", index);
    }

    /* 11. Поиск наибольшего и наименьшего значений в списке */
    private static String eleventhQuestion() {
        return String.format("Минимальное значение - %s\nМаксимальное значение - %s", singleList.min(), singleList.max());
    }

    /* 12. Удаление элемента списка с данным значением */
    private static String twelfthQuestion(String arg) {
        singleList.removeAt(Integer.parseInt(arg));
        return String.format("Элемент успешно удалён\nСписок - %s", singleList.toString());
    }

    /* 13. Удаление всех элементов списка с данным значением */
    private static String thirteenthQuestion(String arg) {
        singleList.remove(Integer.parseInt(arg));
        return String.format("Элементы успешно удалены\nСписок - %s", singleList.toString());
    }

    /* 14. Изменение всех элементов списка с данным значением на новое.*/
    private static String fourteenthQuestion(String arg) {
        int firstNumber, secondNumber;
        try {
            firstNumber = Integer.parseInt(arg.split("\\s")[0]);
            secondNumber = Integer.parseInt(arg.split("\\s")[1]);
        } catch(Exception e) {
            return "Неверно введены числа";
        }
        singleList.replaceAll(firstNumber, secondNumber);
        return String.format("Новый список - %s", singleList.toString());
    }

    /* 15. Определение, является ли список симметричным. */
    private static String fifteenthQuestion() {
        return singleList.isSymmetric() ? "Список симметричен" : "Список несимметричен";
    }

    /* 16. Определение, можно ли удалить из списка каких-нибудь
    два элемента так, чтобы новый список оказался упорядоченным. */
    private static String sixteenthQuestion() {
        return singleList.deleteTwoElementToOrdinary() ? "Список будет упорядоченным, если удалить два элементе"
                : "Список не будет упорядоченным";
    }

    /* 17. Определение, сколько различных значений содержится в списке. */
    private static String seventeenthQuestion() {
        return String.format("Список содержит %d различных элементов", singleList.distinctCount());
    }

    /* 18. Удаление из списка элементов, значения которых
     уже встречались в предыдущих элементах. */
    private static String eighteenthQuestion() {
        singleList.removeDistinct();
        return String.format("Новый список - %s", singleList.toString());
    }

    /* 19.	Изменение порядка элементов на обратный. */
    private static String nineteenthQuestion() {
        singleList.reversed();
        return String.format("Порядок элементов изменён\nСписок - %s", singleList.toString());
    }

    /* 20. Сортировка элементов списка двумя способами (изменение указателей, изменение значений элементов) */
    private static String twentiethQuestion() {
        singleList.pointerSort();
        return String.format("Отсортированный массив - %s", singleList.toString());
    }

    /* 21. Инициализация списка */
    private static String twentyFirstQuestion() {
        var LinkedList = new DoubleLinkedList<>();
        return "Двусвязный список успешно инициализирован";
    }

    /* 22. Добавление элемента в начало списка */
    private static String twentySecondQuestion() {
        doubleList.addFirst(10);
        doubleList.addFirst(20);
        doubleList.addFirst(22);
        doubleList.addFirst(10);
        doubleList.addFirst(15);
        doubleList.addFirst(13);
        doubleList.addFirst(10);

        return String.format("Список - %s", doubleList.toString());
    }

    /* 23. Добавление элемента в конец списка */
    private static String twentyThirdQuestion() {
        doubleList.addLast(10);
        doubleList.addLast(20);
        doubleList.addLast(22);
        doubleList.addLast(10);
        doubleList.addLast(15);
        doubleList.addLast(13);
        doubleList.addLast(10);

        return String.format("Список - %s", doubleList.toString());
    }

    /* 24. Показ всех элементов списка */
    private static String twentyFourthQuestion() {
        return String.format("Список - %s", doubleList.toString());
    }

    /* 25. Удаление всех элементов списка */
    private static String twentyFifthQuestion() {
        doubleList.clear();
        return String.format("Список успешно очищен\nСписок - %s", doubleList.toString());
    }

    /* 26. Определение количества элементов списка */
    private static String twentySixthQuestion() {
        return String.format("Количество элементов в списке - %s", doubleList.size());
    }

    /* 27. Проверка списка на пустоту */
    private static String twentySeventhQuestion() {
        return doubleList.isEmpty() ? "Список является пустым" : "Список не является пустым";
    }

    /* 28. Удаление первого элемента */
    private static String twentyEighthQuestion() {
        doubleList.removeFirst();
        return String.format("Первый элемент успешно удалён\nСписок - %s", doubleList.toString());
    }

    /* 29. Удаление последнего элемента */
    private static String twentyNinthQuestion() {
        doubleList.removeLast();
        return String.format("Последний элемент успешно удалён\nСписок - %s", doubleList.toString());
    }

    /* 30. Поиск данного значения в списке */
    private static String thirtyQuestion(String arg) {
        var index = doubleList.indexOf(Integer.parseInt(arg));
        return index == -1 ? "Нет такого значения в списке" : String.format("Индекс элемента в списке - %s", index);
    }

    /* 31. Поиск наибольшего и наименьшего значений в списке */
    private static String thirtyFirstQuestion() {
        return String.format("Минимальный элемент списка - %s\n" +
                "Максимальный элемент списка - %s", doubleList.min(), doubleList.max());
    }

    /* 32. Удаление элемента списка с данным значением */
    private static String thirtySecondQuestion(String arg) {
        doubleList.removeAt(Integer.parseInt(arg));
        return String.format("Элемент успешно удалён\nСписок - %s", doubleList.toString());
    }

    /* 33. Удаление всех элементов списка с данным значением */
    private static String thirtyThirdQuestion(String arg) {
        doubleList.remove(Integer.parseInt(arg));
        return String.format("Элементы успешно удалены\nСписок - %s", doubleList.toString());
    }

    /* 34. Изменение всех элементов списка с данным значением на новое. */
    private static String thirtyFourthQuestion(String arg) {
        int firstNumber, secondNumber;
        try {
            firstNumber = Integer.parseInt(arg.split("\\s")[0]);
            secondNumber = Integer.parseInt(arg.split("\\s")[1]);
        } catch(Exception e) {
            return "Неверно введены числа";
        }
        doubleList.replaceAll(firstNumber, secondNumber);
        return String.format("Новый список - %s", doubleList.toString());
    }

    /* 35. Определение, является ли список симметричным. */
    private static String thirtyFifthQuestion() {
        return singleList.isSymmetric() ? "Список симметричен" : "Список несимметричен";
    }

    /* 36. Определение, можно ли удалить из списка каких-нибудь два
    элемента так, чтобы новый список оказался упорядоченным. */
    private static String thirtySixthQuestion() {
        return doubleList.deleteTwoElementToOrdinary() ? "Список будет упорядоченным, если удалить два элементе"
                : "Список не будет упорядоченным";
    }

    /* 37. Определение, сколько различных значений содержится в списке. */
    private static String thirtySeventhQuestion() {
        return String.format("Список содержит %d различных элементов", doubleList.distinctCount());
    }

    /* 38. Удаление из списка элементов,
     значения которых уже встречались в предыдущих элементах. */
    private static String thirtyEighthQuestion() {
        doubleList.removeDistinct();
        return String.format("Список - %s", doubleList.toString());
    }

    /* 39. Изменение порядка элементов на обратный. */
    private static String thirtyNinthQuestion() {
        doubleList.reversed();
        return String.format("Список - %s", doubleList.toString());
    }

    /* 40.	Сортировка элементов списка двумя способами (изменение указателей, изменение значений элементов) */
    private static String fortiethQuestion() {
        doubleList.pointerSort();
        return String.format("Отсортированный список - %s", doubleList.toString());
    }

    /* 41. Дан упорядоченный список книг. Добавить новую книгу, сохранив упорядоченность списка. */
    private static String fortyFirstQuestion(String arg) {
        var tree = new TreeSet<>(Arrays.asList(
                new Book("Му-му", "Иван Тургенев", 1852),
                new Book("Гарри Поттер", "Джоан Роулинг", 1997)
        ));

        var it = Arrays.stream(arg.split(",\\s+")).iterator();
        try {
            tree.add(new Book(it.next(), it.next(), Integer.parseInt(it.next())));
            return "Наш список книг после добавления: " + tree;
        } catch (NoSuchElementException e) {
            return "Ввели неправильные аргументы";
        }
    }

    /* 42. Даны два упорядоченных по возрастанию списка.
    Объедините их в новый упорядоченный по возрастанию список. */
    private static String fortySecondQuestion() {

        // Генерация двух упорядоченных массивов, отсортированных по возрастанию
        var firstList = new SingleLinkedList<Integer>();
        var secondList = new SingleLinkedList<Integer>();

        new Random().ints(10, 5, 1000).forEach(firstList::addFirst);
        new Random().ints(10, 5, 1000).forEach(secondList::addFirst);

        firstList.pointerSort();
        secondList.pointerSort();

        for (int i = 0; i < secondList.size(); i++) {
            firstList.addFirst(secondList.find(i));
        }
        firstList.dataSort();

        return String.format("Элементы нового списка - %s", firstList);
    }

    /* 43. Дан список целых чисел. Упорядочьте по возрастанию только:
     а) положительные числа;
     б) элементы с четными порядковыми номерами в списке. */
    private static String fortyThirdQuestion() {
        return "0";
    }

    /* 44. Даны два списка. Определите, совпадают ли множества их элементов. */
    private static String fortyFourthQuestion() {

        var firstList = new HashSet<Integer>();
        var secondList = new HashSet<Integer>();

        new Random().ints(10, 5, 1000).forEach(firstList::add);
        new Random().ints(10, 5, 1000).forEach(secondList::add);

        return firstList.equals(secondList) ? "Множества элементов совпадают" : "Множества элементов не совпадают";
    }

    /* 45. Дан список. После каждого элемента добавьте предшествующую ему часть списка. */
    private static String fortyFifthQuestion() {
        var pastString = new StringBuilder();
        var list = new ArrayList<Integer>();

        new Random().ints(3, 5, 1000).forEach(list::add);

        return list.stream().map(x -> {
            var result = pastString + String.valueOf(x);
            pastString.append(x).append(" ");
            return result;
        }).collect(Collectors.joining(" "));
    }

    /* 46. Пусть элементы списка хранят символы предложения.
    Замените каждое вхождение слова "itmathrepetitor" на "silence". */
    private static String fortySixthQuestion() {
        ArrayList<Character> sentenceList = new ArrayList<>(Arrays.asList(
                'h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd', ' ',
                'i', 't', 'm', 'a', 't', 'h', 'r', 'e', 'p', 'e', 't', 'i', 't', 'o', 'r', ' '
        ));

        var sentence = String.join("", sentenceList.stream().map(Object::toString).toArray(String[]::new));

        return sentence.replaceAll("itmathrepetitor", "silence");
    }

    /* 47. Дан текстовый файл. Создайте двусвязный список,
    каждый элемент которого содержит количество символов
    в соответствующей строке текста. */
    private static void fortySeventhQuestion() {

    }
    private static void fortyEighthQuestion() {

    }
    private static void fortyNinthQuestion() {

    }
}
