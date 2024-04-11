package programmingLanguages.laboratories.GUI.Controllers;

import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.cell.PropertyValueFactory;
import programmingLanguages.laboratories.GUI.DatabaseHelp.DataBaseSQLite;

import java.io.IOException;
import java.net.URL;
import java.sql.SQLException;
import java.util.ResourceBundle;

public class Project implements Initializable {
    @FXML
    private Button backButton;

    @FXML
    private Button ordererButton;

    @FXML
    private Button residueButton;

    @FXML
    private Button reportButton;

    @FXML
    private TableView<Dish> tableMenu;

    @FXML
    private TableColumn<Dish, String> nameColumn;

    @FXML
    private TableColumn<Dish, Double> priceColumn;

    private ObservableList<Dish> dishData = FXCollections.observableArrayList();


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

        // заполняем таблицу данными
        try {
            fillTable();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }

    @FXML
    public void fillTable() throws SQLException {
        var program = new DataBaseSQLite();
        program.open();
        var resultText = program.get();

        while (resultText.next()) {
            dishData.add(new Dish(
                    resultText.getInt("id_dish"),
                    resultText.getString("name"),
                    resultText.getDouble("price")
                    ));
        }

        program.close();

        // устанавливаем тип и значение которое должно хранится в колонке
        nameColumn.setCellValueFactory(new PropertyValueFactory<Dish, String>("name"));
        priceColumn.setCellValueFactory(new PropertyValueFactory<Dish, Double>("price"));

        // заполняем таблицу данными
        tableMenu.setItems(dishData);
    }
}
