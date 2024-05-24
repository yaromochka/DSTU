package programmingLanguages.laboratories.GUI.Controllers;

import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.ListView;
import javafx.scene.control.MultipleSelectionModel;
import javafx.scene.control.SelectionMode;
import programmingLanguages.laboratories.GUI.DatabaseHelp.DataBaseDishes;
import programmingLanguages.laboratories.GUI.HelpMethods.SceneController;

import java.io.IOException;
import java.net.URL;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.ResourceBundle;

public class UserPanel implements Initializable {

    @FXML
    private Button backButton;

    @FXML
    private ListView<String> listView;


    @FXML
    private Button orderButton;

    private ObservableList<String> dishData = FXCollections.observableArrayList();


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

        orderButton.setOnAction(MouseEvent -> {
            ObservableList<String> selectedDishes = listView.getSelectionModel().getSelectedItems();
            var dishes = new ArrayList<String>();
            for (String dish: selectedDishes) {
                dishes.add(Arrays.asList(dish.split(",")).get(0));
            }
            try {
                deleteFromResidue(dishes);
            } catch (SQLException e) {
                throw new RuntimeException(e);
            }
        });


    }


    public void fillListView() throws SQLException {
        var program = new DataBaseDishes();
        program.open("jdbc:sqlite:src/main/resources/Project/ListOfDishes.db");
        var resultText = program.getMenu();

        while (resultText.next()) {
            dishData.add(
                    resultText.getString("name_dish") + ", " + resultText.getDouble("price_dish") + "р");
        }

        program.close();

        // заполняем таблицу данными
        listView.setItems(dishData);
    }


    public void deleteFromResidue(ArrayList<String> dishes) throws SQLException {
        var program = new DataBaseDishes();
        program.open("jdbc:sqlite:/Users/yaromochka/IdeaProjects/DSTU/JavaLang/src/main/resources/Project/ListOfDishes.db");
        program.deleteFrom(dishes);
    }
}
