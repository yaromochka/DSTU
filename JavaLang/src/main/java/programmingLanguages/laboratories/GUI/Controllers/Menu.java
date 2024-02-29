package programmingLanguages.laboratories.GUI.Controllers;


import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.input.MouseEvent;
import programmingLanguages.laboratories.GUI.Controllers.SceneController;

public class Menu {
    @FXML
    private Button laboratoryButton;
    @FXML
    private Button projectButton;


    @FXML
    public void initialize() {
        laboratoryButton.addEventHandler(MouseEvent.MOUSE_CLICKED, new EventHandler<MouseEvent>() {
            @Override
            public void handle(MouseEvent mouseEvent) {

                System.out.println("Hello World!");
            }
        });
    }
}