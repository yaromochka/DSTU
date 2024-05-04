package programmingLanguages.laboratories.GUI.Controllers;

import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import programmingLanguages.laboratories.GUI.HelpMethods.SceneController;

import java.io.IOException;
import java.net.URL;
import java.util.ResourceBundle;

public class AdminPanel implements Initializable {

    @FXML
    private Button backButton;


    @FXML
    private Button reportButton;


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


        reportButton.setOnMouseClicked(MouseEvent -> {
            System.out.println("Hello World!");
        });

    }
}
