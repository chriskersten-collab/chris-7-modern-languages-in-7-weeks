use std::fs;
use std::io;
use std::collections::HashMap;

fn parse_hours(input: &str) -> Result<i32, std::num::ParseIntError> {
    input.parse::<i32>()
}

fn read_file(path: &str) -> Result<String, io::Error> {
    let contents = fs::read_to_string(path)?;
    Ok(contents)
}

fn find_skill<'a>(skills: Vec<&'a str>, target: &'a str) -> Option<&'a str> {
    for skill in skills {
        if skill == target {
            return Some(skill);
        }
    }
    None
}

fn parse_number(input: &str) -> Result<i32, std::num::ParseIntError> {
    input.parse::<i32>()
}

fn safe_read(path: &str) -> Result<String, std::io::Error> {
    std::fs::read_to_string(path)
}

fn get_response(
    responses: &HashMap<String, bool>,
    company: &str,
) -> Option<bool> {
    responses.get(company).copied()
}

fn require_value(value: Option<i32>) -> Result<i32, String> {
    match value {
        Some(v) => Ok(v),
        None => Err("Value missing".to_string()),
    }
}

fn main() {
    println!("\nExample 1 — Handling Result with match");
    /* See also fn parse_hours */
    match parse_hours("5") {
        Ok(hours) => println!("Parsed hours: {}", hours),
        Err(err) => println!("Error parsing hours: {}", err),
    }
    match parse_hours("not_a_number") {
        Ok(hours) => println!("Parsed hours: {}", hours),
        Err(err) => println!("Error parsing hours: {}", err),
    }

    println!("\nExample 2 — Using ? to Propagate Errors");
    /* See also fn read_file */
    match read_file("non_existing_file.txt") {
        Ok(text) => println!("File contents: {}", text),
        Err(err) => println!("Error reading file: {}", err),
    }
    match read_file("existing_file.txt") {
        Ok(text) => println!("File contents: {}", text),
        Err(err) => println!("Error reading file: {}", err),
    }

    println!("\nExample 3 — Option vs Result");
    /* See also fn find_skill */
    let skills = vec!["Rust", "Python", "Go"];
    let target = "Rust";
    match find_skill(skills, target) {
        Some(skill) => println!("Found skill: {}", skill),
        None => println!("Skill not found"),
    }

    println!("\nExercise 1 — Safe Parsing");
    /* Given fn parse_number */
    /* Call it with:
        "10"
        "ten"
        Handle both cases safely. */
    let inputs = vec!["10", "ten"];
    for input in inputs {
        match parse_number(input) {
            Ok(number) => println!("Parsed number: {}", number),
            Err(err) => println!("Error parsing number from '{}': {}", input, err),
        }
    }

    println!("\nExercise 2 — File Read with ?");
    /* Given fn safe_read */
    /* Call it from main and print either the contents or a friendly error. */
    match safe_read("non_existing_file.txt") {
        Ok(contents) => println!("File contents: {}", contents),
        Err(err) => println!("Error reading file: {}", err),
    }
    match safe_read("existing_file.txt") {
        Ok(contents) => println!("File contents: {}", contents),
        Err(err) => println!("Error reading file: {}", err),
    }

    println!("\nExercise 3 — Option Handling");
    /* Given fn get_response */
    /* Print:
        Response if found
        “No entry found” otherwise */
    let mut responses = HashMap::new();
    responses.insert("CompanyA".to_string(), true);
    responses.insert("CompanyB".to_string(), false);

    match get_response(&responses, "CompanyA") {
        Some(response) => println!("Response for CompanyA: {}", response),
        None => println!("No entry found for CompanyA"),
    }
    match get_response(&responses, "CompanyC") {
        Some(response) => println!("Response for CompanyC: {}", response),
        None => println!("No entry found for CompanyC"),
    }

    println!("\nExercise 4 — Convert Option → Result");
    /* Given fn require_value */
    /* Why is this useful? */
    /* 
    It is useful because it allows us to convert an Option type, which may or may not contain a value, 
    into a Result type that can provide more context about the absence of a value by including an error message. 
    This is particularly helpful in scenarios where we want to enforce the presence of a value 
    and handle the absence in a more informative way.
     */
    /* Demo of calling require_value with valid and invalid values */
    match require_value(Some(42)) {
        Ok(value) => println!("Got value: {}", value),
        Err(err) => println!("Error: {}", err),
    }
    match require_value(None) {
        Ok(value) => println!("Got value: {}", value),
        Err(err) => println!("Error: {}", err),
    }

    /* 
    Exercise 5 — Comparison (Written)
    In 1–2 sentences:
    How does Rust’s error handling differ from Python’s exceptions?
    (Add as a comment.)
     
    Rust's error handling uses the Result and Option types to explicitly represent success and failure, 
    requiring developers to handle errors at compile time. 
    In contrast, Python uses exceptions that can be raised and caught at runtime, 
    which may lead to unhandled exceptions if not properly managed.
    */

    /* Go Further (Optional, Strong Signal)
    Try one:

    ✅ Custom Error Type
    #[derive(Debug)]
    enum AppError {
        InvalidInput,
        FileError(std::io::Error),
    }

    Use it in a function signature. */

    #[derive(Debug)]
    enum AppError {
        InvalidInput,
        FileError(std::io::Error),
    }
    fn custom_error_example(path: &str) -> Result<String, AppError> {
        let contents = fs::read_to_string(path).map_err(AppError::FileError)?;
        if contents.is_empty() {
            return Err(AppError::InvalidInput);
        }
        Ok(contents)
    }

    /*
    ✅ When to panic!
    Add a comment answering:
    When is panic! acceptable in Rust?
    (Hint: programmer bugs, invariants, unreachable states.)

    Panic! is acceptable in Rust when dealing with programmer errors, 
    such as violating invariants or reaching unreachable states.

    ✅ unwrap() vs expect()
    Explain why expect("meaningful message") is preferred. 

    expect() is preferred over unwrap() because it allows developers to provide a meaningful error message,
    which aids in debugging by giving context about the failure, whereas unwrap() will simply panic without context.
    */
}