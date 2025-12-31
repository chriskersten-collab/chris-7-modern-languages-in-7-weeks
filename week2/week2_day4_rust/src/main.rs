fn main() {

    // Example 1 Companies You Applied To
    let mut companies: Vec<String> = Vec::new();
    companies.push(String::from("OpenAI"));
    companies.push(String::from("Google"));
    companies.push(String::from("Amazon"));
    println!("\nExample 1 Companies You Applied To");
    println!("{:?}", companies);
    for company in &companies {
        println!("Applied to {}", company);
    }

    // Example 2 HashMap<K, V> — Rust’s Dictionary
    use std::collections::HashMap;
    let mut responses: HashMap<String, bool> = HashMap::new();
    responses.insert(String::from("OpenAI"), true);
    responses.insert(String::from("Google"), false);
    println!("\nExample 2 HashMap<K, V> — Rust’s Dictionary");
    println!("{:?}", responses);
    match responses.get("OpenAI") {
        Some(value) => println!("OpenAI Response: {}", value),
        None => println!("No entry"),
    }

    /* Exercise 1 — Vec Basics
    Create a Vec<String> of at least 5 skills.
    Add one
    Remove one
    Print all */
    let mut skills: Vec<String> = Vec::new();
    skills.push(String::from("Rust"));
    skills.push(String::from("JavaScript"));
    skills.push(String::from("Python"));
    skills.push(String::from("SQL"));
    skills.push(String::from("Go"));
    skills.push(String::from("TypeScript")); // Add one
    skills.remove(1); // Remove one (JavaScript)
    println!("\nExercise 1 — Vec Basics");
    for skill in &skills {
        println!("Skill: {}", skill);  
    }

    /* Exercise 2 — Iteration & Borrowing
    Loop over the skills vector and print each skill without taking ownership.
    (Hint: borrow) */
    println!("\nExercise 2 — Iteration & Borrowing");
    for skill in &skills {
        println!("Skill: {}", skill);  
    }

    /* Exercise 3 — HashMap
    Create a HashMap<String, i32> mapping skill → level. */
    let mut skill_levels: HashMap<String, i32> = HashMap::new();
    skill_levels.insert(String::from("Rust"), 2);
    skill_levels.insert(String::from("Python"), 4);
    skill_levels.insert(String::from("SQL"), 3);
    println!("\nExercise 3 — HashMap");
    for (skill, level) in &skill_levels {
        println!("Skill: {}, Level: {}", skill, level);
    }

    /* Exercise 4 — Safe Access
    Use match or if let to safely read a value from the map. */
    println!("\nExercise 4 — Safe Access");
    match skill_levels.get("Rust") {
        Some(level) => println!("Rust Level: {}", level),
        None => println!("No entry for Rust"),
    }
        match skill_levels.get("C#") {
        Some(level) => println!("C# Level: {}", level),
        None => println!("No entry for C#"),
    }
    /* Exercise 5 — Comparison (Written)
    In 1–2 sentences, explain:
    How does Rust’s ownership model affect how you use data structures 
    compared to Python? 
    In Rust, ownership rules require careful management of data lifetimes 
    and borrowing, which can lead to more explicit handling of references 
    compared to Python's dynamic typing and garbage collection that abstracts away 
    memory management. */

    /* Go Further (Optional)
    Use entry() API
    Convert a Vec<String> into a HashMap
    Write a function borrowing a Vec<String> */
    //use std::collections::HashMap; // Already imported above
    println!("\nGo Further (Optional)");
    println!("Using entry() API:");
    let mut skill_count: HashMap<String, i32> = HashMap::new();
    for skill in &skills {
        let count = skill_count.entry(skill.clone()).or_insert(0);
        *count += 1;
        println!("Skill: {}, Count: {}", skill, count);
    }
    println!("Convert a Vec<String> into a HashMap:");
    let skill_map: HashMap<_, _> = skills.iter().map(|s| (s.clone(), s.len() as i32)).collect();
    for (skill, length) in &skill_map {
        println!("Skill: {}, Length: {}", skill, length);
    }
    println!("Function borrowing a Vec<String>:");
    fn print_skills(skills: &Vec<String>) {
        for skill in skills {
            println!("Skill from function: {}", skill);
        }
    }
    print_skills(&skills);
}