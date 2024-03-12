package programmingLanguages.laboratories.thirdDotFirstLaboratory;

public class HelpClassThirdDotFirst {
    public static String pointOfStart(int numberOfTask, String arg) {
        switch (numberOfTask) {
            case (1) -> {
                return firstQuestion((String) arg);
            }
            case (2) -> secondQuestion();
            case (3) -> thirdQuestion();
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
            default -> {
                return "Неверно введён номер задания";
            }
        }
        return null;
    }

    private static String firstQuestion(String line) {
        return "Hello World!";
    }

    private static void secondQuestion() {

    }

    private static void thirdQuestion() {

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

}
