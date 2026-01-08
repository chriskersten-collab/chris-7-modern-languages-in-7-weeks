class WeekFiveJobApplication {
    company: string;
    applicationsSent: number;
    response: boolean;

    constructor(company: string, applicationsSent: number, response: boolean) {
        this.company = company;
        this.applicationsSent = applicationsSent;
        this.response = response;
    }

    status(): string {
        return this.response ? "Responded" : "No Response";
    }
}

class ImmutableJobApplication {
    readonly company: string;
    readonly applicationsSent: number;
    readonly response: boolean;

    constructor(company: string, applicationsSent: number, response: boolean) {
        this.company = company;
        this.applicationsSent = applicationsSent;
        this.response = response;
    }
    status(): string {
        return this.response ? "Responded" : "No Response";
    }
}

class ExercisesStudySession {
  private constructor(
    public readonly topic: string,
    public readonly hours: number
  ) {}

  static create(topic: string, hours: number): ExercisesStudySession {
    if (hours <= 0) {
      throw new Error("Hours must be positive");
    }
    return new ExercisesStudySession(topic, hours);
  }
}


console.log("\nExercise 1 — Class Definition");
const WeekFiveApp = new WeekFiveJobApplication("TechCorp", 3, true);
console.log(WeekFiveApp.status());
console.log(`Applied to ${WeekFiveApp.company}, Applications Sent: ${WeekFiveApp.applicationsSent}, Status: ${WeekFiveApp.status()}`);

console.log("\nExercise 2 — FP on Objects");
const WeekFiveApplications: WeekFiveJobApplication[] = [
    new WeekFiveJobApplication("InnovateX", 2, false),
    new WeekFiveJobApplication("DevSolutions", 5, true),
    new WeekFiveJobApplication("CodeWorks", 1, false),
];

const responded = WeekFiveApplications.filter(a => a.response);
const totalSent = WeekFiveApplications.reduce(
    (sum, a) => sum + a.applicationsSent,
    0
);
console.log("Responded:", responded.map(a => a.company));
console.log("Total Applications Sent:", totalSent);

console.log("\nExercise 3 — Immutability");
// See ImmutableJobApplication class above.
const ImmutableApp = new ImmutableJobApplication("FutureTech", 4, false);
console.log(`Applied to ${ImmutableApp.company}, Applications Sent: ${ImmutableApp.applicationsSent}, Status: ${ImmutableApp.status()}`);
// ImmutableApp.applicationsSent = 5; // This line would cause a compile-time error due to readonly properties. 

console.log("\nExercise 4 — FP Helper Function");
function totalApplications(apps: ReadonlyArray<ImmutableJobApplication>): number {
    return apps.reduce((sum, a) => sum + a.applicationsSent, 0);
}
// Why is ReadonlyArray useful?
// It prevents modification of the array, ensuring immutability and safer functional programming practices.
const ImmutableApplications: ImmutableJobApplication[] = [
    new ImmutableJobApplication("NextGen", 3, true),
    new ImmutableJobApplication("AlphaBeta", 2, false),
    new ImmutableJobApplication("GammaTech", 6, true),
];
console.log("Total Applications Sent (Immutable):", totalApplications(ImmutableApplications));

/* Exercise 5 — Comparison (Written)
In 1–2 sentences, explain:
How does TypeScript’s class + FP style compare to Python’s dataclasses + FP?
(Add as a comment.) 
TypeScript (TS) focuses on robust compile-time typing for web apps, 
using classes for state/behavior with FP libraries like fp-ts, 
while Python leans on its built-in dataclasses (often with Pydantic) for clear data structures, 
leveraging Python's gradual typing and runtime introspection for functional data transformation, 
creating a balance between type safety and dynamic flexibility. 
TS is more about enforcing types at compile time on JavaScript, 
whereas Python's types are part of the language, allowing runtime checks and rich tooling. 
*/

console.log("\nGo Further (Optional — Strong Signal)");
/* Try one:
Add a static factory method
See ExercisesStudySession class above

Use map → filter → reduce in one chain
*/ 
console.log("Use map → filter → reduce in one chain");
const chainedTotal = WeekFiveApplications
    .map(a => a.applicationsSent)
    .filter(sent => sent >= 2)
    .reduce((sum, sent) => sum + sent, 0);
console.log("Chained Total Applications Sent (>=2):", chainedTotal);
/* Compare TS classes to Go structs (comment)
TypeScript classes and Go structs both group data, 
but they represent fundamentally different programming paradigms and have distinct features. 
TypeScript uses object-oriented programming (OOP) with classes that support inheritance and are based on structural typing, 
whereas Go focuses on composition using structs and associated methods via receiver functions. */