package programmingLanguages.laboratories.firstDotFirstLaboratory;

public class Triangle {
    static class Point {
        int x, y;
        Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
    // Функция для вычисления расстояния между двумя точками
    static double distance(Point p1, Point p2) {
        return Math.sqrt(Math.pow(p2.x - p1.x, 2) + Math.pow(p2.y - p1.y, 2));
    }

    // Функция для вычисления периметра треугольника
    static double perimeter(Point p1, Point p2, Point p3) {
        return distance(p1, p2) + distance(p2, p3) + distance(p3, p1);
    }

    // Функция для нахождения треугольника с наибольшим периметром
    static double maxPerimeter(Point[] points) {
        double maxPerimeter = 0;

        // Перебираем все тройки точек
        for (int i = 0; i < points.length - 2; i++) {
            for (int j = i + 1; j < points.length - 1; j++) {
                for (int k = j + 1; k < points.length; k++) {
                    double currentPerimeter = perimeter(points[i], points[j], points[k]);
                    maxPerimeter = Math.max(maxPerimeter, currentPerimeter);
                }
            }
        }

        return maxPerimeter;
    }
}
