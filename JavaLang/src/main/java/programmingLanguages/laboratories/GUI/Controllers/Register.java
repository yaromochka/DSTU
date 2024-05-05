package programmingLanguages.laboratories.GUI.Controllers;

import java.sql.SQLException;

import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import programmingLanguages.laboratories.GUI.DatabaseHelp.DataBaseUsers;
import programmingLanguages.laboratories.GUI.HelpMethods.AlertMessage;
import programmingLanguages.laboratories.GUI.HelpMethods.SceneController;

import java.io.IOException;
import java.net.URL;
import java.util.ResourceBundle;
import java.util.regex.Pattern;

import static programmingLanguages.laboratories.GUI.HelpMethods.CipherPassword.encryptPassword;

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
                try {
                    addNewUser(login, encryptPassword(password));
                    SceneController.switchToProject(MouseEvent);
                } catch (SQLException | IOException e) {
                    throw new RuntimeException(e);
                }
            } else {
                AlertMessage.getAlert();
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

