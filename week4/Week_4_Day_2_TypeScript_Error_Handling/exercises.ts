console.log('\nExercise 1 — Safe JSON Parsing');
/*
Write a function:
function safeParseJson(input: string): object | null

Rules:
Try parsing JSON
Return null if parsing fails
Do NOT throw
*/
function safeParseJson(input: string): object | null {
    try {
        return JSON.parse(input);
    } catch {
        return null;
    }
}

// Test cases
console.log(safeParseJson('{"valid": "json"}')); // Should log the parsed object
console.log(safeParseJson('invalid json')); // Should log null

console.log('\nExercise 2 — Input Validation');
/*
Rules:
Convert string → number
If NaN, throw an Error
Caller must handle it
*/
function parseHours(input: string): number
{
    const hours = Number(input);
    if (isNaN(hours)) {
        throw new Error("Invalid number");
    }
    return hours;
}
// Test cases
try {
    console.log(parseHours("8")); // Should log: 8
} catch (error) {
    console.error("Error:", error);
}
try {
    console.log(parseHours("eight")); // Should throw an error
} catch (error) {
    console.error("Error:", error);
}

console.log('\nExercise 3 — Multiple Error Types');
/*
Simulate:
A thrown Error
A missing map key
Handle each cleanly.
*/
function getCompanyResponse(responses: Map<string, boolean>, company: string): boolean {
    const response = responses.get(company);
    if (response === undefined) {
        throw new Error(`No response found for company: ${company}`);
    }
    return response;
}
// Test cases
const exercise_responses = new Map<string, boolean>([
    ["CompanyA", true],
    ["CompanyB", false],
]);
// Test cases
try {
    console.log(getCompanyResponse(exercise_responses, "CompanyA")); // Should log: true
} catch (error) {
    console.error("Error:", error);
}
try {
    console.log(getCompanyResponse(exercise_responses, "CompanyC")); // Should throw an error
} catch (error) {
    console.error("Error:", error);
}

/*
Go Further (Optional, Strong Signal)

Try one:
Create a custom error class
Wrap one error inside another
Use never for unreachable code
Compare throw vs returning null
*/
class CustomError extends Error {
    constructor(message: string) {
        super(message);
        this.name = "CustomError";
    }
}

console.log('\nWrap one error inside another:');
function wrapErrorExample() {
    try {
        throw new Error("Original error");
    } catch (error) {
        throw new CustomError("Wrapped error: " + (error as Error).message);
    }
}
// Test cases
try {
    wrapErrorExample();
} catch (error) {
    console.error("Error:", error);
}

console.log('\nUse never for unreachable code:');
function unreachableCodeExample(): never {
    throw new Error("This code should never be reached");
}
// Test cases
try {
    unreachableCodeExample();
} catch (error) {
    console.error("Error:", error);
}
/* Compare throw vs returning null: 
throw is used for exceptional, unexpected errors that abort code execution, 
while returning null is for expected "no value" or "not found" scenarios 
that the calling code should handle as part of the normal program flow. */

/* console log with errors: 

Exercise 1 — Safe JSON Parsing
{ valid: 'json' }
null

Exercise 2 — Input Validation
8
Error: Error: Invalid number
    at parseHours (P:\Documents\PythonLessons\week4\Week_4_Day_2_TypeScript_Error_Handling\exercises.ts:34:15)
    at Object.<anonymous> (P:\Documents\PythonLessons\week4\Week_4_Day_2_TypeScript_Error_Handling\exercises.ts:45:17)
    at Module._compile (node:internal/modules/cjs/loader:1761:14)
    at Module.m._compile (C:\Users\chris\AppData\Roaming\npm\node_modules\ts-node\src\index.ts:1618:23)
    at node:internal/modules/cjs/loader:1893:10
    at Object.require.extensions.<computed> [as .ts] (C:\Users\chris\AppData\Roaming\npm\node_modules\ts-node\src\index.ts:1621:12)     
    at Module.load (node:internal/modules/cjs/loader:1481:32)
    at Module._load (node:internal/modules/cjs/loader:1300:12)
    at TracingChannel.traceSync (node:diagnostics_channel:328:14)
    at wrapModuleLoad (node:internal/modules/cjs/loader:245:24)

Exercise 3 — Multiple Error Types
true
Error: Error: No response found for company: CompanyC
    at getCompanyResponse (P:\Documents\PythonLessons\week4\Week_4_Day_2_TypeScript_Error_Handling\exercises.ts:60:15)
    at Object.<anonymous> (P:\Documents\PythonLessons\week4\Week_4_Day_2_TypeScript_Error_Handling\exercises.ts:76:17)
    at Module._compile (node:internal/modules/cjs/loader:1761:14)
    at Module.m._compile (C:\Users\chris\AppData\Roaming\npm\node_modules\ts-node\src\index.ts:1618:23)
    at node:internal/modules/cjs/loader:1893:10
    at Object.require.extensions.<computed> [as .ts] (C:\Users\chris\AppData\Roaming\npm\node_modules\ts-node\src\index.ts:1621:12)     
    at Module.load (node:internal/modules/cjs/loader:1481:32)
    at Module._load (node:internal/modules/cjs/loader:1300:12)
    at TracingChannel.traceSync (node:diagnostics_channel:328:14)
    at wrapModuleLoad (node:internal/modules/cjs/loader:245:24)

Wrap one error inside another:
Error: CustomError: Wrapped error: Original error
    at wrapErrorExample (P:\Documents\PythonLessons\week4\Week_4_Day_2_TypeScript_Error_Handling\exercises.ts:102:15)
    at Object.<anonymous> (P:\Documents\PythonLessons\week4\Week_4_Day_2_TypeScript_Error_Handling\exercises.ts:107:5)
    at Module._compile (node:internal/modules/cjs/loader:1761:14)
    at Module.m._compile (C:\Users\chris\AppData\Roaming\npm\node_modules\ts-node\src\index.ts:1618:23)
    at node:internal/modules/cjs/loader:1893:10
    at Object.require.extensions.<computed> [as .ts] (C:\Users\chris\AppData\Roaming\npm\node_modules\ts-node\src\index.ts:1621:12)     
    at Module.load (node:internal/modules/cjs/loader:1481:32)
    at Module._load (node:internal/modules/cjs/loader:1300:12)
    at TracingChannel.traceSync (node:diagnostics_channel:328:14)
    at wrapModuleLoad (node:internal/modules/cjs/loader:245:24)

Use never for unreachable code:
Error: Error: This code should never be reached
    at unreachableCodeExample (P:\Documents\PythonLessons\week4\Week_4_Day_2_TypeScript_Error_Handling\exercises.ts:114:11)
    at Object.<anonymous> (P:\Documents\PythonLessons\week4\Week_4_Day_2_TypeScript_Error_Handling\exercises.ts:118:5)
    at Module._compile (node:internal/modules/cjs/loader:1761:14)
    at Module.m._compile (C:\Users\chris\AppData\Roaming\npm\node_modules\ts-node\src\index.ts:1618:23)
    at node:internal/modules/cjs/loader:1893:10
    at Object.require.extensions.<computed> [as .ts] (C:\Users\chris\AppData\Roaming\npm\node_modules\ts-node\src\index.ts:1621:12)     
    at Module.load (node:internal/modules/cjs/loader:1481:32)
    at Module._load (node:internal/modules/cjs/loader:1300:12)
    at TracingChannel.traceSync (node:diagnostics_channel:328:14)
    at wrapModuleLoad (node:internal/modules/cjs/loader:245:24)
*/
