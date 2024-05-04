package programmingLanguages.laboratories.GUI.HelpMethods;

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

    @FXML
    public static void switchToRegister(MouseEvent mouseEvent) throws IOException {
        ButtonMove.moveTo(mouseEvent, "/Register/Register.fxml");
    }

    @FXML
    public static void switchToAdminPanel(MouseEvent mouseEvent) throws IOException {
        ButtonMove.moveTo(mouseEvent, "/AdminPanel/AdminPanel.fxml");
    }

    @FXML
    public static void switchToUserPanel(MouseEvent mouseEvent) throws IOException {
        ButtonMove.moveTo(mouseEvent, "/UserPanel/UserPanel.fxml");
    }

    @FXML
    public static void switchToWaiterPanel(MouseEvent mouseEvent) throws IOException {
        ButtonMove.moveTo(mouseEvent, "/WaiterPanel/WaiterPanel.fxml");
    }
}
