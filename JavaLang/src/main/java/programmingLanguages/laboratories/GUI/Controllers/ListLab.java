package programmingLanguages.laboratories.GUI.Controllers;

import javafx.collections.FXCollections;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.*;
import programmingLanguages.laboratories.GUI.LaboratoryControllers.ChooseLaboratory;

import java.io.IOException;
import java.net.URL;
import java.util.ArrayList;
import java.util.ResourceBundle;


/* Декоратор (?) FXML используется для того, чтобы предъявить
* доступ библиотеке JavaFX к переменным и методам
* Иначе она просто не видит их и не может с ними взаимодействовать */
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

    @FXML
    private TextArea textAreaAnswer;

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {

        /* Это будет удалено и переделано
        * Логика получения количества заданий будет изменена
        * Скорее всего будет подсчёт количества методов в классе лабораторных
        * Только после этого ChoiceBox будет заполняться */
        // choiceBox.setValue("Выберите номер ЛР");


        /* Костыльное получение данных о номере лабораторной
        * При помощи глобальной переменной и трёх обработчиков событий
        * (!) В планах заменить (!)
        */
        laboratoryThirdButton.setOnMouseClicked(event -> {
            numberOfLaboratory = "3";
            choiceBoxFill(19);
            laboratoryThirdButton.setStyle("-fx-background-color: black; -fx-text-fill: white");
            laboratoryThirdDotFirstButton.setStyle("-fx-background-color: #b2acb5; -fx-text-fill: black");
            laboratoryFourthButton.setStyle("-fx-background-color: #b2acb5; -fx-text-fill: black");
            if (choiceBox != null) {
                var text = ChooseLaboratory.getLaboratoryInfo(numberOfLaboratory, choiceBox.getValue().replaceAll("[^0-9]", ""));
                textArea.setText(text);
            }
        });

        laboratoryThirdDotFirstButton.setOnMouseClicked(event -> {
            numberOfLaboratory = "3.1";
            laboratoryThirdDotFirstButton.setStyle("-fx-background-color: black; -fx-text-fill: white");
            laboratoryThirdButton.setStyle("-fx-background-color: #b2acb5; -fx-text-fill: black");
            laboratoryFourthButton.setStyle("-fx-background-color: #b2acb5; -fx-text-fill: black");
            choiceBoxFill(14);
            if (choiceBox != null) {
                var text = ChooseLaboratory.getLaboratoryInfo(numberOfLaboratory, choiceBox.getValue().replaceAll("[^0-9]", ""));
                textArea.setText(text);
            }
        });
        laboratoryFourthButton.setOnMouseClicked(event -> {
            numberOfLaboratory = "4";
            laboratoryFourthButton.setStyle("-fx-background-color: black; -fx-text-fill: white");
            laboratoryThirdButton.setStyle("-fx-background-color: #b2acb5; -fx-text-fill: black");
            laboratoryThirdDotFirstButton.setStyle("-fx-background-color: #b2acb5; -fx-text-fill: black");
            choiceBoxFill(40);
            if (choiceBox != null) {
                var text = ChooseLaboratory.getLaboratoryInfo(numberOfLaboratory, choiceBox.getValue().replaceAll("[^0-9]", ""));
                textArea.setText(text);
            }
        });

        if (choiceBox != null) {
            choiceBox.setOnAction(event -> {
                var text = ChooseLaboratory.getLaboratoryInfo(numberOfLaboratory, choiceBox.getValue().replaceAll("[^0-9]", ""));
                textArea.setText(text);
            });
        }

        clearButton.setOnMouseClicked(event -> textField.clear());


        /* Кнопка "НАЗАД" */
        backButton.setOnMouseClicked(MouseEvent -> {
            try {
                SceneController.switchToMenu(MouseEvent);
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        });

        /* Очень большая функция, обрабатывающая кнопку "ОТПРАВИТЬ"
        * По сути именно эта кнопка является основной в этом окне
        * Именно она будет обрабатывать и запускать все лабораторные */
        sendButton.setOnMouseClicked(event -> {
            /* Получение номера лабораторной и задания */
            var numberOfTask = choiceBox.getValue();
            var textToInput = textField.getText();
            if (numberOfTask != null && numberOfLaboratory != null && textToInput != null) {
                numberOfTask = numberOfTask.replaceAll("[^0-9]", "");
                textField.clear();
                textAreaAnswer.clear();
                textAreaAnswer.setText(ChooseLaboratory.getLaboratoryAnswer(numberOfLaboratory, numberOfTask, textToInput));
                /* Здесь должна быть сама реализация запуска лабораторной
                * В планах:
                * Полученные данные обрабатываются отдельным классом ChooseLaboratory,
                * который в свою очередь запускает соответствующее задание и возвращает результат.
                * После всех взаимодействий этот результат записывается в переменную и выводится
                * В отдельном TextArea */
            }

            /* Вызов окна ошибки при неверно введённых или невведённых данных*/
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

    @FXML
    public void choiceBoxFill(int countOfTask) {
        ArrayList<String> arr = new ArrayList<>();
        for (int i = 1; i < countOfTask; i++) {
            arr.add(String.format("Задание №%s", i));
        }

        choiceBox.setItems(FXCollections.observableArrayList(arr));
        choiceBox.setValue("Выберите номер ЛР");
    }
}
