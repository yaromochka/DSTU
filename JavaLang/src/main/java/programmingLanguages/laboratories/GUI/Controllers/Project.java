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
                var user_status = loginInSystem(login, encryptPassword(password));
                switch (user_status) {
                    case (0) -> AlertMessage.getAlert();
                    case (1) -> SceneController.switchToUserPanel(MouseEvent);
                    case (2) -> SceneController.switchToWaiterPanel(MouseEvent);
                    case (3) -> SceneController.switchToMenu(MouseEvent);
                }
            } catch (SQLException | IOException e) {
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


//    @FXML
//    private Button ordererButton;

//    @FXML
//    private Button residueButton;
//
//    @FXML
//    private Button reportButton;

//    @FXML
//    private TableView<Dish> tableMenu;
//
//    @FXML
//    private TableColumn<Dish, String> nameColumn;
//
//    @FXML
//    private TableColumn<Dish, Double> priceColumn;

//    private ObservableList<Dish> dishData = FXCollections.observableArrayList();

//        /* Кнопка "ОТСТАТОК" */
//        residueButton.setOnMouseClicked(MouseEvent -> {
//            try {
//                SceneController.switchToResidueMenu(MouseEvent);
//            } catch (IOException e) {
//                throw new RuntimeException(e);
//            }
//        });

//        // Заполняем таблицу данными
//        try {
//            fillTable();
//        } catch (SQLException e) {
//            throw new RuntimeException(e);
//        }
//    }

//    @FXML
//    public void fillTable() throws SQLException {
//        var program = new DataBaseSQLite();
//        program.open("jdbc:sqlite:/Users/yaromochka/IdeaProjects/DSTU/JavaLang/src/main/resources/Project/ListOfDishes.db");
//        var resultText = program.get();
//
//        while (resultText.next()) {
//            dishData.add(new Dish(
//                    resultText.getInt("id_dish"),
//                    resultText.getString("name"),
//                    resultText.getDouble("price")
//                    ));
//        }
//
//        program.close();
//
//        // устанавливаем тип и значение которое должно хранится в колонке
//        nameColumn.setCellValueFactory(new PropertyValueFactory<Dish, String>("name"));
//        priceColumn.setCellValueFactory(new PropertyValueFactory<Dish, Double>("price"));
//
//        // заполняем таблицу данными
//        tableMenu.setItems(dishData);
//    }
//}



//        11	Сельдь слабосолёная	560,00
//        12	Стейк	990,00
//        13	Том ям	430,00
//        14	Бутерброд с колбасой	777,00