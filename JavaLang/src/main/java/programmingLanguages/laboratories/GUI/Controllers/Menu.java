package programmingLanguages.laboratories.GUI.Controllers;


import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.input.MouseEvent;

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
    }
}