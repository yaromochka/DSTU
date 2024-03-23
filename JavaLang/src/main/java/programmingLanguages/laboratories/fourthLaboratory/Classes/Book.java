package programmingLanguages.laboratories.fourthLaboratory.Classes;

import org.jetbrains.annotations.NotNull;

import java.util.Comparator;

public class Book implements Comparator<Book>, Comparable<Book> {

    protected final String title;
    protected final String author;
    protected final Integer year;

    public Book(String title, String author, int year) {
        this.title = title;
        this.author = author;
        this.year = year;
    }
    public String toString() {
        return String.format("(%s, %s, %d)", this.title, this.author, this.year);
    }
    @Override
    public int compareTo(@NotNull Book o) {
        return this.compare(this, o);
    }

    @Override
    public int compare(Book o1, Book o2) {
        int nameComparison = o1.title.compareTo(o2.title);
        if (nameComparison !=  0) {
            return nameComparison;
        }

        int authorComparison = o1.author.compareTo(o2.author);
        if (authorComparison !=  0) {
            return authorComparison;
        }

        return o1.year.compareTo(o2.year);
    }
}
