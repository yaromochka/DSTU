package programmingLanguages.laboratories.secondLaboratory;

import java.util.Scanner;


public class Main {
    public static void main(String[] args) {
        var in = new Scanner(System.in);
        System.out.print("Введите номер задания: ");
        try {
            var number = in.nextInt();
            HelpClass.pointOfStart(number);
        } catch (Exception e) {
            System.out.println("Неверно введён номер задания");
        }
    }
}
