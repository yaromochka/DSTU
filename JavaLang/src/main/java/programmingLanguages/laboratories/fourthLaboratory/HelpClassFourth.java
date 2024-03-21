package programmingLanguages.laboratories.fourthLaboratory;

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
            case (11) -> eleventhQuestion();
            case (12) -> twelfthQuestion();
            case (13) -> thirteenthQuestion();
            case (14) -> fourteenthQuestion();
            case (15) -> fifteenthQuestion();
            case (16) -> sixteenthQuestion();
            case (17) -> seventeenthQuestion();
            case (18) -> eighteenthQuestion();
            case (19) -> nineteenthQuestion();
            case (20) -> twentiethQuestion();
            case (21) -> twentyFirstQuestion();
            case (22) -> twentySecondQuestion();
            case (23) -> twentyThirdQuestion();
            case (24) -> twentyFourthQuestion();
            case (25) -> twentyFifthQuestion();
            case (26) -> twentySixthQuestion();
            case (27) -> twentySeventhQuestion();
            case (28) -> twentyEighthQuestion();
            case (29) -> twentyNinthQuestion();
            case (30) -> thirtyQuestion();
            case (31) -> thirtyFirstQuestion();
            case (32) -> thirtySecondQuestion();
            case (33) -> thirtyThirdQuestion();
            case (34) -> thirtyFourthQuestion();
            case (35) -> thirtyFifthQuestion();
            case (36) -> thirtySixthQuestion();
            case (37) -> thirtySeventhQuestion();
            case (38) -> thirtyEighthQuestion();
            case (39) -> thirtyNinthQuestion();
            case (40) -> fortiethQuestion();
            case (41) -> fortyFirstQuestion();
            case (42) -> fortySecondQuestion();
            case (43) -> fortyThirdQuestion();
            case (44) -> fortyFourthQuestion();
            case (45) -> fortyFifthQuestion();
            case (46) -> fortySixthQuestion();
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
        return "Элементы списка успешно удалены";
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

    private static void eleventhQuestion() {

    }

    private static void twelfthQuestion() {

    }

    private static void thirteenthQuestion() {

    }

    private static void fourteenthQuestion() {

    }

    private static void fifteenthQuestion() {

    }

    private static void sixteenthQuestion() {

    }

    private static void seventeenthQuestion() {

    }

    private static void eighteenthQuestion() {

    }

    private static void nineteenthQuestion() {

    }

    private static void twentiethQuestion() {

    }

    private static void twentyFirstQuestion() {

    }

    private static void twentySecondQuestion() {

    }

    private static void twentyThirdQuestion() {

    }

    private static void twentyFourthQuestion() {

    }

    private static void twentyFifthQuestion() {

    }

    private static void twentySixthQuestion() {

    }

    private static void twentySeventhQuestion() {

    }

    private static void twentyEighthQuestion() {

    }

    private static void twentyNinthQuestion() {

    }

    private static void thirtyQuestion() {

    }

    private static void thirtyFirstQuestion() {

    }
    private static void thirtySecondQuestion() {

    }
    private static void thirtyThirdQuestion() {

    }
    private static void thirtyFourthQuestion() {

    }
    private static void thirtyFifthQuestion() {

    }
    private static void thirtySixthQuestion() {

    }
    private static void thirtySeventhQuestion() {

    }
    private static void thirtyEighthQuestion() {

    }
    private static void thirtyNinthQuestion() {

    }
    private static void fortiethQuestion() {

    }
    private static void fortyFirstQuestion() {

    }
    private static void fortySecondQuestion() {

    }
    private static void fortyThirdQuestion() {

    }
    private static void fortyFourthQuestion() {

    }
    private static void fortyFifthQuestion() {

    }
    private static void fortySixthQuestion() {

    }
    private static void fortySeventhQuestion() {

    }
    private static void fortyEighthQuestion() {

    }
    private static void fortyNinthQuestion() {

    }
}
