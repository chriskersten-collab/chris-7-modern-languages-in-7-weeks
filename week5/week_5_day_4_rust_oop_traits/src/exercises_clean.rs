// Feedback from ChatGPT lesson review: this is the cleaned-up version of the exercises file.
// Exercise 1 — Trait Definition
trait Status {
    fn status(&self) -> String {
        "Unknown".to_string()
    }
}

// Go Further — Additional Trait
trait Summarizable {
    fn summary(&self) -> String;
}

// JobApplication struct (required)
struct JobApplication {
    company: String,
    applications_sent: u32,
    response: bool,
}

// Exercise 2 — Implement Traits
impl Status for JobApplication {
    fn status(&self) -> String {
        if self.response {
            "Responded".to_string()
        } else {
            "Pending".to_string()
        }
    }
}

impl Summarizable for JobApplication {
    fn summary(&self) -> String {
        format!(
            "{} — {} applications",
            self.company, self.applications_sent
        )
    }
}

// Exercise 3 — Trait Bound Function
fn print_status<T: Status + ?Sized>(item: &T) {
    println!("Status: {}", item.status());
}

// Go Further — Multiple Trait Bounds
fn notify<T: Status + Summarizable>(item: &T) {
    println!("{} | {}", item.summary(), item.status());
}

// Entry point for this module
pub fn run() {
    let application = JobApplication {
        company: "Tech Corp".into(),
        applications_sent: 3,
        response: true,
    };

    // Trait bound usage
    print_status(&application);
    notify(&application);

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

    for app in apps {
        print_status(&*app);
    }
}
