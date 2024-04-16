package programmingLanguages.laboratories.GUI.Controllers;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.sql.SQLException;
import java.util.Base64;

import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import programmingLanguages.laboratories.GUI.DatabaseHelp.DataBaseUsers;

import java.io.IOException;
import java.net.URL;
import java.util.ResourceBundle;
import java.util.regex.Pattern;

public class Register implements Initializable {

    @FXML
    private Button backButton;


    @FXML
    private TextField loginField;


    @FXML
    private TextField passwordField;


    @FXML
    private TextField repeatPasswordField;


    @FXML
    private Button doneButton;


    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        /* Кнопка "НАЗАД" */
        backButton.setOnMouseClicked(MouseEvent -> {
            try {
                SceneController.switchToProject(MouseEvent);
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        });

        /* Кнопка "РЕГИСТРАЦИЯ" */
        doneButton.setOnMouseClicked(MouseEvent -> {
            var login = getLogin();
            var password = getPassword();
            var repeatPassword = getRepeatPassword();
            loginField.clear(); passwordField.clear(); repeatPasswordField.clear();
            if (password.equals(repeatPassword) &&
                    Pattern.matches("^(?=.*[A-Z])(?=.*[a-z])(?=.*\\d)[A-Za-z0-9_]{8,}$", password)) {

                // Создаем объект MessageDigest с использованием алгоритма SHA-256
                MessageDigest md;
                try {
                    md = MessageDigest.getInstance("SHA-256");
                } catch (NoSuchAlgorithmException e) {
                    throw new RuntimeException(e);
                }

                // Преобразуем пароль в байтовый массив и вычисляем хэш-значение
                byte[] hash = md.digest(password.getBytes());

                // Кодируем хэш-значение в Base64 и выводим на экран
                String encodedHash = Base64.getEncoder().encodeToString(hash);
                try {
                    addNewUser(login, encodedHash);
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
        });
    }

    public String getLogin() {
        return loginField.getText();
    }

    public String getPassword() {
        return passwordField.getText();
    }

    public String getRepeatPassword() {
        return repeatPasswordField.getText();
    }

    public void addNewUser(String login, String password) throws SQLException {
        var program = new DataBaseUsers();
        program.open();
        program.addUserToTable(login, password);
        program.close();
    }
}

