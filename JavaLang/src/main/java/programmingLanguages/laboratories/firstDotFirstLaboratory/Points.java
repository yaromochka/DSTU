package programmingLanguages.laboratories.firstDotFirstLaboratory;

import java.awt.*;

public class Points {
    // Метод для вычисления расстояния между двумя точками
    public static double distance(Point p1, Point p2) {
        return Math.sqrt(Math.pow(p1.getX() - p2.getX(), 2) + Math.pow(p1.getY() - p2.getY(), 2));
    }

    // Метод для вычисления суммы расстояний от точки до всех остальных точек
    public static double totalDistance(Point center, Point[] points) {
        double sum = 0;
        for (Point point : points) {
            sum += distance(center, point);
        }
        return sum;
    }

    // Метод для нахождения точки с минимальной суммой расстояний до остальных точек
    public static Point findMinDistancePoint(Point[] points) {
        Point minPoint = null;
        double minDistance = Double.MAX_VALUE;

        // Итерируемся по всем точкам и находим сумму расстояний для каждой из них
        for (Point point : points) {
            double distance = totalDistance(point, points);
            if (distance < minDistance) {
                minDistance = distance;
                minPoint = point;
            }
        }
        return minPoint;
    }
}
