package programmingLanguages.laboratories.GUI.Controllers;

import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import programmingLanguages.laboratories.GUI.DatabaseHelp.Dish;

import java.io.IOException;
import java.net.URL;
import java.util.ResourceBundle;

public class ResidueMenu implements Initializable {

    @FXML
    private Button backButton;

    @FXML
    private TableView<Dish> residueMenu;

    @FXML
    private TableColumn<Dish, String> nameColumn;

    @FXML
    private TableColumn<Dish, Double> residueColumn;

    private ObservableList<Dish> residueData = FXCollections.observableArrayList();


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
    }
}
