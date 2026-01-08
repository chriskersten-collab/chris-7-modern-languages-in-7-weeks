/* 
Example 1 — Define a Struct + Method
✅ Similar to a class method
❌ No inheritance
 */
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

pub fn run() {
    let application = JobApplication {
        company: String::from("Tech Corp"),
        applications_sent: 3,
        response: true,
    };

    println!("{}", application.summary());
}