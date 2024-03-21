package programmingLanguages.laboratories.fourthLaboratory;


public class DoubleLinkedList<T extends Comparable<T>> extends SingleLinkedList<T> {
      protected Node<T> tail;


    // Конструктор класса двусвязного списка
    public DoubleLinkedList() {
        this.head = this.tail = null;
        this.size = 0;
    }

    // Класс каждой вершины

    @Override
    // Добавление элемента в начало списка
    public void addFirst(T data) {
        Node<T> newNode = new Node<>(null, data, null);

        if (isEmpty()) this.tail = newNode;
        else head.previous = newNode;

        newNode.next = this.head;
        this.head = newNode;

        this.size++;
    }


    @Override
    // Добавление элемента в конец списка
    public void addLast(T data) {
        Node<T> newNode = new Node<>(null, data, null);

        if (isEmpty()) this.head = newNode;
        else this.tail.next = newNode;

        newNode.previous = this.tail;
        this.tail = newNode;

        this.size++;
    }

    @Override
    // Удаление первого элемента в списке
    public void removeFirst() {
        if (this.head == null) this.tail = null;
        else this.head.next.previous = null;

        assert this.head != null;
        this.head = this.head.next;

        this.size--;
    }

    @Override
    // Удаление последнего элемента в списке
    public void removeLast() {
        if (this.head == null) this.tail = null;
        else this.tail.previous.next = null;

        assert tail != null;
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
    public void removeAt(T data) {
        Node<T> currentNode = this.head;

        while (currentNode.next != null) {
            if (currentNode.data.equals(data)) {
                currentNode.previous = currentNode.next;
                break;
            }

            currentNode = currentNode.next;
        }

        this.size--;
    }

    @Override
    // Удаление ВСЕХ элементов списка с данным значением
    public void remove(T data) {
        Node<T> currentNode = this.head;

        while (currentNode.next != null) {
            if (currentNode.data.equals(data)) {
                currentNode.previous = currentNode.next;
                this.size--;
            }
        }
    }
}
