module com.example.dstu {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.dstu to javafx.fxml;
    exports com.example.dstu;
}