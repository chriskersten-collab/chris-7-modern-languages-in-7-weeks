use std::fs;
use std::io;

/* Example 3 — Proper Error Handling (Professional Rust) */
fn read_file(path: &str) -> Result<String, io::Error> {
    fs::read_to_string(path)
}

/* Go Further: Write a function that returns Result<()> */
fn write_file(path: &str, content: &str) -> Result<(), io::Error> {
    fs::write(path, content)
}

fn main() {
    println!("Week 3 Day 4: Rust File I/O");
    println!("Example 1 — Write a File");
    fs::write(
        "study_log.txt",
        "Name: Chris\nDate: 2026-Jan-03\nHours studied: 1\n"
    ).expect("Failed to write to file");
    println!("File written successfully.");

    println!("Example 2 — Read a File");
    let contents = fs::read_to_string("study_log.txt")
        .expect("Failed to read the file");
    println!("File contents:\n{}", contents);

    println!("Example 3 — Proper Error Handling (Professional Rust)");
    match read_file("study_log.txt") {
        Ok(contents) => println!("{}", contents),
        Err(err) => println!("Error reading file: {}", err),
        }

    println!("Exercise 1 — Write a File");
    /* Write study_log.txt containing:
    Your name
    Today’s date
    Hours studied today */
    fs::write(
        "study_log.txt",
        "Your name: Chris\nToday's date: 2026-Jan-03\nHours studied today: 1\n"
    ).expect("Failed to write to file");
    println!("Exercise 1 completed. See study_log.txt file.");

    println!("Exercise 2 — Read the File");
    /* Read study_log.txt and print it. */
    let contents = fs::read_to_string("study_log.txt")
        .expect("Failed to read the file");
    println!("File contents:\n{}", contents);

    println!("Exercise 3 — Error Handling");
    /* Try reading a file that does not exist.
    Handle the error without crashing. */
    match read_file("nonexistent_file.txt") {
        Ok(contents) => println!("{}", contents),
        Err(err) => println!("Error reading file: {}", err),
        }
    println!("Exercise 3 completed.");

    println!("Exercise 4 - CSV-style Data");
    /* Create a string like:
    company,applications_sent,response
    OpenAI,3,true
    Google,2,false
    Write it to applications.csv. */
    fs::write(
        "applications.csv",
        "company,applications_sent,response\nOpenAI,3,true\nGoogle,2,false\n"
    ).expect("Failed to write to file");
    println!("Exercise 4 completed. See applications.csv file.");

    /* Exercise 5 — Comparison (Written)
    In 1–2 sentences, explain:
    How does Rust’s file I/O safety compare to Python’s?
    With Python, file I/O is less safe because it doesn't enforce compile-time checks for file operations, 
    whereas Rust ensures safety through its type system and error handling mechanisms. */

    /* Go Further (Optional, Strong Signal)
    Try one:
    Append to a file instead of overwriting
    Use std::fs::OpenOptions
    Write a function that returns Result<()> */
    println!("Go Further: Append to a file instead of overwriting, using std::fs::OpenOptions");
    use std::fs::OpenOptions;
    use std::io::Write;
    let mut file = OpenOptions::new()
        .append(true)
        .open("study_log.txt")
        .expect("Failed to open file for appending");
    writeln!(file, "Additional study log entry.").expect("Failed to write to file");
    println!("Appended to study_log.txt successfully.");

    println!("Go Further: Write a function that returns Result<()>");
    /* This code uses the write_file function defined above */
    match write_file("new_study_log.txt", "This is a new study log entry.\n") {
        Ok(()) => println!("File written successfully."),
        Err(err) => println!("Error writing file: {}", err),
    }
}
