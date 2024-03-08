package programmingLanguages.laboratories.GUI.LaboratoryControllers;

import javafx.fxml.FXML;

public class ChooseLaboratory {
    @FXML
    public static String getLaboratoryInfo(String laboratoryNumber, String taskNumber) {
        System.out.println(laboratoryNumber + " " + taskNumber);
        if (laboratoryNumber != null && taskNumber != null && !taskNumber.isEmpty()) {
            return JsonSimpleParser.getInstance(laboratoryNumber).get(laboratoryNumber + " лабораторная", taskNumber + " задание");
        }
        else {
            return "Выберите номер лабораторной и задание";
        }
    }

    public static String nameParseLaboratory() {
        return "0";
    }
}
