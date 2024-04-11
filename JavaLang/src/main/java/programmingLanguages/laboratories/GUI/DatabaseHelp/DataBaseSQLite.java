package programmingLanguages.laboratories.GUI.DatabaseHelp;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;

public class DataBaseSQLite {
    public Connection co;

    public DataBaseSQLite() {
    }

    public void open() {
        try {
            Class.forName("org.sqlite.JDBC");
            this.co = DriverManager.getConnection(
                    "jdbc:sqlite:/Users/yaromochka/IdeaProjects/DSTU/JavaLang/src/main/resources/Project/ListOfDishes.db");
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

    public ResultSet get() throws SQLException {
        String query = "SELECT * FROM AllDishes";
        var statement = co.createStatement();
        return statement.executeQuery(query);
    }
}
