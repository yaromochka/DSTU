package programmingLanguages.laboratories.firstDotFirstLaboratory;


import java.awt.*;
import java.util.*;
import java.util.regex.Pattern;

import static programmingLanguages.laboratories.firstDotFirstLaboratory.Points.findMinDistancePoint;
import static programmingLanguages.laboratories.firstDotFirstLaboratory.TenthMethod.countConsonants;
import static programmingLanguages.laboratories.firstDotFirstLaboratory.TenthMethod.countVowels;
import static programmingLanguages.laboratories.firstDotFirstLaboratory.Triangle.maxPerimeter;

public class HelpClass {

    static final Scanner in = new Scanner(System.in).useLocale(Locale.US);
    public static void pointOfStart(int numberOfTask) {
        switch (numberOfTask) {
            case (1) -> firstQuestion();
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
            default -> System.out.println("Неверно введён номер задания");
        }
    }

    /** 1.	Ввести n строк с консоли, найти самую короткую строку.
     * Вывести эту строку и ее длину.*/
    public static void firstQuestion() {
        System.out.print("Введите строку, в которой хотите найти самую короткую: ");
        var line = in.nextLine().split(" ");
        var minLength = 1000000;
        var minLine = "";
        for (var x: line) {
            if (x.length() < minLength) {
                minLength = x.length();
                minLine = x;
            }
        }
        System.out.printf("Самая короткая строка - %s и её длина - %s", minLine, minLength);
    }

    /** 2.	Ввести n строк с консоли. Упорядочить
     *  и вывести строки в порядке возрастания их длин,
     *  а также (второй приоритет) значений этих их длин.*/
    public static void secondQuestion() {
        System.out.print("Введите строку, которую хотите упорядочить: ");
        var line = Arrays.stream(in.nextLine().split(" "))
                .sorted(Comparator.comparing(String::length).thenComparing(Comparator.naturalOrder()))
                .toArray();
        System.out.println(Arrays.toString(line));
    }

    /** 3.	Ввести n строк с консоли. Вывести на консоль те строки,
     * длина которых меньше средней, также их длины.*/
    public static void thirdQuestion() {
        System.out.print("Введите строку: ");
        var line = in.nextLine().split(" ");

        var averageLength = Arrays.stream(line)
                .mapToInt(String::length)
                .average()
                .orElseThrow();

        var result = Arrays.stream(line)
                .filter(word -> word.length() < averageLength)
                .toArray();
        System.out.println(Arrays.toString(result));
    }

    /** 4.	В каждом слове текста k-ю букву заменить заданным символом.
     * Если k больше длины слова, корректировку не выполнять.*/
    public static void fourthQuestion() {
        System.out.print("Введите текст, в котором хотите заменить символы: ");
        var line = in.nextLine().split(" ");
        System.out.print("Введите номер символа, который хотели бы заменять: ");
        var numberOfChar = in.nextInt() - 1;
        System.out.print("Введите символ, на который хотите заменять: ");
        var charToChange = in.next();
        System.out.println("Изменённый текст: ");
        for (var x: line) {
            if (numberOfChar >= x.length()) System.out.print(x + " ");
            else System.out.print(x.substring(0, numberOfChar) + charToChange
                    + x.substring(numberOfChar + 1) + " ");
        }
    }

    /** 5.	В русском тексте каждую букву заменить ее номером в алфавите. В одной
     *  строке печатать текст с двумя пробелами между буквами, в следующей строке
     *  внизу под каждой буквой печатать ее номер.*/
    public static void fifthQuestion() {
        System.out.print("Введите текст из символов русского алфавита: ");
        var line = in.nextLine().split(" ");
        ArrayList<Integer> numberInAlphabet = new ArrayList<>();
        for (var word: line) {
            for (var symbol: word.toLowerCase().toCharArray()) {
                System.out.print(symbol + "  ");
                numberInAlphabet.add(symbol + 'а' - 2143);
            }
        }
        System.out.println();
        for (var num: numberInAlphabet) {
            System.out.print(num + "  ");
        }
    }

    /** 6.	Из небольшого текста удалить все символы, кроме пробелов,
     * не являющиеся буквами. Между последовательностями подряд идущих букв
     * оставить хотя бы один пробел.*/
    public static void sixthQuestion() {
        System.out.print("Введите текст: ");
        var line = in.nextLine().replaceAll("[^A-Za-zа-яА-Я\\s]", "");
        System.out.printf("Текст после удаления ненужных символов: %s", line);
    }

    /** 7.	Из текста удалить все слова заданной длины, начинающиеся на согласную букву.*/
    public static void seventhQuestion() {
        var vowels = "aeiouAEIOUаяуюоеёэиыАЯУЮОЕЁЭИЫ";

        System.out.print("Введите текст: ");
        var line = in.nextLine().split(" ");
        System.out.print("Введите длину: ");
        var numLength = in.nextInt();
        for (var word: line) {
            if (word.length() == numLength && !vowels.contains(String.valueOf(word.charAt(0)))) continue;
            else System.out.print(word + " ");
        }
    }

    /** 8.	В тексте найти все пары слов, из которых одно является обращением другого.*/
    public static void eighthQuestion() {

        var result = new StringBuilder();
        System.out.print("Введите текст: ");
        var line = in.nextLine();

        for (var word : line.split(" ")) {
            var reversedWord = new StringBuilder(word).reverse().toString();
            // Создаем паттерн для поиска слов
            var pattern = Pattern.compile(reversedWord);
            var matcher = pattern.matcher(line);
            if (matcher.find())
                result.append(String.format("Результат для поиска слова %s: ", word)).append(matcher.group()).append("\n");
        }
        System.out.println(result);
    }

    /** 9.	Найти и напечатать, сколько раз повторяется в тексте каждое слово. */
    public static void ninthQuestion() {
        System.out.print("Введите текст: ");
        var line = in.nextLine().split(" ");
        var mapOfWords = new HashMap<>();

        for (var word : line) {
            if (mapOfWords.containsKey(word)) mapOfWords.put(word, (int) mapOfWords.get(word) + 1);
            else mapOfWords.put(word, 1);
        }

        System.out.println("Словарь: " + mapOfWords);
    }

    /** 10.	Найти, каких букв, гласных или согласных, больше в каждом предложении текста. */
    public static void tenthQuestion() {
        var result = new StringBuilder();
        System.out.println("Введите текст: ");

        Arrays.stream(in.nextLine().split("[.?!]\\s+")).forEach(sentence -> {

            var vowelsCount = countVowels(sentence);
            var consonantsCount = countConsonants(sentence);

            result.append(String.format("В предложении '%s' %s букв: гласных - %d, согласных - %d%n",
                    sentence, (vowelsCount > consonantsCount) ? "гласных больше" : "согласных больше",
                    vowelsCount, consonantsCount));

        });
        System.out.print(result);
    }

    /** 11.	Выбрать три разные точки заданного на плоскости множества точек,
     * составляющие треугольник наибольшего периметра. */
    public static void eleventhQuestion() {
        Triangle.Point[] points = {
                new Triangle.Point(0, 0),
                new Triangle.Point(1, 2),
                new Triangle.Point(2, 3),
                new Triangle.Point(4, 1),
                new Triangle.Point(5, 6)
        };
        System.out.println("Максимальный периметр треугольника: " + maxPerimeter(points));
    }

    /** 12.	Найти такую точку заданного на плоскости множества точек,
     * сумма расстояний от которой до остальных минимальна.*/
    public static void twelfthQuestion() {
        Point[] points = {
                new Point(0, 0),
                new Point(1, 2),
                new Point(2, 3),
                new Point(4, 1),
                new Point(16, 17)
        };

        Point minSumPoint = findMinDistancePoint(points);
        System.out.println("Точка с минимальной суммой расстояний: (" + minSumPoint.x + ", " + minSumPoint.y + ")");
    }

    /** 13.	Выпуклый многоугольник задан на плоскости перечислением
     * координат вершин в порядке обхода его границы. Определить площадь многоугольника. */
    public static void thirteenthQuestion() {
        Point[] points = {
                new Point(4, 10),
                new Point(9, 7),
                new Point(11, 2),
                new Point(2, 2),
        };

        // https://www.mathopenref.com/coordpolygonarea.html
        int countPoints = Arrays.asList(points).size();
        double sum = 0;
        for (int i = 0; i < countPoints; i += 1)

            sum += points[i].x * points[(i + 1) % countPoints].y -
                    points[(i + 1) % countPoints].x * points[i].y;

        System.out.printf("Площадь многоугольника: %s", Math.abs(sum / 2.0));
    }
}



