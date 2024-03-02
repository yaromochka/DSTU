package programmingLanguages.laboratories.GUI.Buttons;

import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.input.MouseEvent;
import javafx.stage.Stage;
import programmingLanguages.laboratories.GUI.Controllers.SceneController;

import java.io.IOException;
import java.net.URL;
import java.util.Objects;
import java.util.ResourceBundle;

public class ButtonMove implements Initializable {
    @FXML
    private static Stage stage;
    @FXML
    private static Scene scene;
    @FXML
    private static Parent root;
    @FXML
    public static void moveTo(MouseEvent mouseEvent, String pathToFolder) throws IOException {
        Parent root = FXMLLoader.load(Objects.requireNonNull(SceneController.class.getResource(pathToFolder)));
        stage = (Stage) ((Node)mouseEvent.getSource()).getScene().getWindow();
        scene = new Scene(root);
        stage.setScene(scene);
        stage.show();
    }

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {

    }
}

