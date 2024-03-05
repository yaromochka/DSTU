package programmingLanguages.laboratories.GUI.Controllers;

import javafx.collections.FXCollections;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.*;

import java.io.IOException;
import java.net.URL;
import java.util.ArrayList;
import java.util.ResourceBundle;

public class ListLab implements Initializable {
    @FXML
    private TextField textField;

    @FXML
    private TextArea textArea;

    @FXML
    private Button laboratoryThirdButton;

    @FXML
    private Button laboratoryThirdDotFirstButton;

    @FXML
    private Button laboratoryFourthButton;

    @FXML
    private Button clearButton;

    @FXML
    private Button sendButton;

    @FXML
    private static String numberOfLaboratory;

    @FXML
    private ChoiceBox<String> choiceBox;

    @FXML
    private Button backButton;

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        ArrayList<String> arr = new ArrayList<>();
        for (int i = 1; i < 30; i++) {
            arr.add(String.format("Задание №%s", i));
        }

        choiceBox.setItems(FXCollections.observableArrayList(arr));
        choiceBox.setValue("Выберите номер лабораторной");

        laboratoryThirdButton.setOnMouseClicked(event -> numberOfLaboratory = "3");
        laboratoryThirdDotFirstButton.setOnMouseClicked(event -> numberOfLaboratory = "3.1");
        laboratoryFourthButton.setOnMouseClicked(event -> numberOfLaboratory = "4");

        clearButton.setOnMouseClicked(event -> textField.clear());

        backButton.setOnMouseClicked(MouseEvent -> {
            try {
                SceneController.switchToMenu(MouseEvent);
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        });

        sendButton.setOnMouseClicked(event -> {
            var numberOfTask = choiceBox.getValue();
            var textToInput = textField.getText();
            if (numberOfTask != null && numberOfLaboratory != null && textToInput != null) {
                numberOfTask = numberOfTask.replaceAll("[^0-9]", "");
                textField.clear();
                System.out.println(numberOfTask + " " + numberOfLaboratory + " " + textToInput);
            }
            else {
                textField.clear();
                Alert alert = new Alert(Alert.AlertType.INFORMATION);
                alert.setTitle("ALARM");
                alert.setHeaderText("Произошла непредвиденная ошибка");
                alert.setContentText("Возможно вы не выбрали нужное задание");

                alert.showAndWait();
            }
        });
    }
}
