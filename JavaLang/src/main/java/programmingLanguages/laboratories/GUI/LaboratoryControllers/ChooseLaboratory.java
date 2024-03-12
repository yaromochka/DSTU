package programmingLanguages.laboratories.GUI.LaboratoryControllers;

import javafx.fxml.FXML;
import programmingLanguages.laboratories.thirdLaboratory.HelpClassThird;
import programmingLanguages.laboratories.thirdDotFirstLaboratory.HelpClassThirdDotFirst;
import programmingLanguages.laboratories.fourthLaboratory.HelpClassFourth;

public class ChooseLaboratory {
    @FXML
    public static String getLaboratoryInfo(String laboratoryNumber, String taskNumber) {
        if (laboratoryNumber != null && taskNumber != null && !taskNumber.isEmpty()) {
            return JsonSimpleParser.getInstance(laboratoryNumber).get(laboratoryNumber + " лабораторная", taskNumber + " задание");
        }
        else {
            return "Выберите номер лабораторной и задание";
        }
    }

    @FXML
    public static String getLaboratoryAnswer(String numberOfLaboratory, String numberOfTask, String arg) {
        switch (numberOfLaboratory) {
            case ("3") -> {
                return HelpClassThird.pointOfStart(Integer.parseInt(numberOfTask), arg);
            }
            case ("3.1") -> {
                return HelpClassThirdDotFirst.pointOfStart(Integer.parseInt(numberOfTask), arg);
            }
            case ("4") -> {
                return HelpClassFourth.pointOfStart(Integer.parseInt(numberOfTask), arg);
            }
        }
        return "Что-то пошло не так";
    }

    public static String countParseLaboratory() {
        return "0";
    }
}
