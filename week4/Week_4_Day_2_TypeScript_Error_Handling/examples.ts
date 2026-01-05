console.log('\nExample 1 — Basic try / catch');
try {
    const result = JSON.parse('not valid JSON');
    console.log('Parsed result:', result);
} catch (error) {
    console.error('Error parsing JSON:', error);
}

console.log('\nExample 2 — Narrowing unknown Errors (Very Important)');
try {
    throw new Error('Something went wrong!');
} catch (error) {
    if (error instanceof Error) {
        console.error(error.message);
    } else {
        console.error('Caught an unknown error: ', error);
    }
}

console.log('\nExample 3 — Throwing Your Own Errors');
function validateApplications(count: number): void {
    if (count < 0) {
        throw new Error('Application count cannot be negative');
    }
}
try {
    validateApplications(-5);
} catch (error) {
    if (error instanceof Error) {
        console.error('Validation error:', error.message);
    }
}

console.log('\nExample 4 — Defensive Programming with undefined');
function getResponse(responses: Map<string, boolean>, company: string): boolean {
    const value = responses.get(company);
    if (value === undefined) {
        throw new Error(`No response found for company: ${company}`);
    }
    return value;
}