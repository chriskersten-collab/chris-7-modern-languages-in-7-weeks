// copied from example_one.rs
struct JobApplication {
    company: String,
    applications_sent: u32,
    response: bool,
}

impl JobApplication {
    fn summary(&self) -> String {
        format!(
            "Applied to {} ({} times) — Response: {}",
            self.company,
            self.applications_sent,
            self.response
        )
    }
}


// Example 2 - define a trait
trait Summarizable {
    fn summary(&self) -> String;
} // Traits define what a type can do, not what it is.

// Example 3 — Implement Trait for Struct
impl Summarizable for JobApplication {
    fn summary(&self) -> String {
        format!(
            "{} — applied {} times",
            self.company,
            self.applications_sent
        )
    }
} // Now JobApplication implements behavior, not inheritance.

// Example 4 — Trait Bounds (Static Dispatch)
fn print_summary<T: Summarizable>(item: &T) {
    println!("{}", item.summary());
}
/* Resolved at compile time
Zero runtime cost
Extremely fast */

// Example 5 — Dynamic Dispatch (dyn Trait)
fn print_summary_dyn(item: &dyn Summarizable) {
    println!("{}", item.summary());
}
/* Runtime dispatch
Needed for heterogeneous collections */

pub fn run() {
    let application = JobApplication {
        company: String::from("Tech Corp"),
        applications_sent: 3,
        response: true,
    };

    // Using static dispatch
    print_summary(&application);

    // Using dynamic dispatch
    print_summary_dyn(&application);
}