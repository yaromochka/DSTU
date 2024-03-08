package programmingLanguages.laboratories.GUI.Controllers;

import javafx.fxml.FXML;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.input.MouseEvent;
import javafx.stage.Stage;
import programmingLanguages.laboratories.GUI.Buttons.ButtonMove;

import java.io.IOException;

public class SceneController {
    @FXML
    private static Stage stage;
    @FXML
    private static Scene scene;
    @FXML
    private static Parent root;

    @FXML
    public static void switchToLaboratories(MouseEvent mouseEvent) throws IOException {
        ButtonMove.moveTo(mouseEvent, "/ListLab/ListLab.fxml");
    }

    @FXML
    public static void switchToMenu(MouseEvent mouseEvent) throws IOException {
        ButtonMove.moveTo(mouseEvent, "/Menu/MainMenu.fxml");
    }
}
