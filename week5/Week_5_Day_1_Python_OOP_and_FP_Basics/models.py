# models.py
from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class StudySession:
    topic: str
    hours: int

    def summary(self) -> str:
        return f"Studied {self.topic} for {self.hours} hours"

    def __str__(self) -> str:
        return self.summary()


@dataclass
class Person:
    name: str
    age: int

    @classmethod
    def from_birth_year(cls, name: str, birth_year: int) -> "Person":
        current_year = date.today().year
        return cls(name, current_year - birth_year)

    def display(self) -> None:
        print(f"{self.name}'s age is: {self.age}")
