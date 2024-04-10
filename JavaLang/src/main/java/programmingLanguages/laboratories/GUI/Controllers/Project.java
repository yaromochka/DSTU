package programmingLanguages.laboratories.GUI.Controllers;

import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.TableView;

import java.io.IOException;
import java.net.URL;
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
    private TableView tableMenu;

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
    }
}
