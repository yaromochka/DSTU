package programmingLanguages.laboratories.GUI.Controllers;


import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.input.MouseEvent;
import programmingLanguages.laboratories.GUI.DatabaseHelp.DataBaseDishes;
import programmingLanguages.laboratories.GUI.HelpMethods.SceneController;

import java.io.IOException;
import java.sql.SQLException;

public class Menu {
    @FXML
    private Button laboratoryButton;
    @FXML
    private Button projectButton;


    @FXML
    public void initialize() {
        var program = new DataBaseDishes();
        program.open("jdbc:sqlite:/Users/yaromochka/IdeaProjects/DSTU/JavaLang/src/main/resources/Project/ListOfDishes.db");
        try {
            program.createTemporaryTable();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }


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