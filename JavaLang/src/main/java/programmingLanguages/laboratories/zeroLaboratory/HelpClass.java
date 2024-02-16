package programmingLanguages.laboratories.zeroLaboratory;

/*
 * В пояснениях не нуждается (надеюсь)
 * */

import programmingLanguages.laboratories.zeroLaboratory.Owner.Pet;

public class HelpClass {

    public static int a = 1;
    public static int b = 3;
    public static int c = 9;
    public static int d = 27;

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
            case (14) -> fourteenQuestion();
            case (15) -> fifteenthQuestion();
            case (16) -> sixteenthQuestion();
            case (17) -> seventeenthQuestion();
            case (18) -> eighteenthQuestion();
            default -> System.out.println("Неверно введён номер задания");
        }
    }

    public static void firstQuestion() {
        var jedi = "Какое-нибудь значение";
        System.out.println(jedi);
    }

    public static void secondQuestion() {
        var number = 2;
        System.out.println(Integer.toString(number * number));
    }

    public static void thirdQuestion() {
        for (var i = 0; i < 10; i++) System.out.println("May the Force be with you.");
    }

    public static void fourthQuestion() {
        var s = "Anakin ";
        System.out.print(s);
        // System.out.println("how are you? ");
        // System.out.println("I am ");
        // System.out.println("glad ");
        // System.out.print("to see you.");
        // System.out.println("This Lightsaber ");
        System.out.print("is ");
        // System.out.print("Your");
        System.out.print("a hero");
        System.out.println("!");
    }

    public static void fifthQuestion() {
        var mol = "Mol";
        var darth = "Mol";
        var text = "Darth " + mol + "!";
        System.out.println(text);
    }

    public static void sixthQuestion() {
        var result = -a + b - c + d;
        System.out.println(result);
    }

    public static void seventhQuestion() {
        System.out.println(sqr(5));
    }

    public static int sqr(int num) {
        return num * num;
    }

    public static void eighthQuestion() {
        // int a = 1;
        double b = 1.5;
        double c = b + 1.5;
        // int d = a + 12;
        // double e = 12.3;
        // String s = "Luke, " + a;
        String s1 = "Twice ";
        // String s2 = "a";
        String s3 = s1 + "the pride, ";
        String s4 = " the fall.";
        System.out.println(s3 + c + s4);
    }

    public static void ninthQuestion() {
        print("The power is easy to use!");
        print("The power opens many opportunities!");
    }

    public static void print(String text) {
        System.out.println(text);
    }

    public static void tenthQuestion() {
        var firstOwner = new Owner();
        var firstPet = new Pet();

        firstOwner.name = "Mike";
        firstPet.kind = "cat";
        firstPet.color = "black";

        firstOwner.pet = firstPet;
        firstOwner.say();
    }

    public static void eleventhQuestion() {
        increaseSpeed(700);
    }

    public static void increaseSpeed(int speed) {
        speed = speed + 100;
        System.out.println("Your speed is " + speed + "km/h");
    }

    public static void twelfthQuestion() {
        var zam = new Zam();
        var dron = new Dron();
        zam.spy = dron;
        dron.hunter = zam;
    }

    public static class Zam {
        public int kam;
        public int dam;
        public Dron spy;
    }

    public static class Dron {
        public int tron;
        public int kron;
        public Zam hunter;
    }

    public static void thirteenthQuestion() {
        var firstJedi = new Jedi();
        firstJedi.name = "Obi-Wan";
        var secondJedi = new Jedi();
        secondJedi.name = "Anakin";
        var thirdJedi = new Jedi();
        thirdJedi.name = "Joda";
        System.out.println(thirdJedi.name);
    }

    public static class Jedi {
        public String name;
    }

    public static void fourteenQuestion() {
        var firstClone = new Clone();
        var secondClone = new Clone();
        var thirdClone = new Clone();
        var fourthClone = new Clone();
        var fifthClone = new Clone();
        var sixthClone = new Clone();
        var seventhClone = new Clone();
        var eighthClone = new Clone();
        Clone ninthClone;
        Clone teenthClone;
    }

    public static class Clone {
    }

    public static void fifteenthQuestion() {
        var clone1 = new Clone1();
        var clone2 = new Clone2();
        var clone3 = new Clone3();
        var dias = new Dias();
        clone1.owner = dias;
        clone2.owner = dias;
        clone3.owner = dias;
    }

    public static class Clone1 {
        public Dias owner;
    }

    public static class Clone2 {
        public Dias owner;
    }

    public static class Clone3 {
        public Dias owner;
    }

    public static class Dias {
    }

    public static void sixteenthQuestion() {
        System.out.println(getWeight(888));
    }

    public static double getWeight(int weight) {
        return weight / 6.0;
    }

    public static void seventeenthQuestion() {
        print3("dump");
        print3("cargo");
    }

    public static void print3(String s) {
        System.out.print(s + " " + s + " " + s + " ");
    }

    public static void eighteenthQuestion() {
        System.out.println(min(12, 33));
        System.out.println(min(-20, 0));
        System.out.println(min(-10, -20));
    }

    public static int min(int a, int b) {
        return a < b ? a : b;
    }
}