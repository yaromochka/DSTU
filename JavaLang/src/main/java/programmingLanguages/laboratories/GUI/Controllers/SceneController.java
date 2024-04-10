package programmingLanguages.laboratories.GUI.Controllers;

import javafx.fxml.FXML;
import javafx.scene.input.MouseEvent;
import programmingLanguages.laboratories.GUI.Buttons.ButtonMove;

import java.io.IOException;

public class SceneController {

    @FXML
    public static void switchToLaboratories(MouseEvent mouseEvent) throws IOException {
        ButtonMove.moveTo(mouseEvent, "/ListLab/ListLab.fxml");
    }

    @FXML
    public static void switchToMenu(MouseEvent mouseEvent) throws IOException {
        ButtonMove.moveTo(mouseEvent, "/Menu/MainMenu.fxml");
    }

    @FXML
    public static void switchToProject(MouseEvent mouseEvent) throws IOException {
        ButtonMove.moveTo(mouseEvent, "/Project/Project.fxml");
    }
}
