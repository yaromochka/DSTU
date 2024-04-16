package programmingLanguages.laboratories.GUI.Controllers;


import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.input.MouseEvent;
import programmingLanguages.laboratories.GUI.HelpMethods.SceneController;

import java.io.IOException;

public class Menu {
    @FXML
    private Button laboratoryButton;
    @FXML
    private Button projectButton;


    @FXML
    public void initialize() {
        laboratoryButton.addEventHandler(MouseEvent.MOUSE_CLICKED, mouseEvent -> {
            try {
                SceneController.switchToLaboratories(mouseEvent);
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        });
        projectButton.addEventHandler(MouseEvent.MOUSE_CLICKED, mouseEvent -> {
            try {
                SceneController.switchToProject(mouseEvent);
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        });
    }
}