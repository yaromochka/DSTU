package programmingLanguages.laboratories.GUI.Controllers;

import javafx.beans.property.SimpleStringProperty;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.*;
import programmingLanguages.laboratories.GUI.DatabaseHelp.DataBaseDishes;
import programmingLanguages.laboratories.GUI.HelpMethods.SceneController;

import java.io.IOException;
import java.net.URL;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.ResourceBundle;

public class WaiterPanel implements Initializable {

    @FXML
    private Button backButton;

    @FXML
    private Button orderButton;

    @FXML
    private ListView<String> listView;

    private final ObservableList<String> dishData = FXCollections.observableArrayList();

    @FXML
    private TreeTableView<Order> orderedTable = new TreeTableView<>();


    @FXML
    private TreeTableColumn<Order, String> orderedColumn = new TreeTableColumn<>("Заказ");


    @FXML
    private TreeTableColumn<Order, String> readyColumn = new TreeTableColumn<>("Готовность");



    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {

        MultipleSelectionModel<String> listViewSelectionModel = listView.getSelectionModel();
        listViewSelectionModel.setSelectionMode(SelectionMode.MULTIPLE);

        /* Кнопка "НАЗАД" */
        backButton.setOnMouseClicked(MouseEvent -> {
            try {
                SceneController.switchToProject(MouseEvent);
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        });

        try {
            fillListView();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }


        orderButton.setOnMouseClicked(MouseEvent -> {
            ObservableList<String> selectedDishes = listView.getSelectionModel().getSelectedItems();
            var dishes = new ArrayList<String>();
            for (String dish: selectedDishes) {
                dishes.add(Arrays.asList(dish.split(",")).get(0));
            }
            addToOrderedTable(dishes);
            System.out.println("Заказ успешно");
        });
    }


    public void fillListView() throws SQLException {
        var program = new DataBaseDishes();
        program.open("jdbc:sqlite:/Users/yaromochka/IdeaProjects/DSTU/JavaLang/src/main/resources/Project/ListOfDishes.db");
        var resultText = program.getMenu();

        while (resultText.next()) {
            dishData.add(
                    resultText.getString("name_dish") + ", " + resultText.getDouble("price_dish") + "р");
        }

        program.close();

        // заполняем таблицу данными
        listView.setItems(dishData);
    }

    public void addToOrderedTable(ArrayList<String> dishes) {
        var order = new TreeItem<Order>();
        for (String dish: dishes) {
            order.getChildren().add(new TreeItem<>(new Order(dish, "В процессе")));
        }

        // устанавливаем тип и значение которое должно храниться в колонке
        orderedColumn.setCellValueFactory(cellData -> new SimpleStringProperty(
                cellData.getValue().getValue().getOrder()
        ));
        readyColumn.setCellValueFactory(cellData -> new SimpleStringProperty(
                cellData.getValue().getValue().getReady()
        ));


        // заполняем таблицу данными
        orderedTable.setRoot(order);
    }



    static class Order {
        String order;
        String ready = "В процессе";


        public Order() {}
        public Order(String order, String ready) {
            this.order = order;
            this.ready = ready;
        }

        public String getOrder() {
            return this.order;
        }

        public String getReady() {
            return this.ready;
        }
    }
}
