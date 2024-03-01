package programmingLanguages.laboratories.GUI.Controllers;

import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.*;

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
    private ChoiceBox<String> choiceBox;

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        ArrayList<String> arr = new ArrayList<>();
        for (int i = 1; i < 30; i++) {
            arr.add(String.format("Задание №%s", i));
        }

        choiceBox.setItems(FXCollections.observableArrayList(arr));
        choiceBox.setValue("");
    }
/*
    @FXML
    public void addInputToComboBox(ActionEvent event) {
        comboBox.getItems().add(textField.getText());
        textField.clear();
    }

    @FXML
    public void getComboBoxInfo(ActionEvent event) {
        System.out.println(comboBox.getValue());
    }
 */
}
