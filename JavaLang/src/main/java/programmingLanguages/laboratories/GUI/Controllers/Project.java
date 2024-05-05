package programmingLanguages.laboratories.GUI.Controllers;

import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.*;

import java.io.IOException;
import java.net.URL;
import java.sql.SQLException;
import java.util.ResourceBundle;

import programmingLanguages.laboratories.GUI.DatabaseHelp.DataBaseUsers;
import programmingLanguages.laboratories.GUI.HelpMethods.SceneController;
import programmingLanguages.laboratories.GUI.HelpMethods.AlertMessage;

import static programmingLanguages.laboratories.GUI.HelpMethods.CipherPassword.encryptPassword;

public class Project implements Initializable {


    @FXML
    private Button backButton;


    @FXML
    private TextField loginField;


    @FXML
    private PasswordField passwordField;


    @FXML
    private Button loginButton;


    @FXML
    private Button registerButton;


    @FXML
    private Button userButton;

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        /* Кнопка "НАЗАД" */
        backButton.setOnMouseClicked(MouseEvent -> {
            try {
                SceneController.switchToMenu(MouseEvent);
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        });

        /* Кнопка "ВОЙТИ" */
        loginButton.setOnMouseClicked(MouseEvent -> {
            var login = getLogin();
            var password = getPassword();
            loginField.clear(); passwordField.clear();
            try {
                var userStatus = loginInSystem(login, encryptPassword(password));
                switch (userStatus) {
                    case (0) -> AlertMessage.getAlert();
                    case (1) -> SceneController.switchToUserPanel(MouseEvent);
                    case (2) -> SceneController.switchToWaiterPanel(MouseEvent);
                    case (3) -> SceneController.switchToAdminPanel(MouseEvent);
                }
            } catch (SQLException | IOException e) {
                throw new RuntimeException(e);
            }
        });

        userButton.setOnMouseClicked(MouseEvent -> {
            try {
                SceneController.switchToUserPanel(MouseEvent);
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        });

        /* Кнопка "ЗАРЕГИСТРИРОВАТЬСЯ" */
        registerButton.setOnMouseClicked(MouseEvent -> {
            try {
                SceneController.switchToRegister(MouseEvent);
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        });
    }

    public String getLogin() {
        return loginField.getText();
    }

    public String getPassword() {
        return passwordField.getText();
    }

    public int loginInSystem(String login, String password) throws SQLException {
        var program = new DataBaseUsers();
        program.open();
        var user_status = program.tryToLogin(login, password);
        program.close();
        return user_status;
    }
}
