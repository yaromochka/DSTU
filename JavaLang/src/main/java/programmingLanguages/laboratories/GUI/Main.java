package programmingLanguages.laboratories.GUI;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
// import javafx.scene.paint.Color;
import javafx.stage.Stage;
// import javafx.stage.StageStyle;

import java.util.Objects;


public class Main extends Application {

    @Override
    public void start(Stage stage) throws Exception {
        Parent windowFXML = FXMLLoader.load(Objects.requireNonNull(getClass().getResource("/Menu/MainMenu.fxml")));
        var scene = new Scene(windowFXML);
/*
        stage.setResizable(false);
        stage.initStyle(StageStyle.TRANSPARENT);
        scene.setFill(Color.TRANSPARENT);

 */
        stage.setScene(scene);
        stage.show();
    }
}
