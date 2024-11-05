package programmingLanguages.laboratories.secondLaboratory;


public class HelpClass {
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
            default -> System.out.println("Неверно введён номер задания");
        }
    }

    /** 1. Расставьте правильно операторы приведения типа, чтобы получился ответ: d = 3.765. Операторы — в условии. */
    public static void firstQuestion() {
        int a = 15;
        int b = 4;
        // Добавил явное преобразование во float
        float c = (float) a / b;
        double d = a * 1e-3 + c;
        System.out.println(d);
    }

    /** 2. Давайте тоже найдем решение задачи: у нас есть какие-то переменные,
     * преобразованные в другой тип, но их недостаточно. Нужно добавить одну
     * операцию по преобразованию типа, чтобы получался нужный нам ответ b = 0.*/
    public static void secondQuestion() {
        float f = (float) 128.50;
        int i = (int) f;
        // Ответ 256, но округлив байтом получаем 0
        int b = (short) (i + f);
        System.out.println((byte) b);
    }

    /** 3. Даны short number = 9, char zero = ‘0’ и int nine = (zero + number).
     Добавьте одну операцию по преобразованию типа, чтобы получился красивый правильный ответ: 9.
     */
    public static void thirdQuestion() {
        short number = 9;
        char zero = '0';
        int nine = (zero + number);
        // Выводим как чар т.к. чар нуля имеет код символа 0
        System.out.println((char) nine);
    }

    /** 4. Уберите ненужные операторы приведения типа, чтобы получился ответ: result: 1000.0 */
    public static void fourthQuestion() {
        double d = (short) 2.50256e2d;
        // Убрал здесь шорт, чтобы число не уменьшалось т.к. чар д занимает больше памяти
        char c = 'd';
        short s = (short) 2.22;
        int i = 150000;
        float f = 0.50f;
        double result = f + (i / c) - (d * s) - 500e-3;
        System.out.println("result: " + result);
    }

    /** 5. Уберите ненужные операторы приведения типа, чтобы получился ответ: 1234567. */
    public static void fifthQuestion() {
        // Удалил везде byte кроме m. Метод проб...
        long l = 1234_564_890L;  //1234564890
        int x = 0b1000_1100_1010; //1102
        double m = (byte) 110_987_654_6299.123_34;  //127.12334
        float f = l++ + 10 + ++x - (float) m;  //1234564890+10+1103+127.12334
        l = (long) f / 1000;
        System.out.println(l);
    }

    /** 6. Нужно добавить одну операцию по преобразованию типа,
     * чтобы получался ответ: d = 2.941. Пример вывода: 2.9411764705882355*/
    public static void sixthQuestion() {
        int a = 50;
        int b = 17;
        // Явно приводим к флоату для повышения точности. Переменная b к флоату приводится неявно
        double d = (float) a / b;
        System.out.println(d);
    }

    /** 7. Нужно добавить одну операцию по преобразованию типа, чтобы получался ответ: d = 1.0 */
    public static void seventhQuestion() {
        int a = 257;
        int b = 4;
        int c = 3;
        int e = 2;
        double d = (byte) a + b / c / e; // Перед плюсом всегда ноль
        // Округлили байтом 257.0 -> 1.0
        System.out.println(d);
    }

    /** 8. Вам надо добавить одну операцию по преобразованию типа, чтобы получался ответ: d = 5.5. */
    public static void eighthQuestion() {
        int a = 5;
        int b = 4;
        int c = 3;
        int e = 2;
        // Скобки делают там единичку. Получаем 1/2 и приводим явно к флоату, чтобы сохранить точность
        // (иначе останется 0)
        double d = a + (float) (b / c) / e;
        System.out.println(d);
    }
}
