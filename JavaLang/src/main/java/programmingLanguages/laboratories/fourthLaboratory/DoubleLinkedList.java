package programmingLanguages.laboratories.fourthLaboratory;

import java.util.ArrayList;
import java.util.List;

public class DoubleLinkedList extends SingleLinkedList {

    private Node head;
    private Node tail;
    private int size;

    // Конструктор класса двусвязного списка
    public DoubleLinkedList() {
        this.head = this.tail = null;
        this.size = 0;
    }

    // Класс каждой вершины
    public class Node {
        public int data;
        public DoubleLinkedList.Node next;
        public DoubleLinkedList.Node previous;

        public Node(int data) {
            this.data = data;
            next = null;
            previous = null;
        }
    }

    @Override
    // Добавление элемента в начало списка
    public void addFirst(int data) {
        Node newNode = new Node(data);

        if (isEmpty()) this.tail = newNode;
        else head.previous = newNode;

        newNode.next = head;
        head = newNode;

        this.size++;
    }

    @Override
    // Добавление элемента в конец списка
    public void addLast(int data) {
        Node newNode = new Node(data);

        if (isEmpty()) this.head = newNode;
        else tail.next = newNode;

        newNode.previous = tail;
        tail = newNode;

        this.size++;
    }

    @Override
    // Удаление первого элемента в списке
    public void removeFirst() {
        if (this.head == null) this.tail = null;
        else this.head.next.previous = null;

        this.head = this.head.next;

        this.size--;
    }

    @Override
    // Удаление последнего элемента в списке
    public void removeLast() {
        if (this.head == null) this.tail = null;
        else this.tail.previous.next = null;

        this.tail = tail.previous;

        this.size--;
    }

    @Override
    // Удаление всех элементов списка
    public void clear() {
        this.head = this.tail = null;
        this.size = 0;
    }

    @Override
    // Удаление элемента списка с данным значением
    public void removeAt(int data) {
        Node currentNode = this.head;

        while (currentNode.next != null) {
            if (currentNode.data == data) {
                currentNode.previous = currentNode.next;
                break;
            }

            currentNode = currentNode.next;
        }

        this.size--;
    }

    @Override
    // Удаление ВСЕХ элементов списка с данным значением
    public void remove(int data) {
        Node currentNode = this.head;

        while (currentNode.next != null) {
            if (currentNode.data == data) {
                currentNode.previous = currentNode.next;
                this.size--;
            }
        }
    }

}
