package programmingLanguages.laboratories.GUI.Controllers;

import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;

import javafx.scene.control.TreeTableColumn;
import javafx.scene.control.cell.PropertyValueFactory;
import programmingLanguages.laboratories.GUI.DatabaseHelp.Dish;
import programmingLanguages.laboratories.GUI.HelpMethods.SceneController;
import programmingLanguages.laboratories.GUI.DatabaseHelp.DataBaseDishes;

import java.io.IOException;
import java.net.URL;
import java.sql.SQLException;
import java.util.ResourceBundle;

public class AdminPanel implements Initializable {

    @FXML
    private Button backButton;


    @FXML
    private Button reportButton;


    @FXML
    private Button productButton;


    @FXML
    private TableView<Dish> tableMenu;

    @FXML
    private TableColumn<Dish, String> nameColumn;

    @FXML
    private TableColumn<Dish, String> countColumn;

    private ObservableList<Dish> dishData = FXCollections.observableArrayList();


    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {

        try {
            fillTable();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
        /* Кнопка "НАЗАД" */
        backButton.setOnMouseClicked(MouseEvent -> {
            try {
                SceneController.switchToProject(MouseEvent);
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        });


        /* Кнопка "ОТЧЁТ" */
        reportButton.setOnMouseClicked(MouseEvent -> {
            System.out.println("Hello World!");
        });


        /* Кнопка "ЗАКАЗ" */
        productButton.setOnMouseClicked(MouseEvent -> {
            System.out.println("Hello World!");
        });
    }

    @FXML
    public void fillTable() throws SQLException {
        var program = new DataBaseDishes();
        program.open("jdbc:sqlite:/Users/yaromochka/IdeaProjects/DSTU/JavaLang/src/main/resources/Project/ListOfDishes.db");
        var resultText = program.getResidue();

        while (resultText.next()) {
            dishData.add(new Dish(
                    resultText.getInt("id_residue"),
                    resultText.getString("name_residue"),
                    resultText.getString("count_residue")
                    ));
        }

        program.close();

        // устанавливаем тип и значение которое должно хранится в колонке
        nameColumn.setCellValueFactory(
                (TableColumn.CellDataFeatures<Dish, String> param) -> param.getValue().nameProperty());
        countColumn.setCellValueFactory(
                (TableColumn.CellDataFeatures<Dish, String> param) -> param.getValue().countProperty());

        // заполняем таблицу данными
        tableMenu.setItems(dishData);
    }
}
