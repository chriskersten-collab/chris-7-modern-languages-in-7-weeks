/* Exercises (Submit All)
Create a file:
📄 week3_day2.ts (done!)

Exercise 1 — Write a File (Sync)
Write study_log.txt containing:
Your name
Today’s date
Hours studied today */
import * as fs from 'fs';
import { writeFile, readFile } from "fs/promises";

fs.writeFileSync("study_log.txt", "Your name: Chris\n" +
"Today's date: " + new Date().toLocaleDateString() + "\n" +
"Hours studied today: 4 hours");

console.log("\nExercise 2 — Read the File (Sync)")
/* Read and print study_log.txt.*/
const contents = fs.readFileSync("study_log.txt", "utf-8");
console.log(contents);

// console.log("\nExercise 3 — Async File Read");
/* Read study_log.txt asynchronously and print it. */
fs.readFile("study_log.txt", "utf-8", (err, data) => { // reading asynchronously
    if (err) {
        console.error("Error reading file:", err);
        return;
    }
    console.log("\nExercise 3 — Async File Read");
    console.log(data);
}); 

// console.log("\nExercise 4 — JSON");
/* Create a job application object
Write it to application.json
Read it back
Print the company name */

// Create a job application object, write it to application.json
async function saveApplication() {
    const application = {
        company: "Tech Corp",
        applicationsSent: 12,
        response: true,
    };
    await writeFile("application.json", JSON.stringify(application, null, 2),"utf-8");
}
saveApplication();

// read it back, print the company name
async function readApplication() {
    const raw = await readFile("application.json", "utf-8");
    console.log("Raw JSON string:", raw);
    if (!raw.trim()) {
        console.log("JSON file is empty");
        return;
    }
    const data = JSON.parse(raw);
    console.log("\nExercise 4 — JSON, print the company name:");
    console.log(data.company);
}
readApplication();

/* Exercise 5 — Comparison (Written)
In 1–2 sentences, explain:
How does async file I/O in Node differ from Python’s file handling model?
In Node.js, async file I/O is handled through callbacks or promises, while in Python, it's typically done with 
synchronous operations or using async/await syntax with asyncio. */

/* Go Further (Optional, Strong Signal)
Try one:
Handle a missing file with try/catch
Use path.join
Use top-level await
Compare sync vs async in a comment */
const extraCreditFilePath = 'fileThatDoesNotExist.txt';
try {
  const data = fs.readFileSync(extraCreditFilePath, 'utf-8');
  console.log('File content:', data);
} catch (error) {
  // The caught error is of type 'unknown' in strict TypeScript configurations
  if (error instanceof Error) {
    // Narrowing the type to access standard Error properties
    console.error('Error reading file:', error.message);

    // Specific error check for "file not found" (ENOENT)
    if ('code' in error && error.code === 'ENOENT') {
      console.error(`The file was not found at path: ${extraCreditFilePath}`);
    }
  } else {
    console.error('An unknown error occurred:', error);
  }
}
// Sync vs Async comparison:
// Synchronous file I/O blocks the execution of subsequent code until the operation completes, 
// which can lead to performance bottlenecks in I/O-bound applications. 
// Asynchronous file I/O, on the other hand, allows other operations to continue executing 
// while waiting for the file operation to complete, improving overall application responsiveness.