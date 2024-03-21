package programmingLanguages.laboratories.fourthLaboratory;

import org.jetbrains.annotations.NotNull;

public class Node<T extends Comparable<T>> implements Comparable<Node<T>> {
    public T data;
    public Node<T> next;
    public Node<T> previous;

    public Node(Node<T> previous, T data, Node<T> next) {
        this.data = data;
        this.next = next;
        this.previous = previous;
    }

    public Node(T data, Node<T> next) {
        this.data = data;
        this.next = next;
    }

    @Override
    public int compareTo(Node<T> o) {
        return this.data.compareTo(o.data);
    }
}