package programmingLanguages.laboratories.thirdLaboratory;

public class Student {
    private final String surname;
    private final String grade;
    private final String lesson;

    Student(String surname, String grade, String lesson) {
        this.surname = surname.length() > 15 ? surname.substring(0, 15) : surname;
        this.grade = grade.length() > 3 ? grade.substring(0, 3) : grade;
        this.lesson = lesson.length() > 10 ? lesson.substring(0, 10) : lesson;
    }

    @Override
    public String toString() {
        return String.format("Студент %s получил %s по %s", this.surname, this.grade, this.lesson);
    }
}
