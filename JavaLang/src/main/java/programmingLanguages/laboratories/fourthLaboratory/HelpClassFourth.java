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
            case (4) -> fourthQuestion();
            case (5) -> fifthQuestion();
            case (6) -> sixthQuestion();
            case (7) -> seventhQuestion();
            case (8) -> eighthQuestion();
            case (9) -> ninthQuestion();
            case (10) -> tenthQuestion();
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
            default -> {
                return "Неверно введён номер задания";
            }
        }
        return null;
    }

    /* 1. Инициализация списка */
    private static String firstQuestion() {
        var LinkedList = new SingleLinkedList<>();
        return "Односвязный список успешно инициализирован";
    }

    private static String secondQuestion() {
        var LinkedList = new SingleLinkedList<Integer>();
        LinkedList.addFirst(10);
        LinkedList.addFirst(20);
        LinkedList.addFirst(22);
        LinkedList.addFirst(10);
        LinkedList.addFirst(15);
        LinkedList.addFirst(13);
        LinkedList.addFirst(10);
        LinkedList.pointerSort();

        return LinkedList.toString();
    }

    private static String thirdQuestion() {
        var LinkedList = new DoubleLinkedList<Integer>();
        LinkedList.addFirst(10);
        LinkedList.addFirst(20);
        LinkedList.addFirst(22);
        LinkedList.addFirst(10);
        LinkedList.addFirst(15);
        LinkedList.addFirst(13);
        LinkedList.addFirst(10);
        LinkedList.dataSort();

        return LinkedList.toString();
    }

    private static void fourthQuestion() {

    }

    private static void fifthQuestion() {

    }

    private static void sixthQuestion() {

    }

    private static void seventhQuestion() {

    }

    private static void eighthQuestion() {

    }

    private static void ninthQuestion() {

    }

    private static void tenthQuestion() {

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
}
