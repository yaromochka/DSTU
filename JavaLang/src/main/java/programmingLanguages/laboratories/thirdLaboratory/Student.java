package programmingLanguages.laboratories.thirdLaboratory;

public class Student {
    private final String surname;
    private final String grade;
    private final String lesson;

    Student(String surname, String grade, String lesson) {
        this.surname = surname;
        this.grade = grade;
        this.lesson = lesson;
    }

    @Override
    public String toString() {
        return String.format("Студент %s получил %s по %s", this.surname, this.grade, this.lesson);
    }
}
