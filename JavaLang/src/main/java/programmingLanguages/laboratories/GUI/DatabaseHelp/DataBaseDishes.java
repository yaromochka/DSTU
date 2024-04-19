package programmingLanguages.laboratories.GUI.DatabaseHelp;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;

public class DataBaseDishes {
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
}
