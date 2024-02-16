package programmingLanguages.laboratories.GUI;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.util.Objects;


public class Main extends Application {

    @Override
    public void start(Stage stage) throws Exception {
        Parent windowFXML = FXMLLoader.load(Objects.requireNonNull(getClass().getResource("/Menu/Menu.fxml")));
        stage.setScene(new Scene(windowFXML));
        stage.show();
    }
}
