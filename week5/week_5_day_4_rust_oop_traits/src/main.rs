mod example_one;
mod example_two_through_five;
mod exercises_clean;

fn main() {
    println!("\nExample 1 — Define a Struct + Method and demonstrate its usage");
    example_one::run();

    println!("\nExamples 2 through 5 — Define a Trait, Implement it for a Struct, and demonstrate static and dynamic dispatch");
    example_two_through_five::run();

    println!("\nExercises Cleaned Up — Implement Traits and Demonstrate Usage");
    exercises_clean::run();
}
