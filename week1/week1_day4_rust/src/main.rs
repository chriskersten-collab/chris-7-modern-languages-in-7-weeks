fn main() {
    let study_hours = 6;

    if study_hours < 5 {
         println!("Low");
    } else if study_hours < 10 {
         println!("Good");
    } else {
         println!("High");
    }
    let applications = [0, 2, 6, 11];
    for count in applications {
         if count == 0 {
             println!("None");
         } else if count < 10 {
             println!("Some");
         } else {
             println!("A lot");
         }
    }
    for count in applications {
         match count {
             0 => println!("None"),
             1..=9 => println!("Some"),
             _ => println!("A lot"),
         }
     }

     let applications_sent = 7;

     let effort_level = match applications_sent {
         0 => "None",
         1..=9 => "Some",
         _ => "A lot",
     };

     println!("Effort level: {}", effort_level);

}
