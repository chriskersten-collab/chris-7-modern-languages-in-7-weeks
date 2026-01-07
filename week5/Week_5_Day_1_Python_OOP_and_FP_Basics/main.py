# main.py
from models import StudySession, Person
from fp_utils import total_study_time, filter_hours, product

def main() -> None:
    print("Exercise 1 — StudySession")
    session = StudySession("Python OOP", 3)
    print(session)

    print("\nExercise 2 — Functional Thinking")
    hours = [1, 3, 2, 4, 1]
    filtered = filter_hours(hours)
    total = sum(filtered)

    print("Filtered hours:", filtered)
    print("Total hours:", total)
    print("Original list:", hours)

    print("\nExercise 3 — OOP + FP Together")
    sessions = [
        StudySession("Python OOP", 3),
        StudySession("Functional Programming", 2),
        StudySession("Data Structures", 4),
    ]

    for s in sessions:
        print(s)

    print("Total study time:", total_study_time(sessions))

    print("\nGo Further — Classmethod Constructor")
    person = Person.from_birth_year("John", 1985)
    person.display()

    print("\nGo Further — reduce() example")
    numbers = [1, 2, 3, 4, 5]
    print("Product:", product(numbers))


if __name__ == "__main__":
    main()
