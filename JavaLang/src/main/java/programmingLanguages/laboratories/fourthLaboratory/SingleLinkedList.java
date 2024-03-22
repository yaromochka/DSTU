package programmingLanguages.laboratories.fourthLaboratory;


import java.util.*;

public class SingleLinkedList<T extends Comparable<T>>  {
    protected Node<T> head;
    protected int size;

    // Конструктор класса
    public SingleLinkedList() {
        this.head = null;
        this.size = 0;
    }

    // Добавление элемента data в конец списка
    @SuppressWarnings("unused")
    public void addLast(T data) {
        Node<T> newNode = new Node<>(data, null);
        Node<T> currentNode = this.head;

        if (head == null) this.head = newNode;
        else {
            while (currentNode.next != null) currentNode = currentNode.next;
            currentNode.next = newNode;
        }
        this.size++;
    }

    // Удаление ВСЕХ элементов со значением data
    @SuppressWarnings("unused")
    public void remove(T data) {
        Node<T> currentNode = this.head;
        Node<T> previousNode = null;

        while (currentNode.next != null) {

            if (currentNode.data.equals(data)) {
                if (currentNode == head) this.head = currentNode.next;
                else previousNode.next = currentNode.next;
            }

            previousNode = currentNode;
            currentNode = currentNode.next;
            this.size--;
        }
    }

    // Определение количества элементов
    @SuppressWarnings("unused")
    public int size() {
        return this.size;
    }

    // Добавление элемента на первое место (вместо головы)
    @SuppressWarnings("unused")
    public void addFirst(T data) {
        Node<T> newNode = new Node<>(data, null);

        newNode.next = this.head;
        this.head = newNode;

        this.size++;
    }

    // Удаление всех элементов (списку больше не на что ссылаться)
    @SuppressWarnings("unused")
    public void clear() {
        this.head = null;
        this.size = 0;
    }

    // Перевод списка в строку с помощью StringBuilder
    @SuppressWarnings("unused")
    @Override
    public String toString() {
        Node<T> currentNode = this.head;

        var str = new StringBuilder();
        for (var i = 0; i < this.size; i++) {
            str.append(currentNode.data).append(" ");

            currentNode = currentNode.next;
        }

        return str.toString();
    }

    // Проверка списка на пустоту
    @SuppressWarnings("unused")
    public boolean isEmpty() {
        return this.size == 0;
    }

    // Удаление первого элемента
    @SuppressWarnings("unused")
    public void removeFirst() {
        Node<T> currentNode = this.head;

        this.head = currentNode.next;

        currentNode.next = null;
        this.size--;
    }

    // Удаление последнего элемента
    @SuppressWarnings("unused")
    public void removeLast() {
        Node<T> currentNode = this.head;
        Node<T> previousNode = null;

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
    @SuppressWarnings("unused")
    public int indexOf(T data) {
        Node<T> currentNode = this.head;

        var counter = 0;

        while (currentNode.next != null) {
            if (currentNode.data.equals(data)) return counter;
            else counter++;

            currentNode = currentNode.next;
        }

        return -1;
    }

    // Поиск наименьшего значения в списке
    @SuppressWarnings("unused")
    public T min() {
        Node<T> currentNode = this.head;
        Node<T> minNode = this.head;

        if (this.size != 0) {

            while (currentNode.next != null) {
                if (currentNode.compareTo(minNode) < 0) minNode.data = currentNode.data;
                currentNode = currentNode.next;
            }
        }
        return minNode.data;
    }

    // Поиск наибольшего значения в списке
    @SuppressWarnings("unused")
    public T max() {
        Node<T> currentNode = this.head;
        Node<T> maxNode = this.head;

        if (this.size != 0) {

            while (currentNode.next != null) {
                if (currentNode.compareTo(maxNode) < 0) maxNode.data = currentNode.data;
                currentNode = currentNode.next;
            }
        }
        return maxNode.data;
    }

    // Удаление ОДНОГО элемента списка с данным значением
    @SuppressWarnings("unused")
    public void removeAt(T data) {
        Node<T> currentNode = this.head;
        Node<T> previousNode = null;
        while (currentNode.next != null) {

            if (currentNode.data.equals(data)) {
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
    @SuppressWarnings("unused")
    public void replaceAll(T oldData, T newData) {
        Node<T> currentNode = this.head;

        while (currentNode.next != null) {
            if (currentNode.data.equals(oldData)) currentNode.data = newData;

            currentNode = currentNode.next;
        }

    }

    // Определение, является ли список симметричным.
    @SuppressWarnings("unused")
    public boolean isSymmetric() {

        if (this.head == null) return true; // Пустой список является симметричным

        Node<T> currentNode = this.head;
        var elements = new ArrayList<>();
        // Пройти по всему списку и добавить элементы в массив
        while (currentNode != null) {
            elements.add(currentNode.data);
            currentNode = currentNode.next;
        }

        // Сравнить элементы списка с элементами массива, начиная с конца
        currentNode = this.head;
        for (int i = elements.size() - 1; i >= 0; i--) {
            if (!(currentNode.data.equals(elements.get(i)))) {
                return false; // Несимметричный элемент
            }
            currentNode = currentNode.next;
        }

        return true; // Все элементы совпали, список симметричен
    }

    // Определение, можно ли удалить из списка каких-нибудь два
    // элемента так, чтобы новый список оказался упорядоченным.
    @SuppressWarnings("unused")
    public boolean deleteTwoElementToOrdinary() {
        Node<T> currentNode = this.head;
        var counter = 0;

        while (currentNode.next != null) {
            if (currentNode.data.compareTo(currentNode.next.data) > 0) {
                counter++;
            }
            currentNode = currentNode.next;
        }

        return counter <= 2;
    }

    // Определение, сколько различных значений содержится в списке.
    @SuppressWarnings("unused")
    public int distinctCount() {
        Node<T> currentNode = this.head;
        var distinctSet = new HashSet<>();

        while (currentNode.next != null) {
            distinctSet.add(currentNode.data);

            currentNode = currentNode.next;
        }

        return distinctSet.size();
    }

    // Удаление из списка элементов, значения которых уже встречались в предыдущих элементах.
    @SuppressWarnings("unused")
    public void removeDistinct() {
        Node<T> currentNode = this.head;
        Node<T> previousNode = null;
        var distinctSet = new HashSet<>();

        for (var i = 0; i < this.size; i++) {
            if (distinctSet.contains(currentNode.data)) {
                previousNode.next = currentNode.next;
                this.size--;
            }

            distinctSet.add(currentNode.data);

            previousNode = currentNode;
            currentNode = currentNode.next;
        }
    }

    // Изменение порядка элементов на обратный.
    @SuppressWarnings("unused")
    public void reversed() {
        Node<T> currentNode = this.head;
        Node<T> previousNode = null;

        while (currentNode != null) {
            Node<T> temporaryNode = currentNode.next;
            currentNode.next = previousNode;

            previousNode = currentNode;
            currentNode = temporaryNode;
        }

        this.head = previousNode;
    }

    // Сортировка элементов списка двумя способами (изменение указателей, изменение значений элементов)
    @SuppressWarnings("unused")
    public void pointerSort() {
        Node<T> dummyNode = new Node<>(null, null);
        Node<T> currentNode = this.head;

        while (currentNode != null) {
            Node<T> insertCurrentPos = dummyNode.next;
            Node<T> insertPrePos = null;

            while (insertCurrentPos != null) {
                if (insertCurrentPos.data.compareTo(currentNode.data) > 0) {
                    break;
                }

                insertPrePos = insertCurrentPos;
                insertCurrentPos = insertCurrentPos.next;
            }

            if (insertPrePos == null) {
                insertPrePos = dummyNode;
            }

            Node<T> tempNode = currentNode.next;

            currentNode.next = insertPrePos.next;
            insertPrePos.next = currentNode;

            currentNode = tempNode;
        }

        this.head = dummyNode.next;
    }

    @SuppressWarnings("unused")
    public void dataSort() {
        boolean swapped;
        Node<T> currentNode;

        if (head == null) {
            return;
        }

        do {
            swapped = false;
            currentNode = this.head;

            while (currentNode.next != null) {

                if (currentNode.data.compareTo(currentNode.next.data) > 0) {
                    swap(currentNode, currentNode.next);
                    swapped = true;
                }

                currentNode = currentNode.next;

            }

        } while (swapped);
    }

    private void swap(Node<T> ptr1, Node<T> ptr2) {
        T temporary = ptr2.data;
        ptr2.data = ptr1.data;
        ptr1.data = temporary;
    }
}
