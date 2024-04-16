package programmingLanguages.laboratories.GUI.DatabaseHelp;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;


public class DataBaseUsers{
    public Connection co;

    public DataBaseUsers() {}

    public void open() {
        try {
            Class.forName("org.sqlite.JDBC");
            co = DriverManager.getConnection(
                    "jdbc:sqlite:/Users/yaromochka/IdeaProjects/DSTU/JavaLang/src/main/resources/DataBases/Users.db");
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

    public void addUserToTable(String login, String password) throws SQLException {
        String query = "INSERT INTO Users (login_user, password_user, status_user) VALUES (" + login + ", " + password + ", 1);";
        var statement = co.createStatement();
        statement.execute(query);
    }
}

