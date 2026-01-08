// Examples

const companies: string[] = ["OpenAI", "Google", "Amazon"];
companies.push("Microsoft");
companies.splice(companies.indexOf("Amazon"), 1);
console.log(companies);
for (const company of companies) {
  console.log("Applied to:", company);
}

const application = {
  company: "OpenAI",
  role: "Data Scientist",
  applicationsSent: 12,
  response: true,
};
console.log(application);
application.response = false;
console.log(application);

type WeekTwoJobApplication = {
  company: string;
  role: string;
  applicationsSent: number;
  response: boolean;
};
const WeekTwoApp: WeekTwoJobApplication = {
  company: "Google",
  role: "Data Scientist",
  applicationsSent: 5,
  response: false,
};

const more_skills = new Set<string>(["python", "sql", "git", "python"]);
more_skills.add("aws");
console.log("Has Python? ", more_skills.has("python"));

const responses = new Map<string, boolean>();
responses.set("Google", false);
responses.set("OpenAI", true);
console.log("Response: ", responses.get("OpenAI"));

const coordinates: readonly number[] = [40.7, -74.0];

// Exercises

/* Exercise 1 — Arrays
Create a typed array of at least 5 companies.
Add one
Remove one
Print all */
const myCompanies: string[] = ["Facebook", "Apple", "Netflix", "Tesla", "IBM"];
myCompanies.push("Intel");
myCompanies.splice(myCompanies.indexOf("Tesla"), 1);
console.log("Exercise 1:");
console.log(myCompanies);

/* Exercise 2 — Typed Object
Define a WeekTwoJobApplication type.
Create one object and print its fields. */
const myApplication: WeekTwoJobApplication = {
  company: "Apple",
  role: "Data Analyst",
  response: false,
  applicationsSent: 0
};
console.log("Exercise 2:");
console.log("Company:", myApplication.company);
console.log("Role:", myApplication.role);

/* Exercise 3 — Array of Objects
Create an array of WeekTwoJobApplication.
Loop and print:
company
response */
const applicationArray: WeekTwoJobApplication[] = [
  {
    company: "Apple",
    role: "Data Analyst",
    response: false,
    applicationsSent: 0
  },
  {
    company: "Google",
    role: "Data Scientist",
    response: true,
    applicationsSent: 0
  },
];
console.log("Exercise 3:");
for (const WeekTwoApp of applicationArray) {
  console.log("Company:", WeekTwoApp.company);
  console.log("Response:", WeekTwoApp.response);
}

/* Exercise 4 — Sets
Create a Set<string> of skills.
Add a duplicate
Show uniqueness
Check membership */
const exerciseFourSkills = new Set<string>(["python", "typescript", "react"]);
exerciseFourSkills.add("python");
console.log("Exercise 4:");
console.log("Skills:", exerciseFourSkills);
console.log("Has TypeScript?", exerciseFourSkills.has("typescript"));

/* Exercise 5 — Comparison (Written)
In 1–2 sentences, explain:
One advantage TypeScript data structures have over Python.

TypeScript provides compile-time type checking, which helps catch errors early 
in the development process, whereas Python's dynamic typing can lead to 
runtime errors that are harder to detect and debug. */

/* Go Further (Optional)
Use Map<string, WeekTwoJobApplication>
Make a readonly object
Write a typed function returning a string */
const applicationMap: Map<string, WeekTwoJobApplication> = new Map();
applicationMap.set("Apple", {
  company: "Apple",
  role: "Data Analyst",
  response: false,
  applicationsSent: 0
});
interface Point {
  readonly readOnlyExample: number;
}
function getApplicationSummary(WeekTwoApp: WeekTwoJobApplication): string {
  return `Application to ${WeekTwoApp.company}`;
}
