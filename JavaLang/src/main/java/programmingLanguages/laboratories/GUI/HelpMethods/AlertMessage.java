package programmingLanguages.laboratories.GUI.HelpMethods;

import javafx.scene.control.Alert;

public class AlertMessage {
    public static void getAlert() {
        Alert alert = new Alert(Alert.AlertType.INFORMATION);
        alert.setTitle("ALARM");
        alert.setHeaderText("Произошла непредвиденная ошибка");
        alert.setContentText("Возможно вы ввели неверные данные");

        alert.showAndWait();
    }
}
