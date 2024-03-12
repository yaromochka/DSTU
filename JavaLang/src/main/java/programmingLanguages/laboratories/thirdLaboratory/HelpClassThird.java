package programmingLanguages.laboratories.thirdLaboratory;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.NoSuchElementException;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Collectors;

// 29 заданий
public class HelpClassThird {
    public static String pointOfStart(int numberOfTask, String arg) {
        switch (numberOfTask) {
            case (1) -> {
                return firstQuestion(arg);
            }
            case (2) -> {
                return secondQuestion(arg);
            }
            case (3) -> {
                return thirdQuestion(arg);
            }
            case (4) -> {
                return fourthQuestion(arg);
            }
            case (5) -> {
                return fifthQuestion(arg);
            }
            case (6) -> {
                return sixthQuestion(arg);
            }
            case (7) -> {
                return seventhQuestion(arg);
            }
            case (8) -> {
                return eighthQuestion(arg);
            }
            case (9) -> {
                return ninthQuestion(arg);
            }
            case (10) -> {
                return tenthQuestion(arg);
            }
            case (11) -> {
                return eleventhQuestion(arg);
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
                return fifteenthQuestion(arg);
            }
            case (16) -> {
                return sixteenthQuestion(arg);
            }
            case (17) -> {
                return seventeenthQuestion(arg);
            }
            case (18) -> {
                return eighteenthQuestion(arg);
            }
            default -> {
                return "Неверно введён номер задания";
            }
        }
    }

    /* 1.	Ввести n строк с консоли, найти самую короткую и самую длинную строки.
    Вывести найденные строки и их длину. */
    private static String firstQuestion(String line) {
        var in = line.split("\\s+");
        int maxLen = Integer.MAX_VALUE, minLen = Integer.MIN_VALUE;
        String minLine = "", maxLine = "";
        for (var word : in) {
            if (word.length() >= maxLen) {
                maxLine = word;
                maxLen = word.length();
            } else if (word.length() <= minLen) {
                minLine = word;
                minLen = word.length();
            }
        }
        return String.format("Максимальная строка - %s с длиной: %d\nМинимальная строка - %s с длиной: %d",
                maxLine, maxLen, minLine, minLen);
    }

    /* 2. Ввести n строк с консоли. Упорядочить и вывести строки в
    порядке возрастания (убывания) значений их длины. */
    private static String secondQuestion(String line) {
        var answer = line.split("\\s+");
        Arrays.sort(answer);
        return String.format("Сортировка по увеличению длины:\n%s:", Arrays.toString(answer));
    }

    /* 3. Ввести n строк с консоли. Вывести на консоль те строки,
    длина которых меньше (больше) средней, а также длину. */
    private static String thirdQuestion(String line) {
        ArrayList<String> answer = new ArrayList<>();
        int lineMeanLength = (int) Arrays.stream(line.split("\\s+")).mapToInt(String::length).average().orElseThrow();
        for (var word : line.split("\\s+")) {
            if (word.length() < lineMeanLength) {
                answer.add(word);
            }
        }
        return String.format("Строки, длина которых меньше средней: %s", String.join(", ", answer));
    }

    /* 4. Ввести n слов с консоли. Найти слово,
     в котором число различных символов минимально.
     Если таких слов несколько, найти первое из них. */
    private static String fourthQuestion(String line) {
        var ListWithRows = line.split("\\s+");

        int minLenSymbols = Integer.MAX_VALUE;
        String answer = "";

        for (var word : ListWithRows) {
            var countDifferentSymbol = word.chars().mapToObj(i -> (char) i).distinct().count();

            if (countDifferentSymbol < minLenSymbols) {
                minLenSymbols = (int) countDifferentSymbol;
                answer = word;
            }
        }
        return String.format
                (
                        "Слово - %s, с количеством разных символов - %d",
                        answer,
                        minLenSymbols
                );
    }

    /* 5. Ввести n слов с консоли. Найти количество слов,
     содержащих только символы латинского алфавита,
     а среди них – количество слов с равным числом
     гласных и согласных букв. */
    private static String fifthQuestion(String line) {
        var result = Arrays.stream(line.split("\\s+"))
                .filter(word -> word.matches("^[a-zA-Z0-9]+$"))
                .filter(word -> {
                    var countConsonants = word.replaceAll("(?i)[^aeiouy]", "").length();
                    var countVowels = word.length() - countConsonants;
                    return countVowels == countConsonants;
                })
                .count();
        return String.format("Количество слов, содержащие только латинские буквы, " +
                "где количество гласных и согласных одинаково : %d", result);
    }

    /* 6. Ввести n слов с консоли. Найти слово, символы в котором
    идут в строгом порядке возрастания их кодов.
    Если таких слов несколько, найти первое из них. */
    private static String sixthQuestion(String line) {
        var tempLine = line.split("\\s+");
        String answer = "Нет такой строки";
        for (var word : tempLine) {
            for (int i = 0; i < word.length() - 1; i++) {
                if (!(word.charAt(i) < word.charAt(i + 1))) {
                    break;
                }
                answer = word;
            }
        }
        return String.format("Искомая строка - %s", answer);
    }

    /* 7. Ввести n слов с консоли. Найти слово, состоящее только
     из различных символов. Если таких слов несколько, найти первое из них. */
    private static String seventhQuestion(String line) {
        var tempLine = line.split("\\s+");
        String answer = "Нет такой строки";
        for (var word : tempLine) {
            var countDifferentSymbol = word.chars().mapToObj(i -> (char) i).distinct().count();
            if (countDifferentSymbol == word.length()) answer = word;
        }
        return String.format("Искомая строка - %s", answer);
    }

    /* 8. Ввести n слов с консоли. Среди слов, состоящих только из цифр,
     найти слово-палиндром. Если таких слов больше одного, найти второе из них. */
    private static String eighthQuestion(String line) {
        var answer = Arrays.stream(line.split("\\s+"))
                .filter(word -> word.matches("[0-9]+"))
                .filter(word -> {
                    var reversedLine = new StringBuilder(word).reverse().toString();
                    return word.equals(reversedLine);
                })
                .skip(1)
                .findFirst()
                .orElse("Не найдено палиндромов состоящих из цифр");

        if (answer.equals("Не найдено палиндромов, состоящих только из цифр"))
            return answer;

        return String.format("Второе слово палиндром, состоящее только из цифр: %s", answer);
    }

    /* 9. Написать программы решения задач 1–8,
    осуществляя ввод строк как аргументов командной строки. */
    private static String ninthQuestion(String line) {
        return "Все команды осуществлены с вводом командной строки";
    }

    /* 10. a) Напишите метод, который принимает в качестве параметра любую строку, например “I like Java!!!”.
    б) Распечатать последний символ строки. Используем метод String.charAt().
    в) Проверить, заканчивается ли ваша строка подстрокой “!!!”. Используем метод String.endsWith().
    г) Проверить, начинается ли ваша строка подстрокой “I like”. Используем метод String.startsWith().
    д) Проверить, содержит ли ваша строка подстроку “Java”. Используем метод String.contains().
    e) Найти позицию подстроки “Java” в строке “I like Java!!!”.
    ж) Заменить все символы “а” на “о”.
    з) Преобразуйте строку к верхнему регистру.
    и) Преобразуйте строку к нижнему регистру.
    к) Вырезать строку Java c помощью метода String.substring(). */
    private static String tenthQuestion(String line) {
        return String.format(
                "Последний символ строки - %s\n" +
                "Строка заканчивается '!!!' - %s\n" +
                "Строка начинается 'I like' - %s\n" +
                "Строка содержит 'Java' - %s\n" +
                "Позиция Java - %s\n" +
                "Строка с заменой - %s\n" +
                "Строка с только верхним регистром - %s\n" +
                "Строка с только нижним регистром - %s\n" +
                "Строка без 'Java' - %s\n",
                line.charAt(line.length() - 1),
                line.endsWith("!!!"),
                line.startsWith("I like"),
                line.contains("Java"),
                line.indexOf("Java"),
                line.replaceAll("a", "o"),
                line.toUpperCase(),
                line.toLowerCase(),
                line.substring(0, line.indexOf("Java") - 1) + line.substring(line.indexOf("Java") + 4));
    }

    /* 11.	а) Дано два числа, например 3 и 56, необходимо составить следующие строки:
    3 + 56 = 59
    3 – 56 = -53
    3 * 56 = 168.
    Используем метод StringBuilder.append().
    б) Замените символ “=” на слово “равно”. Используйте методы StringBuilder.insert(), StringBuilder.deleteCharAt().
    в) Замените символ “=” на слово “равно”. Используйте методы StringBuilder.replace(). */
    private static String eleventhQuestion(String line) {
        var answer = new StringBuilder();
        var secondAnswer = new StringBuilder();
        var thirdAnswer = new StringBuilder();
        var stringNumbers = line.split("\\s+");
        int firstNumber, secondNumber;
        try {
            firstNumber = Integer.parseInt(stringNumbers[0]);
            secondNumber = Integer.parseInt(stringNumbers[1]);
        } catch(Exception e) {
            return "Неверно введены числа";
        }

        answer.append(firstNumber + " + " + secondNumber + " = " + (firstNumber + secondNumber) + "\n");
        answer.append(firstNumber + " - " + secondNumber + " = " + (firstNumber - secondNumber) + "\n");
        answer.append(firstNumber + " * " + secondNumber + " = " + (firstNumber * secondNumber) + "\n");

        secondAnswer.append(firstNumber + " - " + secondNumber + " = " + (firstNumber - secondNumber) + "\n");

        var equalsPosition = secondAnswer.indexOf("=");

        while (equalsPosition != -1) {
            // Удаление символа '='
            secondAnswer.deleteCharAt(equalsPosition);

            // Вставка слова "равно" вместо удаленного символа
            secondAnswer.insert(equalsPosition, "равно");

            equalsPosition = secondAnswer.indexOf("=");
        }

        thirdAnswer.append(firstNumber + " * " + secondNumber + " = " + (firstNumber * secondNumber) + "\n");

        return answer + " " + secondAnswer + " " +
                (thirdAnswer.toString()).replaceAll("=", "равно");
    }

    /* 12.	Напишите метод, заменяющий в строке каждое второе вхождение «object-oriented programming»
    (не учитываем регистр символов) на «OOP». Например, строка "Object-oriented programming is a programming
    language model organized around objects rather than "actions" and data rather than logic.
    Object-oriented programming blabla. Object-oriented programming bla." должна быть преобразована в
    "Object-oriented programming is a programming language model organized around objects rather than
     "actions" and data rather than logic. OOP blabla. Object-oriented programming bla." */
    private static String twelfthQuestion(String line) {

        // Object-oriented programming is a programming language model organized around objects rather than "actions" and data rather than logic. Object-oriented programming blabla. Object-oriented programming bla.

        var regex = "(?i)object-oriented programming";
        Pattern compiledPattern = Pattern.compile(regex);
        Matcher matcher = compiledPattern.matcher(line);

        int count = 0;
        StringBuilder sb = new StringBuilder();

        while (matcher.find()) {
            if ((count % 2) == 1) {
                matcher.appendReplacement(sb, "OOP"); // Добавление с реплейсом
            }
            count++;
        }
        matcher.appendTail(sb);
        return sb.toString();
    }

    /* 13. Даны строки разной длины (длина - четное число),
    необходимо вернуть ее два средних знака: "string" → "ri", "code" → "od", "Practice"→"ct". */
    private static String thirteenthQuestion(String line) {
        var sb = new StringBuilder();
        for (var word : line.split("\\s+")) {
            var middleLen = word.length() / 2;
            if (word.length() % 2 == 0) sb.append(word.substring(middleLen - 1, middleLen + 1) + "\n");
            else sb.append("Эта строка имею нечётную длину");
        }
        return sb.toString();
    }

    /* 14.	Создать строку, используя форматирование: Студент [Фамилия]
    получил [оценка] по [предмету]. Форматирование и вывод строки на консоль
    написать в отдельном методе, который принимает фамилию, оценку и название
    предмета в качестве параметров. Выделить под фамилию 15 символов, под оценку 3 символа, предмет – 10. */
    private static String fourteenthQuestion(String line) {
        var iter = Arrays.stream(line.split("\\s+")).iterator();
        try {
            return new Student(iter.next(), iter.next(), iter.next()).toString();
        } catch (NoSuchElementException e) {
            return "Вы ввели неверные параметры";
        }
    }

    /* 15. Дана строка “Versions: Java  5, Java 6, Java
    7, Java 8, Java 12.” Найти все подстроки "Java X" и распечатать их. */
    private static String fifteenthQuestion(String line) {

        // Versions: Java  5, Java 6, Java 7, Java 8, Java 12.

        var pattern = Pattern.compile("Java \\d+");

        var matcher = pattern.matcher(line);

        var sb = new StringBuilder();

        while (matcher.find()) {
            sb.append(line.substring(matcher.start(), matcher.end()) + "\n");
        }

        return sb.toString();
    }

    /* 16.	Найти слово, в котором число различных символов минимально.
    Слово может содержать буквы и цифры. Если таких слов несколько,
    найти первое из них. Например, в строке "fffff ab f 1234 jkjk"
    найденное слово должно быть "fffff". */
    private static String sixteenthQuestion(String line) {

        // Кажется, что уже было такое задание
        // fffff ab f 1234 jkjk

        var answer = Arrays.stream(line.split("\\s+")).min(Comparator.comparing(o -> o.chars().distinct().count()));
        return String.format("Найденное слово: %s", answer);
    }

    /* 17. Предложение состоит из нескольких слов,
     разделенных пробелами. Например: "One two three раз два три one1 two2 123".
     Найти количество слов, содержащих только символы латинского алфавита. */
    private static String seventeenthQuestion(String line) {

        // One two three раз два три one1 two2 123 -> 3

        var answer = Arrays.stream(line.split("\\s+"))
                .filter(word -> word.matches("[A-Za-z]+"))
                .count();

        return String.format("Количество слов: %s", answer);
    }

    /* 1.	Предложение состоит из нескольких слов, например:
    "Если есть хвосты по дз, начните с 1 не сданного задания. 123 324 111 4554".
     Среди слов, состоящих только из цифр, найти слово палиндром. */
    private static String eighteenthQuestion(String line) {

        // Если есть хвосты по дз, начните с 1 не сданного задания. 123 324 111 4554

        var answer = Arrays.stream(line.split("\\s+"))
                .filter(word -> word.matches("[0-9]+"))
                .filter(word -> {
                    var reversedLine = new StringBuilder(word).reverse().toString();
                    return word.equals(reversedLine);
                })
                .collect(Collectors.joining("\n"));

        return String.format("Найденные слова-палиндромы: %s\n", answer);
    }
}