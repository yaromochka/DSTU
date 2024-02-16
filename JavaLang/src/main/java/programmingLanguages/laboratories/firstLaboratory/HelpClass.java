package programmingLanguages.laboratories.firstLaboratory;

import java.util.Scanner;
import java.util.Comparator;
import java.util.Random;
import java.lang.Math;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Locale;

import static programmingLanguages.laboratories.firstLaboratory.Methods4Solutions.*;
import static programmingLanguages.laboratories.firstLaboratory.FourthClass.strangeFunc;
import static programmingLanguages.laboratories.firstLaboratory.Factorial.factorial;


public class HelpClass {
    static final Scanner in = new Scanner(System.in).useLocale(Locale.US);
    static final int[] firstArray = new Random().ints(20, -100, 100).toArray();
    static final int[] secondArray = new Random().ints(15, -100, 100).toArray();
    static final int[] thirdArray = new Random().ints(10, -100, 100).toArray();

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
            default -> System.out.println("Неверно введён номер задания");
        }
    }


    /**
     * 1. Вычислить z = Math.exp(Math.abs(max_x)) - Math.exp(Math.abs(max_y))) / Math.sqrt((Math.abs(max_x * max_y)))
     * где - max_x наибольший элемент массива X(20); max_y - наибольший элемент массива Y(15).
     * Для вычисления наибольшего элемента массива использовать функцию.
     */
    public static void firstQuestion() {
        var max_x = Arrays.stream(firstArray).max().orElseThrow();
        var max_y = Arrays.stream(secondArray).max().orElseThrow();
        var z = Math.exp(Math.abs(max_x)) - Math.exp(Math.abs(max_y)) / Math.sqrt((Math.abs(max_x * max_y)));
        System.out.printf("z = ( e ^ |%d| - e ^ |%d| ) / sqrt(| %d * %d |) = %f", max_x, max_y, max_x, max_y, z);
    }

    /**
     * 2.	Даны массивы действительных чисел А(20), В(15), С(10).
     * Вычислить (S + T + K) / 2 где S, T, K – суммы положительных элементов массивов А, В, С соответственно.
     * Для вычисления суммы положительных элементов использовать функцию.
     */
    public static void secondQuestion() {
        var S = sum(firstArray);
        var T = sum(secondArray);
        var K = sum(thirdArray);
        System.out.printf("(%s + %s + %s) / 2 = %s", S, T, K, (S + T + K) / 2);
    }

    /**
     * Даны целые числа m, n. Вычислить c = m!/n!(m - n)!. Для вычисления факториала использовать функцию.
     */
    public static void thirdQuestion() {
        var m = 4;
        var n = 6;
        var result = factorial(n) / (factorial(m) * factorial(n - m));
        System.out.printf("C = %s! / %s! ((%s! - %s!)) = %s", n, m, n, m, result);
    }

    /**
     * 4.	Даны действительные х, у, z. Составить программу вычисления значения
     * s = sqrt(x ** 2 + y ** 2 + sin ** 2 (xy)) + sqrt(x ** 2 + z ** 2 + sin ** 2 (xz)) +
     * + sqrt(y ** 2 + z ** 2 + sin ** 2 (yz)) используя функцию для вычисления выражения
     * sqrt(a ** 2 + b ** 2 + sin ** 2 (ab))
     */
    public static void fourthQuestion() {
        Random rand = new Random();
        var x = rand.nextDouble() * 10;
        var y = rand.nextDouble() * 10;
        var z = rand.nextDouble() * 100;
        var result = Math.sqrt(strangeFunc(x, y) + strangeFunc(x, z) + strangeFunc(y, z));
        System.out.printf("x = %s, y = %s, z = %s, result = %s", x, y, z, result);
    }

    /**
     * 5.	Составить программу для вычисления среднего арифметического положительных элементов
     * массивов Х(20), Y(15), Z(10), используя в качестве подпрограммы функцию.
     */
    public static void fifthQuestion() {
        System.out.printf("Average:\nX(20) = %s\nY(15) = %s\nZ(10) = %s\n", sumAverage(firstArray), sumAverage(secondArray), sumAverage(thirdArray));
    }

    /** 6.	Даны массивы A(15), B(10),C(12). Вычислить */
    public static void sixthQuestion() {
        System.out.printf("min a = %s\n", minInArray(secondArray));
        if (Math.abs(minInArray(secondArray)) > 10) {
            var minFirst = minInArray(firstArray);
            var minThird = minInArray(thirdArray);
            System.out.printf("min b + min c = %s + %s = %s", minFirst, minThird, minFirst + minThird);
        }
        else {
            System.out.printf("1 + min|c| = %s", minInArrayWithAbs(thirdArray));
        }
    }

    /** 7.	Дан массив D(40) вещественных чисел. Найти среднее геометрическое его элементов,
     *  которые удовлетворяют условию  0 <di<12. Для вычислений использовать функцию */
    public static void seventhQuestion() {
        var fortyArray = new Random().doubles(40, -100, 100).toArray();
        System.out.printf("Среднее геометрическое равно: %s", geometryMean(fortyArray));
    }

    /** 8.	Дан массив А(80) целых  чисел. Найти сумму и количество теx элементов массива,
     * которые отрицательны и нечетны. Использовать в качестве подпрограммы процедуру. */
    public static void eighthQuestion() {
        var eightyArray = new Random().ints(10, -100, 100).toArray();
        negativeOdd(eightyArray);
    }

    /** 9.	Функция, вычисляющая среднее арифметическое элементов массива
     Написать функцию, которая вычисляет среднее арифметическое элементов массива,
     переданного ей в качестве аргумента.
     */
    public static void ninthQuestion() {
        System.out.printf("Среднее арифметическое массива равно %s", arMean(firstArray));
    }

    /** 10.	Отсортировать массив по возрастанию суммы цифр
     Дан одномерный массив, состоящий из натуральных чисел. Выполнить сортировку
     данного массива по возрастанию суммы цифр чисел. Например, дан массив чисел [14, 30, 103].
     После сортировки он будет таким: [30, 103, 14], так как сумма цифр числа 30 составляет 3, числа 103
     равна 4, числа 14 равна 5.
     */
    public static void tenthQuestion() {
        var result = Arrays.stream(firstArray)
                .boxed()
                .sorted(Comparator.comparingInt(Methods4Solutions::sumDigits))
                .toArray();

        System.out.printf("Массив: %s\nСортированный массив: %s", Arrays.toString(firstArray), Arrays.toString(result));
    }

    /** 11.	Вывести на экран исходный массив, отсортированный массив,
     *  а также для контроля сумму цифр каждого числа отсортированного массива.*/
    public static void eleventhQuestion() {
        var result = Arrays.stream(firstArray)
                .boxed()
                .sorted(Comparator.comparingInt(Methods4Solutions::sumDigits))
                .toArray();
        var digitsArray = Arrays.stream(firstArray)
                .boxed()
                .sorted(Comparator.comparingInt(Methods4Solutions::sumDigits))
                .map(Methods4Solutions::sumDigits)
                .toArray();
        System.out.printf("Массив: %s\nСортированный массив: %s\nМассив суммы цифр: %s",
                Arrays.toString(firstArray), Arrays.toString(result), Arrays.toString(digitsArray));
    }

    /** 12.	Определить количество разрядов числа
     Написать функцию, которая определяет количество разрядов введенного целого числа.
     */
    public static void twelfthQuestion() {
        var randNumber = new Random().nextInt();
        System.out.printf("Количество разрядов в числе %s равно %s", randNumber, Integer.toString(Math.abs(randNumber)).length());
    }

    /** 13.	Сумма ряда с факториалом. Вычислить сумму ряда
     s = ∑ (-1) * i * (x / i!)
     i=1..5
     Значение x вводится с клавиатуры.
     */
    public static void thirteenthQuestion() {
        System.out.print("Введите число для которого вы хотите посчитать сумму ряда: ");
        try {
            var x = in.nextInt();
            var s = 0.0;
            for (int i = 1; i < 6; i++) {
                s +=  ((-1) * i * ((double) x / factorial(i)));
            }
            System.out.printf("Для x равному %s сумма ряда равна %s", x, s);
        } catch (Exception e) {
            System.out.print("Неверно введено число");
        }
    }

    /** 14.	Изменить порядок слов в строке на обратный
     Вводится строка, состоящая из слов, разделенных пробелами.
     Следует заменить ее на строку, в которой слова идут в обратном порядке
     по сравнению с исходной строкой. Вывести измененную строку на экран.
     */
    public static void fourteenthQuestion() {
        System.out.print("Введите строку, которую хотите развернуть: ");
        var line = in.nextLine();
        System.out.println(new StringBuilder(line).reverse());
    }

    /** 15.	Функция бинарного поиска в массиве
     Пользователь вводит число. Сообщить, есть ли оно в массиве,
     элементы которого расположены по возрастанию значений, а также, если есть,
     в каком месте находится. При решении задачи использовать бинарный (двоичный) поиск,
     который оформить в виде отдельной функции.
     */
    public static void fifteenthQuestion() {
        System.out.print("Введите число, которое бы хотели найти в массиве: ");
        var numberToSearch = in.nextInt();
        var index = Arrays.binarySearch(firstArray, numberToSearch);
        System.out.printf("Элементы массива: %s\n", Arrays.toString(firstArray));
        System.out.print(index > 0 ? "Число " + numberToSearch + " имеет индекс " + index :
                "Число " + numberToSearch + " не найдено в массиве");
    }

    /** 16.	Вычисление наибольших общих делителей
     Найти наибольшие общие делители (НОД) для множества пар чисел.
     */
    public static void sixteenthQuestion() {
        System.out.print("Введите два числа через пробел, НОД которых хотите найти: ");
        var lineOfNumber = in.nextLine().split(" ");
        var firstNumber = Integer.parseInt(lineOfNumber[0]);
        var secondNumber = Integer.parseInt(lineOfNumber[1]);
        System.out.printf("НОД чисел %s и %s равен %s", firstNumber,
        secondNumber, gcd(firstNumber, secondNumber));
    }

    /** 17.	Найти площади разных фигур
     В зависимости от выбора пользователя вычислить площадь круга,
     прямоугольника или треугольника. Для вычисления площади каждой фигуры
     должна быть написана отдельная функция.
     */
    public static void seventeenthQuestion() {
        System.out.println("Введите название фигуры: ");
        var figureName = in.next().toLowerCase();
        // for triangle
        if (figureName.equals("треугольник")) {
            System.out.print("Введите длину основания и высоты через пробел: ");
            var lineOfNumber = in.nextLine().split(" ");
            var baseTriangle = Integer.parseInt(lineOfNumber[0]);
            var highTriangle = Integer.parseInt(lineOfNumber[1]);
            System.out.printf("Площадь треугольника с длиной основания %s и %s высоты равна %s",
            baseTriangle, highTriangle, squareTriangle(baseTriangle, highTriangle));
        // for rectangle
        } else if (figureName.equals("прямоугольник")) {
            System.out.print("Введите длину двух сторон прямоугольника через пробел: ");
            var lineOfNumber = in.nextLine().split(" ");
            var biggerSideLength = Integer.parseInt(lineOfNumber[0]);
            var smallerSideLength = Integer.parseInt(lineOfNumber[1]);
            System.out.printf("Площадь прямоугольника со сторонами %s и %s равна %s",
            biggerSideLength, smallerSideLength, squareRectangle(biggerSideLength, smallerSideLength));
        // for circle
        } else if (figureName.equals("круг")) {
            System.out.print("Введите радиус круга: ");
            var radius = in.nextInt();
            System.out.printf("Площадь круга с радиусом %s равна %s", radius, squareCircle(radius));
        // other
        } else System.out.println("Площадь такой фигуры посчитать не можем =(");
    }

    /** 18.	Найти массив с максимальной суммой элементов
     Сгенерировать десять массивов из случайных чисел. Вывести их и сумму их элементов на экран.
     Найти среди них один с максимальной суммой элементов.
     Указать какой он по счету, повторно вывести этот массив и сумму его элементов.
     Заполнение массива и подсчет суммы его элементов оформить в виде отдельной функции.
     */
    public static void eighteenthQuestion() {
        int[][] arrays = new int[10][10]; // Создаем массив из 10 массивов

        // Заполняем массивы случайными числами и выводим их
        for (var i = 0; i < 10; i++) {
            fillArray(arrays[i]);
            System.out.println("Массив " + (i + 1) + ": ");
            printArray(arrays[i]);
            System.out.println("Сумма элементов: " + sumArray(arrays[i]));
            System.out.println();
        }

        // Находим массив с максимальной суммой элементов
        var maxSum = Integer.MIN_VALUE;
        var indexOfMaxSum = -1;
        for (var i = 0; i < 10; i++) {
            int sum = sumArray(arrays[i]);
            if (sum > maxSum) {
                maxSum = sum;
                indexOfMaxSum = i;
            }
        }

        // Выводим массив с максимальной суммой и его сумму
        System.out.println("Массив с максимальной суммой элементов (массив " + (indexOfMaxSum + 1) + "): ");
        printArray(arrays[indexOfMaxSum]);
        System.out.println("Сумма элементов: " + maxSum);
    }

    // Функция для заполнения массива случайными числами
    public static void fillArray(int[] array) {
        var random = new Random();
        for (var i = 0; i < array.length; i++) {
            array[i] = random.nextInt(100); // Генерируем случайное число от 0 до 99
        }
    }

    // Функция для вывода массива
    public static void printArray(int[] array) {
        for (var i = 0; i < array.length; i++) {
            System.out.print(array[i] + " ");
        }
        System.out.println();
    }

    // Функция для подсчета суммы элементов массива
    public static int sumArray(int[] array) {
        var sum = 0;
        for (var i = 0; i < array.length; i++) {
            sum += array[i];
        }
        return sum;
    }

    /** 19.	Вычислить сумму элементов главной или побочной диагонали матрицы
     Дана квадратная матрица. Вычислить сумму элементов главной или побочной
     диагонали в зависимости от выбора пользователя. Сумма элементов любой диагонали
     должна вычисляться в одной и той же функции.
     */
    public static void nineteenthQuestion() {
        int[][] randomMatrix = generateRandomMatrix(3, 3);
        System.out.print("Сумму элементов какой диагонали требуется вычислить: ");
        var diagonal = in.next().toLowerCase();
        System.out.println("Матрица: ");
        Arrays.stream(randomMatrix).map(Arrays::toString).forEach(System.out::println);
        if (diagonal.equals("побочной")) {
            System.out.printf("Сумма элементов побочной диагонали равна %s", secondaryDiagonal(randomMatrix));
        } else if (diagonal.equals("главной")) {
            System.out.printf("Сумма элементов главной диагонали равна %s", mainDiagonal(randomMatrix));
        } else {
            System.out.println("Неверное введены данные");
        }
    }

    /** 20.	Функция перевода десятичного числа в двоичное
     Переводить в двоичную систему счисления вводимые в десятичной
     системе счисления числа до тех пор, пока не будет введен 0.
     Для перевода десятичного числа в двоичное написать функцию.
     */
    public static void twentiethQuestion() {
        System.out.print("Введите число, которое хотите перевести в двоичное (для остановки введите 0): ");
        var number = in.nextInt();
        while (number != 0) {
            System.out.printf("Десятичное число %s в двоичной записи равно %s\n", number, decimalToBinary(number));
            System.out.print("Введите ещё одно число или 0, если хотите закончить: ");
            number = in.nextInt();
        }
    }

    /** 21.	Вычислить значения функции y=f(x) на заданном диапазоне
     Вычислить значения нижеприведенной функции в диапазоне значений x от -10 до 10
     включительно с шагом, равным 1.
     y = x2 при -5 <= x <= 5;
     y = 2*|x|-1 при x < -5;
     y = 2x при x > 5.
     Вычисление значения функции оформить в виде программной функции,
     которая принимает значение x, а возвращает полученное значение функции (y).
     */
    public static void twentyFirstQuestion() {
        System.out.print("Введите диапазон из двух чисел через пробел: ");
        var lineOfNumber = in.nextLine().split(" ");
        var firstNumber = Integer.parseInt(lineOfNumber[0]);
        var secondNumber = Integer.parseInt(lineOfNumber[1]);
        for (var i = firstNumber; i < secondNumber; i++) {
            System.out.printf("Значении %s даёт значение функции равное %s\n", i, strangeFuncToo(i));
        }
    }

    /** 22.	Функция заполнения массива случайными числами
     Написать функцию, которая заполняет массив случайными числами в диапазоне,
     указанном пользователем. Функция должна принимать два аргумента - начало диапазона
     и его конец, при этом ничего не возвращать. Вывод значений элементов массива должен
     происходить в основной ветке программы.
     */
    public static void twentySecondQuestion() {
        System.out.print("Введите диапазон из двух чисел через пробел: ");
        var lineOfNumber = in.nextLine().split(" ");
        var firstNumber = Integer.parseInt(lineOfNumber[0]);
        var secondNumber = Integer.parseInt(lineOfNumber[1]);
        int[][] randomMatrix = generateRandomMatrix(3, 3, firstNumber, secondNumber);
        System.out.println("Матрица: ");
        Arrays.stream(randomMatrix).map(Arrays::toString).forEach(System.out::println);
    }

    /** 23.	Написать функцию вычисления величины силы тока
     *  на участке электрической цепи сопротивлением R Ом при напряжении U В.*/
    public static void twentyThirdQuestion() {
        System.out.print("Введите значение сопротивления и напряжения (через пробел): ");
        var lineOfNumber = in.nextLine().split(" ");
        var R = Integer.parseInt(lineOfNumber[0]);
        var I = Integer.parseInt(lineOfNumber[1]);
        System.out.printf("Значение силы тока на участке цепи равно %s", I * R);
    }

    /** 24.	Написать функцию вычисления напряжения на каждом из последовательно
     соединенных участков электрической цепи сопротивлением R1, R2, R3 Ом, если сила
     тока при напряжении U В составляет I А.
     */
    public static void twentyFourthQuestion() {
        System.out.print("Введите три значения сопротивления (через пробел): ");
        String[] resistanceArray = in.nextLine().split(" ");
        System.out.print("Введите значение силы тока: ");
        var I = in.nextInt();
        for (var i = 0; i < 3; i++) {
            System.out.printf("При I = %s и R = %s напряжение U = %s\n",
                    I, resistanceArray[i], I * Integer.parseInt(resistanceArray[i]));
        }
    }

    /** 25.	Составить программу для ввода на экран номера дня недели и вывода
     * соответствующего ему дня недели на русском языке. */
    public static void twentyFifthQuestion() {
        // Создание и заполнение словаря
        HashMap<Integer, String> mapOfDays = new HashMap<>();
        mapOfDays.put(1, "Понедельник");
        mapOfDays.put(2, "Вторник");
        mapOfDays.put(3, "Среда");
        mapOfDays.put(4, "Четверг");
        mapOfDays.put(5, "Пятница");
        mapOfDays.put(6, "Суббота");
        mapOfDays.put(7, "Воскресенье");

        System.out.print("Введите номер дня недели: ");
        var numberOfDay = in.nextInt();
        System.out.printf("Под номером %s день под названием %s", numberOfDay, mapOfDays.get(numberOfDay));
    }
}
