package programmingLanguages.laboratories.GUI.DatabaseHelp;

public class Dish {
    private int id;
    private String name;
    private Double price;

    public Dish(int id, String name, Double price) {
        this.id = id;
        this.name = name;
        this.price = price;
    }

    public Dish() {}

    public String getName() { return this.name;}
    public Double getPrice() { return this.price;}

    public void getName(String name) { this.name = name;}
    public void getPrice(Double price) { this.price = price;}
}
