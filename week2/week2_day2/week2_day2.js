"use strict";
// Examples
const companies = ["OpenAI", "Google", "Amazon"];
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
const app = {
    company: "Google",
    role: "Data Scientist",
    applicationsSent: 5,
    response: false,
};
const more_skills = new Set(["python", "sql", "git", "python"]);
more_skills.add("aws");
console.log("Has Python? ", more_skills.has("python"));
const responses = new Map();
responses.set("Google", false);
responses.set("OpenAI", true);
console.log("Response: ", responses.get("OpenAI"));
const coordinates = [40.7, -74.0];
// Exercises
/* Exercise 1 — Arrays
Create a typed array of at least 5 companies.
Add one
Remove one
Print all */
const myCompanies = ["Facebook", "Apple", "Netflix", "Tesla", "IBM"];
myCompanies.push("Intel");
myCompanies.splice(myCompanies.indexOf("Tesla"), 1);
console.log("Exercise 1:");
console.log(myCompanies);
const myApplication = {
    company: "Apple",
    role: "Data Analyst",
    response: false,
};
console.log("Exercise 2:");
console.log("Company:", myApplication.company);
console.log("Role:", myApplication.role);
/* Exercise 3 — Array of Objects
Create an array of JobApplication.
Loop and print:
company
response */
const applicationArray = [
    {
        company: "Apple",
        role: "Data Analyst",
        response: false,
    },
    {
        company: "Google",
        role: "Data Scientist",
        response: true,
    },
];
console.log("Exercise 3:");
for (const app of applicationArray) {
    console.log("Company:", app.company);
    console.log("Response:", app.response);
}
/* Exercise 4 — Sets
Create a Set<string> of skills.
Add a duplicate
Show uniqueness
Check membership */
const exerciseFourSkills = new Set(["python", "typescript", "react"]);
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
Use Map<string, JobApplication>
Make a readonly object
Write a typed function returning a string */
const applicationMap = new Map();
applicationMap.set("Apple", {
    company: "Apple",
    role: "Data Analyst",
    response: false,
});
function getApplicationSummary(app) {
    return `Application to ${app.company}`;
}
