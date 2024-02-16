module com.example.javalang {
    requires javafx.controls;
    requires javafx.fxml;
    requires java.desktop;


    opens com.example.javalang to javafx.fxml;
    exports com.example.javalang;
}