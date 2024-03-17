package programmingLanguages.laboratories.fourthLaboratory;


import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;

public class SingleLinkedList {
    private Node head;
    private int size;

    // Конструктор класса
    public SingleLinkedList() {
        this.head = null;
    }

    // Класс каждой вершины
    public class Node {
        public int data;
        public Node next;

        public Node(int data) {
            this.data = data;
            next = null;
        }
    }

    // Добавление элемента data в конец списка
    public void add(int data) {
        Node newNode = new Node(data);
        Node currentNode = this.head;

        if (head == null) head = newNode;
        else {
            while (currentNode.next != null) currentNode = currentNode.next;
            currentNode.next = newNode;
        }
        this.size++;
    }

    // Удаление ВСЕХ элементов со значением data
    public void remove(int data) {
        Node currentNode = this.head;
        Node previousNode = null;

        while (currentNode.next != null) {

            if (currentNode.data == data) {
                if (currentNode == head) this.head = currentNode.next;
                else previousNode.next = currentNode.next;
            }

            previousNode = currentNode;
            currentNode = currentNode.next;
            this.size--;
        }
    }

    // Определение количества элементов
    public int size() {
        return this.size;
    }

    // Добавление элемента на первое место (вместо головы)
    public void addFirst(int data) {
        Node newNode = new Node(data);

        if (head == null) this.head = newNode;
        else {
            newNode.next = this.head;
            this.head = newNode;
        }

        this.size++;
    }

    // Удаление всех элементов (списку больше не на что ссылаться)
    public void clear() {
        this.head = null;
        this.size = 0;
    }

    // Перевод списка в строку с помощью StringBuilder
    public String toString() {
        var curr = head;
        StringBuilder str = new StringBuilder();
        while (curr != null) {
            str.append(curr.data).append(" ");
            curr = curr.next;
        }
        return str.toString();
    }

    // Проверка списка на пустоту
    public boolean isEmpty() {
        return this.size == 0;
    }

    // Удаление первого элемента
    public void delFirst() {
        Node currentNode = this.head;

        this.head = currentNode.next;

        currentNode.next = null;
        this.size--;
    }

    // Удаление последнего элемента
    public void delLast() {
        Node currentNode = this.head;
        Node previousNode = null;

        // 15 12 118 19
        if (this.head != null) {
            while (currentNode.next != null) {
                previousNode = currentNode;
                currentNode = currentNode.next;
            }
            if (previousNode != null) {
                previousNode.next = null;
            }
            else this.head = null;
        }
        this.size--;
    }

    // Поиск данного значения
    public int indexOf(int data) {
        Node currentNode = this.head;

        var counter = 0;

        while (currentNode.next != null) {
            if (currentNode.data == data) return counter;
            else counter++;

            currentNode = currentNode.next;
        }

        return -1;
    }

    // Поиск наименьшего значения в списке
    public int min() {
        if (this.size != 0) {
            Node currentNode = this.head;
            Node minNode = this.head;

            while (currentNode.next != null) {
                if (currentNode.data < minNode.data) minNode.data = currentNode.data;
                currentNode = currentNode.next;
            }
            return minNode.data;
        }
        return -1;
    }

    // Поиск наибольшего значения в списке
    public int max() {
        if (this.size != 0) {
            Node currentNode = this.head;
            Node maxNode = this.head;

            while (currentNode.next != null) {
                if (currentNode.data > maxNode.data) maxNode.data = currentNode.data;
                currentNode = currentNode.next;
            }
            return maxNode.data;
        }
        return -1;
    }

    // Удаление ОДНОГО элемента списка с данным значением
    public void removeFirst(int data) {
        Node currentNode = this.head;
        Node previousNode = null;
        while (currentNode.next != null) {

            if (currentNode.data == data) {
                if (currentNode == head) this.head = currentNode.next;
                else previousNode.next = currentNode.next;
                break;
            }

            previousNode = currentNode;
            currentNode = currentNode.next;
        }
        this.size--;
    }

    // Изменение всех элементов списка с данным значением на новое.
    public void replaceAll(int oldData, int newData) {
        Node currentNode = this.head;

        while (currentNode.next != null) {
            if (currentNode.data == oldData) currentNode.data = newData;

            currentNode = currentNode.next;
        }

        this.size = 0;
    }

    // Определение, является ли список симметричным.
    public boolean isSymmetric() {

        if (this.head == null) return true; // Пустой список является симметричным

        Node currentNode = this.head;
        List<Integer> elements = new ArrayList<>();
        // Пройти по всему списку и добавить элементы в массив
        while (currentNode != null) {
            elements.add(currentNode.data);
            currentNode = currentNode.next;
        }

        // Сравнить элементы списка с элементами массива, начиная с конца
        currentNode = head;
        for (int i = elements.size() - 1; i >= 0; i--) {
            if (!(currentNode.data == elements.get(i))) {
                return false; // Несимметричный элемент
            }
            currentNode = currentNode.next;
        }

        return true; // Все элементы совпали, список симметричен
    }

    // Определение, можно ли удалить из списка каких-нибудь два
    // элемента так, чтобы новый список оказался упорядоченным.
    public boolean deleteTwoElementToOrdinary() {
        Node currentNode = this.head;
        var counter = 0;

        while (currentNode.next != null) {
            if (currentNode.data >= currentNode.next.data) {
                counter++;
            }
            currentNode = currentNode.next;
        }

        return counter <= 2;
    }

    // Определение, сколько различных значений содержится в списке.
    public int distinctCount() {
        Node currentNode = this.head;
        var distinctSet = new HashSet<Integer>();

        while (currentNode.next != null) {
            distinctSet.add(currentNode.data);

            currentNode = currentNode.next;
        }

        return distinctSet.size();
    }

    // Удаление из списка элементов, значения которых уже встречались в предыдущих элементах.
    public void removeDistinct() {
        Node currentNode = this.head;
        Node previousNode = null;
        var distinctSet = new HashSet<Integer>();

        for (var i = 0; i < this.size; i++) {
            if (distinctSet.contains(currentNode.data)) {
                previousNode.next = currentNode.next;

            }

            distinctSet.add(currentNode.data);

            previousNode = currentNode;
            currentNode = currentNode.next;
        }
    }

    // Изменение порядка элементов на обратный.
    public void reversed() {
        Node currentNode = this.head;
        Node previousNode = null;

        while (currentNode != null) {
            Node temporaryNode = currentNode.next;
            currentNode.next = previousNode;

            previousNode = currentNode;
            currentNode = temporaryNode;
        }

        this.head = previousNode;
    }

    // Сортировка элементов списка двумя способами (изменение указателей, изменение значений элементов)
    public void pointerSort() {}

    public void dataSort() {}
}
