/* Exercise 1 — Trait Definition
Create a trait: 
*/
trait Status {
    fn status(&self) -> String {
        "Unknown".to_string() // ⭐ Go Further (Strong Signal) 1️⃣ Default Trait Methods
    }
}

// Exercise 2 — Implement Trait
 impl Status for JobApplication {
    fn status(&self) -> String {
        if self.response {
            "Responded".to_string()
        } else {
            "Pending".to_string()
        }
    }
}

// Exercise 3 — Trait Bound Function
fn print_status<T: Status>(item: &T) {
    println!("Status: {}", item.status());
}

// ⭐ Go Further (Strong Signal) 2️⃣ Trait + Generic Return Type
fn notify<T: Status + Summarizable>(item: &T) {
    println!("{} — {}", item.summary(), item.status());
}


// Exercise 4 — Trait Object Vector
let apps: Vec<Box<dyn Status>> = vec![
    Box::new(JobApplication {
        company: "OpenAI".into(),
        applications_sent: 3,
        response: true,
    }),
    Box::new(JobApplication {
        company: "Google".into(),
        applications_sent: 2,
        response: false,
    }),
];

pub fn run() {
    let application = JobApplication {
        company: String::from("Tech Corp"),
        applications_sent: 3,
        response: true,
    };

    // Using trait bound function
    print_status(&application);

    // Using trait object vector
    for app in apps {
        print_status(&*app);
    }
}

/* Exercise 5 — Comparison (Written)

In 1–2 sentences, explain:
How do Rust traits compare to Python inheritance?
✍️ Add as a comment in your file. 

Rust traits define shared behavior that types can implement without forming a strict hierarchical relationship, 
unlike Python inheritance which establishes a parent-child class structure. 
Traits promote composition over inheritance, allowing for more flexible code reuse.
*/

/* ⭐ Go Further (Strong Signal)  
3️⃣ Why Rust Avoids Inheritance (Comment)

Focus on:
Compile-time safety
No diamond problem
Explicit behavior

Rust avoids traditional inheritance to ensure compile-time safety by preventing ambiguities like the diamond problem, 
where multiple inheritance paths can lead to conflicting implementations.
*/