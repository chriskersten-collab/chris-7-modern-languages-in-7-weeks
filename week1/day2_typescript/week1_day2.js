"use strict";
// week1 day 2 TypeScript lesson
// Variable declarations with types
const myname = "Chris";
const role = "Data Scientist";
const studyHours = 5;
const applicationsSent = 12;
const applications = [0, 1, 3, 7, 12];
const skills = ["python", "sql", "excel", "git", "aws"];
//demo code from the lesson
console.log(`Hi, my name is ${myname}. I'm aiming to become a ${role} and I study ${studyHours} hours per week.`);
console.log("ts-node execution started");
if (applicationsSent === 0) {
    console.log("Start applying");
}
else if (applicationsSent < 10) {
    console.log("Good momentum");
}
else {
    console.log("High volume — track quality");
}
for (let i = 1; i <= 5; i++) {
    console.log(i);
}
for (const count of applications) {
    if (count === 0) {
        console.log("Low");
    }
    else if (count < 10) {
        console.log("Medium");
    }
    else {
        console.log("High");
    }
}
skills.forEach((skill) => {
    if (skill.length > 3) {
        console.log(`${skill} is longer than 3 characters`);
    }
});
/*const skillLengths: number[] = skills.map((skill) => skill.length);
const upperSkills: string[] = skills.map((skill) => skill.toUpperCase());

console.log(skillLengths);
console.log(upperSkills); */
// my code starts here
/* Exercise 1 — Typed Variables
Create typed variables for:
Your name
Target job role
Weekly study hours
Print one sentence.
*/
console.log(`Hi, my name is ${myname}. I'm aiming to become a ${role} and I study ${studyHours} hours per week.`);
/* Exercise 2 — Conditionals
Based on applicationsSent, print:
Start applying → 0
Good momentum → 1–9
High volume → 10+
*/
if (applicationsSent === 0) {
    console.log("Start applying");
}
else if (applicationsSent < 10) {
    console.log("Good momentum");
}
else {
    console.log("High volume");
}
/* Exercise 3 — Loop Classification
Given:
const applications: number[] = [0, 1, 3, 7, 12];
Print Low / Medium / High for each.
*/
for (const count of applications) {
    if (count === 0) {
        console.log(`${count} is Low`);
    }
    else if (count < 10) {
        console.log(`${count} is Medium`);
    }
    else {
        console.log(`${count} is High`);
    }
}
/* Exercise 4 — forEach Filtering
From skills:
Print skills longer than 3 chars
Print skills starting with a vowel
*/
skills.forEach((skill) => {
    if (skill.length > 3) {
        console.log(`${skill} is longer than 3 characters`);
    }
    if ("aeiou".includes(skill[0].toLowerCase())) {
        console.log(`${skill} starts with a vowel`);
    }
});
/*Exercise 5 — map Transformations
Create:
Array of skill lengths
Array of uppercase skills
Print both.
*/
const skillLengths = skills.map((skill) => skill.length);
const upperSkills = skills.map((skill) => skill.toUpperCase());
/*
console.log(skillLengths);
console.log(upperSkills);
*/
console.log(`Array of skill lengths ${skillLengths}`);
console.log(`Array of uppercase skills ${upperSkills}`);
// Add a typed function
function myTypedFunction(name) {
    return `Hello, ${name}!`;
}
console.log(myTypedFunction("Chris"));
// Use number | string with narrowing
function processValue(value) {
    // Check the type of the value at runtime
    if (typeof value === "string") {
        // Inside this block, TypeScript knows 'value' is a string
        // You can safely use string methods like .toUpperCase()
        console.log(`String detected: ${value.toUpperCase()}`);
    }
    else {
        // In the 'else' block, TypeScript knows 'value' must be a number
        // You can safely use number methods like .toFixed()
        console.log(`Number detected: ${value.toFixed(2)}`);
    }
}
// Example usage:
processValue("hello world"); // Output: String detected: HELLO WORLD
processValue(123.456); // Output: Number detected: 123.46
/*Explain let vs const in a comment

In TypeScript, both let and const are used for variable declarations with block scope,
meaning they are only accessible within the curly braces {} where they are defined.
The key difference lies in reassignment: let allows its value to be changed,
while const does not. */ 
