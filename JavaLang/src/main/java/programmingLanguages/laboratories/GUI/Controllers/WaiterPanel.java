package programmingLanguages.laboratories.GUI.Controllers;

import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.*;
import programmingLanguages.laboratories.GUI.DatabaseHelp.DataBaseDishes;
import programmingLanguages.laboratories.GUI.HelpMethods.SceneController;

import java.io.IOException;
import java.net.URL;
import java.sql.SQLException;
import java.util.ResourceBundle;

public class WaiterPanel implements Initializable {

    @FXML
    private Button backButton;

    @FXML
    private Button orderButton;

    @FXML
    private ListView<String> listView;

    private final ObservableList<String> dishData = FXCollections.observableArrayList();

    @FXML
    private TreeTableView<TreeItem<String>> orderedTable;


    @FXML
    private TreeTableColumn<String, String> orderedColumn;


    @FXML
    private TreeTableColumn<String, String> readyColumn;


    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {

        MultipleSelectionModel<String> listViewSelectionModel = listView.getSelectionModel();
        listViewSelectionModel.setSelectionMode(SelectionMode.MULTIPLE);

        /* Кнопка "НАЗАД" */
        backButton.setOnMouseClicked(MouseEvent -> {
            try {
                SceneController.switchToProject(MouseEvent);
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        });

        try {
            fillListView();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }

        orderButton.setOnMouseClicked(MouseEvent -> {

        });
    }


    public void fillListView() throws SQLException {
        var program = new DataBaseDishes();
        program.open("jdbc:sqlite:/Users/yaromochka/IdeaProjects/DSTU/JavaLang/src/main/resources/Project/ListOfDishes.db");
        var resultText = program.getMenu();

        while (resultText.next()) {
            dishData.add(
                    resultText.getString("name_dish") + ", " + String.valueOf(resultText.getDouble("price_dish")) + "р");
        }

        program.close();

        // заполняем таблицу данными
        listView.setItems(dishData);
    }

}
