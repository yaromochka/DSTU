package programmingLanguages.laboratories.firstLaboratory;

import java.lang.Math;
import java.util.Arrays;
import java.util.Random;

public class Methods4Solutions {
    public static int sum(int[] a) {
        var counter = 0;
        for (var x : a)
            if (x > 0) counter += x;
        return counter;
    }

    /**
     * Если нет + элементов, то вернётся 0
     */
    public static int sumAverage(int[] a) {
        var counter = 0;
        var s = 0;
        for (var x : a) {
            if (x > 0) {
                counter += 1;
                s += x;
            }
        }
        return counter > 0 ? s / counter : 0;
    }

    public static int minInArray(int[] a) {
        var minimal = 1000000;
        for (var x: a) {
            if (x < minimal) minimal = x;
        }
        return minimal;
    }

    public static int minInArrayWithAbs(int[] a) {
        var minimal = 1000000;
        for (var x: a) {
            x = Math.abs(x);
            if (x < minimal) minimal = x;
        }
        return minimal;
    }

    public static double geometryMean(double[] a) {
        var s = 1.0;
        var counter = 0;
        for (var x: a) {
            if (0 <= x && x <= 12) {
                counter += 1;
                s *= x;
            }
        }
        return Math.pow(s, 1 / (double) counter);
    }

    public static void negativeOdd(int[] a) {
        var s = 0;
        var counter = 0;
        for (var x: a) {
            System.out.print(x + " ");
            if (Math.abs(x) % 2 != 0 && x < 0) {
                counter += 1;
                s += x;
            }
        }
        System.out.println();
        System.out.printf("Количество нечётный и отрицательных = %s, а сумма = %s", counter, s);
    }

    public static double arMean(int[] a) {
        var s = 0;
        var counter = 0;
        for (var x: a) {
            s += x;
            counter += 1;
        }
        return (double) s / (double) counter;
    }

    public static int sumDigits(int n) {
        var sumOfDigits = 0;
        n = Math.abs(n);

        while (n > 0) {
            sumOfDigits += n % 10;
            n /= 10;
        }
        return sumOfDigits;
    }

    // Используется банальный алгоритм Евклида с тернарным оператором
    public static int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }

    // Площадь круга
    public static double squareCircle(int r) {
        return Math.PI * Math.pow(r, 2);
    }

    // Просто площадь прямоугольника
    public static int squareRectangle(int firstSide, int secondSide) {
        return firstSide * secondSide;
    }

    // Полупроизведение основания на высоту
    public static double squareTriangle(int h, int base) {
        return h * base / 2.0;
    }

    /** Здесь использована перегрузка методов
     * Названия и функционал одинаковый
     * Но методы принимают разное количество аргументов*/
    public static int[][] generateRandomMatrix(int CountRows, int CountColumns) {
        Random random = new Random();
        return Arrays.stream(new int[CountRows][CountColumns])
                .map(row -> Arrays.stream(row)
                        .map(col -> random.nextInt(100))
                        .toArray())
                .toArray(int[][]::new);
    }

    // Генерация рандомной матрицы
    public static int[][] generateRandomMatrix(int CountRows, int CountColumns, int firstNumber, int secondNumber) {
        Random random = new Random();
        return Arrays.stream(new int[CountRows][CountColumns])
                .map(row -> Arrays.stream(row)
                        .map(col -> random.nextInt(firstNumber, secondNumber))
                        .toArray())
                .toArray(int[][]::new);
    }

    // Сумма элементов побочной диагонали
    public static int secondaryDiagonal(int[][] matrix) {
        var s = 0;
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                if (matrix[i].length - j - 1 == i) {
                    s += matrix[i][j];
                }
            }
        }
        return s;
    }

    // Сумма элементов главной диагонали
    public static int mainDiagonal(int[][] matrix) {
        var s = 0;
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                if (i == j) {
                    s += matrix[i][j];
                }
            }
        }
        return s;
    }

    // Перевод десятичного числа в двоичную запись
    public static String decimalToBinary(int num) {
        StringBuilder s = new StringBuilder();
        while (num > 0) {
            s.insert(0, (num % 2));
            num /= 2;
        }
        return s.toString();
    }

    // Странная функция короч
    /** y = x2 при -5 <= x <= 5;
     y = 2*|x|-1 при x < -5;
     y = 2x при x > 5.
     */
    public static int strangeFuncToo(int x) {
        if (-5 <= x && x <= 5) return x * x;
        else if (x < -5) return 2 * Math.abs(x) - 1;
        else return 2 * x;
    }
}
