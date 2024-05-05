package programmingLanguages.laboratories.GUI.DatabaseHelp;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.*;

public class DataBaseDishes {

    public Map<String, ArrayList<String>> map = new HashMap<>();
    {
        map.put("Филе индейки", new ArrayList<>(List.of("Филе индейки")));
        map.put("Картошка", new ArrayList<>(List.of("Картошка")));
        map.put("Доширак с говядиной", new ArrayList<>(List.of("Доширак с говядиной")));
        map.put("Сало", new ArrayList<>(List.of("Сало")));
        map.put("Бефстроганов", new ArrayList<>(Arrays.asList("Говядина", "Лук репчатый", "Томатная паста", "Сметана 20%")));
        map.put("Борщ со свёклой", new ArrayList<>(Arrays.asList("Картошка", "Лук репчатый", "Томатная паста", "Свёкла", "Морковь")));
        map.put("Чебупели", new ArrayList<>(List.of("Чебупели")));
        map.put("Пельмени", new ArrayList<>(List.of("Пельмени")));
        map.put("Шашлык свиной", new ArrayList<>(List.of("Свинина")));
        map.put("Роллы с курицей", new ArrayList<>(Arrays.asList("Куриное филе", "Рис круглозёрный")));
        map.put("Биг Мак", new ArrayList<>(List.of("Биг Мак")));
        map.put("Морс крыжовниковый", new ArrayList<>(List.of("Крыжовник")));
    }

    public Connection co;

    public DataBaseDishes() {
    }

    public void open(String url) {
        try {
            Class.forName("org.sqlite.JDBC");
            this.co = DriverManager.getConnection(
                    url);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    public void close() {
        try {
            this.co.close();
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    public ResultSet getMenu() throws SQLException {
        String query = "SELECT name_dish, price_dish\n" +
                "FROM AllDishes\n" +
                "ORDER BY random()\n" +
                "LIMIT 7";
        var statement = co.createStatement();
        return statement.executeQuery(query);
    }


    public ResultSet getResidue() throws SQLException {
        String query = "SELECT id_residue, name_residue, count_residue FROM Residue";
        var statement = co.createStatement();
        return statement.executeQuery(query);
    }

    public void addTen() throws SQLException {
        String query = "UPDATE Residue SET count_residue = count_residue + 10";
        var statement = co.createStatement();
        statement.executeUpdate(query);
    }


    public void deleteFrom(ArrayList<String> dishes) throws SQLException {
        for (var dish : dishes) {
            for (var s : map.get(dish)) {
                System.out.println(s);
                String query = String.format("UPDATE Residue SET count_residue = count_residue - 1 WHERE name_residue = '%s'", s);
                var statement = co.createStatement();
                statement.executeUpdate(query);
            }
        }
    }
}
