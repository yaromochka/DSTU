package programmingLanguages.laboratories.thirdDotFirstLaboratory;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class HelpClassThirdDotFirst {
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
            default -> {
                return "Неверно введён номер задания";
            }
        }
    }

    /* 1. Написать регулярное выражение, определяющее является
    ли данная строка строкой "abcdefghijklmnopqrstuv18340" или нет.
    – пример правильных выражений: abcdefghijklmnopqrstuv18340.
    – пример неправильных выражений: abcdefghijklmnoasdfasdpqrstuv18340. */
    private static String firstQuestion(String line) {
        return String.valueOf(Pattern.matches("abcdefghijklmnopqrstuv18340", line.strip()));
    }

    /* 2. Написать регулярное выражение, определяющее является ли данная
    строка GUID с или без скобок. Где GUID это строчка, состоящая из 8, 4, 4, 4, 12 шестнадцатеричных цифр разделенных тире.
    – пример правильных выражений: e02fd0e4-00fd-090A-ca30-0d00a0038ba0.
    – пример неправильных выражений: e02fd0e400fd090Aca300d00a0038ba0. */
    private static String secondQuestion(String line) {
        return String.valueOf(Pattern.matches("^(\\{?[0-9a-fA-F]{8}-(?:[0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}}?)$", line.strip()));
    }

    /* 3. Написать регулярное выражение, определяющее является ли заданная строка правильным MAC-адресом.
    – пример правильных выражений: aE:dC:cA:56:76:54.
    – пример неправильных выражений: 01:23:45:67:89:Az. */
    private static String thirdQuestion(String line) {
        return String.valueOf(Pattern.matches("^(?:[0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$", line.strip()));
    }

    /* 4. Написать регулярное выражение, определяющее является ли данная строчка
     валидным URL адресом. В данной задаче правильным URL считаются адреса http и https,
     явное указание протокола также может отсутствовать. Учитываются только адреса, состоящие
     из символов, т.е. IP адреса в качестве URL не присутствуют при проверке. Допускаются
     поддомены, указание порта доступа через двоеточие, GET запросы с передачей параметров,
     доступ к подпапкам на домене, допускается наличие якоря через решетку. Однобуквенные
     домены считаются запрещенными. Запрещены спецсимволы, например «–» в начале и конце
     имени домена. Запрещен символ «_» и пробел в имени домена. При составлении регулярного
     выражения ориентируйтесь на список правильных и неправильных выражений заданных ниже.
      – пример правильных выражений: http://www.example.com, http://example.com.
      – пример неправильных выражений: Just Text, http://a.com. */
    private static String fourthQuestion(String line) {
        return String.valueOf(Pattern.matches("^https?://(?:www\\.)?[a-z0-9]{2,}\\.(com|ru)$", line.strip()));
    }

    /* 5. Написать регулярное выражение, определяющее является ли данная строчка
     шестнадцатиричным идентификатором цвета в HTML. Где #FFFFFF для белого, #000000
     для черного, #FF0000 для красного и т.д.
     – пример правильных выражений: #FFFFFF, #FF3421, #00ff00.
     – пример неправильных выражений: 232323, f#fddee, #fd2. */
    private static String fifthQuestion(String line ) {
        return String.valueOf(Pattern.matches("^#[0-9a-fA-F]{6}$", line.strip()));
    }

    /* 6. Написать регулярное выражение, определяющее является ли данная строчка
     датой в формате dd/mm/yyyy. Начиная с 1600 года до 9999 года.
     – пример правильных выражений: 29/02/2000, 30/04/2003, 01/01/2003.
     – пример неправильных выражений: 29/02/2001, 30-04-2003, 1/1/1899. */
    private static String sixthQuestion(String line) {
        return String.valueOf(Pattern.matches("^(0[1-9]|1\\d|2[0-8])/(0[1-9]|1[0-2])/((?:1[6-9]|[2-9]\\d)?\\d{2})$" +
                "|^29/02/(?:(?:1[6-9]|[2-9]\\d)(?:0[48]|[2468][048]|[13579][26])|(?:16|[2468][048]|[3579][26])00)$", line.strip()));
    }

    /* 7. Написать регулярное выражение, определяющее является ли данная строчка
     валидным E-mail адресом согласно RFC под номером 2822.
     – пример правильных выражений: user@example.com, root@localhost
     – пример неправильных выражений: bug@@@com.ru, @val.ru, Just Text2. */
    private static String seventhQuestion(String line) {
        return String.valueOf(Pattern.matches("^\\w+@\\w+(\\.)?\\w+$", line.strip()));
    }

    /* 8. Составить регулярное выражение, определяющее является ли заданная строка IP адресом,
     записанным в десятичном виде.
     – пример правильных выражений: 127.0.0.1, 255.255.255.0.
     – пример неправильных выражений: 1300.6.7.8, abc.def.gha.bcd. */
    private static String eighthQuestion(String line) {
        return String.valueOf(Pattern.matches("^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.)" +
                "{3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", line.strip()));
    }

    /* 9. Проверить, надежно ли составлен пароль. Пароль считается надежным,
    если он состоит из 8 или более символов. Где символом может быть английская
    буква, цифра и знак подчеркивания. Пароль должен содержать хотя бы одну
    заглавную букву, одну маленькую букву и одну цифру.
    – пример правильных выражений: C00l_Pass, SupperPas1.
    – пример неправильных выражений: Cool_pass, C00l. */
    private static String ninthQuestion(String line) {
        return String.valueOf(Pattern.matches("^(?=.*[A-Z])(?=.*[a-z])(?=.*\\d)[A-Za-z0-9_]{8,}$", line.strip()));
    }

    /* 10. Проверить является ли заданная строка шестизначным числом,
     записанным в десятичной системе счисления без нулей в старших разрядах.
     – пример правильных выражений: 123456, 234567.
     – пример неправильных выражений: 1234567, 12345. */
    private static String tenthQuestion(String line) {
        return String.valueOf(Pattern.matches("^[1-9]\\d{5}$", line.strip()));
    }

    /* 11. Есть текст со списками цен. Извлечь из него цены в USD, RUR, EU.
    – пример правильных выражений: 23.78 USD.
    – пример неправильных выражений: 22 UDD, 0.002 USD. */
    private static String eleventhQuestion(String line) {
        return String.valueOf(Pattern.matches("(\\d+(?:\\.\\d+)?)\\s+(USD|RUR|EU)", line.strip()));
    }

    /* 12. Проверить существуют ли в тексте цифры, за которыми не стоит «+».
    – пример правильных выражений: (3 + 5) – 9 × 4.
    – пример неправильных выражений: 2 * 9 – 6 × 5. */
    private static String twelfthQuestion(String line) {
        return String.valueOf(Pattern.matches("\\b\\d+\\s*\\+", line.strip()));
    }

    /* 13. Создать запрос для вывода только правильно написанных
    выражений со скобками (количество открытых и закрытых скобок должно быть одинаково).
    – пример правильных выражений: (3 + 5) – 9 × 4.
    – пример неправильных выражений: ((3 + 5) – 9 × 4. */
    private static String thirteenthQuestion(String line) {
        Pattern pattern = Pattern.compile("((\\([^()]*\\)[^()]*)*)");
        Matcher matcher = pattern.matcher(line);

        if (!matcher.matches()) {
            return String.valueOf(false);
        }

        int openBrackets = 0;
        int closeBrackets = 0;
        for (char c : line.toCharArray()) {
            if (c == '(') {
                openBrackets++;
            } else if (c == ')') {
                closeBrackets++;
            }
        }

        return String.valueOf(openBrackets == closeBrackets);
    }
}
