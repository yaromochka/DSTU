package programmingLanguages.laboratories.zeroLaboratory;


public class Owner {
    String name;
    Pet pet;

    void say() {
        System.out.println("Hello, my name is " + name
        + " and my " + pet.kind + " is " + pet.color);
    }

    static class Pet {
        String kind;
        String color;
    }
}
