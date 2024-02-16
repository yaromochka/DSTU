package programmingLanguages.laboratories.firstDotFirstLaboratory;

import java.util.Locale;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class TenthMethod {
    public static long countConsonants(String str) {
        return str.toLowerCase(Locale.ROOT).chars()
                .mapToObj(c -> (char) c)
                .filter(c -> Character.isLetter(c) && countVowels(String.valueOf(c)) != 1)
                .count();
    }

    public static long countVowels(String str) {
        Set<Character> vowels = Stream.of('а', 'о', 'у', 'ы', 'э', 'е', 'ё', 'и', 'ю', 'я',
                'a', 'e', 'i', 'o', 'u').collect(Collectors.toSet());
        // Locale.ROOT представляет собой константу в классе Locale в Java, предназначенную для представления
        // нейтральной локали.
        // Нейтральная локаль означает отсутствие спецификации конкретного региона, языка или варианта.
        return str.toLowerCase(Locale.ROOT).chars()
                .mapToObj(c -> (char) c)
                .filter(vowels::contains)
                .count();
    }
}
