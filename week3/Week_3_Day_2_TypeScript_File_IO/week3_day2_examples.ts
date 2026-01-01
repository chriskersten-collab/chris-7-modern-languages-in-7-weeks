import * as fs from 'fs';

// Example 1: read a file synchronously
const contents = fs.readFileSync("notes.txt", "utf-8");
console.log(contents);
// Example 2: write to a file synchronously
fs.writeFileSync("output.txt", "Hello from TypeScript!\n");
fs.appendFileSync("output.txt", "Appending a new line.\n");
fs.appendFileSync("another_output.txt", "This is another file.\n");

// Example 3. Async File I/O (Very Important)
fs.readFile("notes.txt", "utf-8", (err, data) => { // reading asynchronously
    if (err) {
        console.error("Error reading file:", err);
        return;
    }
    console.log(data);
}); 
//writing asynchronously
fs.writeFile("async_output.txt", "Async write\n", (err) => {
    if (err) {
        console.error("Error writing file:", err);
    }
});

// Example 4. Promise-based API (Best Modern Style)
import { readFile, writeFile } from "fs/promises";
async function run() {
    await writeFile("data.txt", "Saved using promises\n");
    const data = await readFile("data.txt", "utf-8");
    console.log(data);
}
run();

// Example 5. JSON Files (Extremely Common)
// writing JSON
// import { writeFile, readFile } from "fs/promises"; // already imported above
async function saveApplication() {
    const application = {
        company: "Tech Corp",
        applicationsSent: 12,
        response: true,
    };
    await writeFile("application.json", JSON.stringify(application, null, 2),"utf-8");
}
saveApplication();

// reading JSON
async function readApplication() {
    const raw = await readFile("application.json", "utf-8");
    console.log("Raw JSON string:", raw);
    if (!raw.trim()) {
        console.log("JSON file is empty");
        return;
    }
    const data = JSON.parse(raw);
    console.log(data);
}
readApplication();

// Example 6. Paths (Cross-Platform Safe)
import * as path from "path";
const filePath = path.join("data", "files", "log.txt");
console.log("Cross-platform file path:", filePath);