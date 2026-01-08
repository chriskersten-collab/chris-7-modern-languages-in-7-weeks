class StudySession {
    constructor(
        public readonly topic: string,
        public readonly hours: number
    ) {}

    summary(): string {
        return `Studied ${this.topic} for ${this.hours} hours.`;
    }
}

class Person {
    private age: number;

    constructor(public name: string, age: number) {
        this.age = age;
    }

    getAge(): number {
        return this.age;
    }
}

const sessions: StudySession[] = [
    new StudySession("TypeScript Basics", 2),
    new StudySession("FP Concepts", 3),
    new StudySession("Classes in TypeScript", 1),
];

console.log("\nExample 1 — A Simple Class");
const session = new StudySession("TypeScript OOP", 3);
console.log(session.summary());

console.log("\nExample 2 — Private State + Getter");
const person = new Person("Chris", 30);
console.log(`${person.name} is ${person.getAge()} years old.`);

console.log("\nExample 3 — Functional Operations on Objects");
const longSessions = sessions.filter(s => s.hours >= 2);
const totalHours = sessions.reduce((sum, s) => sum + s.hours, 0);
console.log("Long Sessions:", longSessions.map(s => s.summary()));
console.log("Total hours:", totalHours);