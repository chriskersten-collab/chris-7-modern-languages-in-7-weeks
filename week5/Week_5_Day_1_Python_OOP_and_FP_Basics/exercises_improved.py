from dataclasses import dataclass
from datetime import date
from functools import reduce
from typing import Iterable
from operator import mul

''' Exercise 1 — Your First Class
Task:

Create a class StudySession with:
topic: str
hours: int

Methods:
summary() → "Studied <topic> for <hours> hours" '''
@dataclass(frozen=True)
class StudySession:
    topic: str
    hours: int
    def summary(self) -> str:
        return f"Studied {self.topic} for {self.hours} hours"


'''      Go Further (Optional — Strong Signal)    Add a @classmethod constructor
'''
@dataclass
class Person:
    name: str
    age: int

    @classmethod
    def from_birth_year(cls, name: str, birth_year: int) -> "Person":
        """A class method to create a Person object from a birth year."""
        current_year = date.today().year
        age = current_year - birth_year
        return cls(name, age) # This is equivalent to calling Person(name, age)

    def display(self):
        print(f"{self.name}'s age is: {self.age}")

def total_study_time(sessions: Iterable[StudySession]) -> int:
    ''' Example 6 — FP Operating on Objects '''
    return sum(session.hours for session in sessions)

def add(x, y):
    return x + y

if __name__ == "__main__":

    print('Test the StudySession class')
    session = StudySession("Python OOP", 3)
    print(session.summary())

    print('''
Exercise 2 — Functional Thinking
    Given: hours = [1, 3, 2, 4, 1]
    
    Create a new list with hours ≥ 2
    Compute the total hours
    Do NOT modify the original list ''')
    hours = [1, 3, 2, 4, 1]
    filtered_hours = [h for h in hours if h >= 2]
    total_hours = sum(filtered_hours)
    print("Filtered hours (>=2):", filtered_hours)
    print("Total hours:", total_hours)
    print("Original hours list:", hours)

    print('''
Exercise 3 — OOP + FP Together
    1. Create 3 StudySession objects
    2. Store them in a list
    3. Write a function that returns total hours
    4. Print summaries + total ''')
    sessions = [
        StudySession("Python OOP", 3),
        StudySession("Functional Programming", 2),
        StudySession("Data Structures", 4)
    ]
    total = total_study_time(sessions)
    for session in sessions:
        print(session.summary())
    print("Total study time:", total)

    ''' Concept Check (Write as Comments)
    Answer in 1-2 sentences each:

    When is OOP preferable in Python? OOP is preferable when modeling complex entities with state and behavior, 
    allowing for encapsulation and code organization.

    When is FP preferable? FP is preferable for operations on data collections, 
    promoting immutability and easier reasoning about code.

    Why does Python encourage mixing both? Python encourages mixing both to leverage the strengths of each paradigm, 
    enabling developers to choose the best approach for different parts of their code.
    
    Go Further (Optional — Strong Signal)
    Try one:
    Make StudySession immutable (@dataclass(frozen=True))
    Add a @classmethod constructor
    Use functools.reduce

    Compare Python OOP to Go structs (comment) 
    Go structs can have methods, but Go lacks classes, inheritance, and method overriding.
    Composition is favored over inheritance, whereas Python supports full OOP.

     
      from dataclasses import dataclass
      @dataclass(frozen=True)
'''

    print('''
Go Further (Optional — Strong Signal)    Add a @classmethod constructor''')
    print('Using the regular constructor (instance method)')
    person1 = Person('Adam', 25)
    person1.display()

    print('Using the class method (factory method)')
    person2 = Person.from_birth_year('John', 1985)
    person2.display()

    print('Class methods can also be called on an instance, but still receive the class')
    person3 = person2.from_birth_year('Jane', 1990)
    person3.display()


    print('''
Go Further (Optional — Strong Signal)    Use functools.reduce  ''')
    numbers = [1, 2, 3, 4, 5]
    total_sum = reduce(add, numbers)
    print("Total sum using reduce:", total_sum)
    product = reduce(mul, numbers)
    print("Product using reduce:", product)