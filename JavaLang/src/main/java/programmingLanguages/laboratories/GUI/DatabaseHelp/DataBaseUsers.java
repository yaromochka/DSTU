package programmingLanguages.laboratories.GUI.DatabaseHelp;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;


public class DataBaseUsers {
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
        String query = String.format("INSERT INTO Users (login_user, password_user, status_user) VALUES ('%s', '%s', 1);", login, password);
        var statement = co.createStatement();
        statement.execute(query);
    }

    public int tryToLogin(String login, String password) throws SQLException {
        String query = String.format("SELECT status_user FROM Users WHERE login_user = '%s' AND password_user = '%s'", login, password);
        var statement = co.createStatement();
        return (statement.executeQuery(query)).getInt("status_user");
    }
}

