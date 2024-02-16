package programmingLanguages.laboratories.firstLaboratory;

import java.lang.Math;

public class FourthClass {
    public static double strangeFunc(double a, double b) {
        return Math.sqrt(Math.pow(a, 2) + Math.pow(b, 2) + Math.pow(Math.sin(a * b), 2));
    }
}
