package main

import (
	"fmt"
	"slices"
)

func main() {
	fmt.Println("Example 1: Slices (Go's most important data structure)")
	applications := []string{"OpenAI", "Google", "Amazon"}
	applications = append(applications, "Microsoft")
	fmt.Println(applications)
	fmt.Println("First", applications[0])
	fmt.Println("Total:", len(applications))
	for _, company := range applications {
		fmt.Println("Applied to:", company)
	}

	fmt.Println("\nExample 2: Maps(Dictionaries)")
	responses := map[string]bool{
		"OpenAI": true,
		"Google": false,
	}
	fmt.Println("OpenAI response:", responses["OpenAI"])
	// safe access pattern (very important)
	value, exists := responses["Amazon"]
	if exists {
		fmt.Println("Amazon response:", value)
	} else {
		fmt.Println("No Amazon entry")
	}

	fmt.Println("\nExample 3: Structs (Typed Records)")
	type ExampleJobApplication struct {
		Company          string
		Role             string
		ApplicationsSent int
		Response         bool
	}
	app := ExampleJobApplication{
		Company:          "OpenAI",
		Role:             "Data Scientist",
		ApplicationsSent: 12,
		Response:         true,
	}
	fmt.Println("Applied to", app.Company, app.ApplicationsSent,
		"times for the role of", app.Role,
		". Response:", app.Response)

	fmt.Println("\nExample 4. Slice of Structs (Real-World Pattern)")
	jobApplications := []ExampleJobApplication{
		{Company: "OpenAF", Role: "DS", ApplicationsSent: 12, Response: true},
		{Company: "Google", Role: "DS", ApplicationsSent: 5, Response: false},
	}
	for _, app := range jobApplications {
		fmt.Println(app.Company, "-> Response:", app.Response)
	}

	fmt.Println("\nExercise 1 - Slices")
	// Create a slice of at least 5 companies:
	// Add one
	// Remove one (by index)
	// Print all
	mySlice := []string{"OpenSesame", "Pizza Renzo", "Tropical Tacos", "Google", "Spotify"}
	mySlice = append(mySlice, "Cromulent Electromotive")
	mySlice = slices.Delete(mySlice, 2, 3)
	for _, company := range mySlice {
		fmt.Println("Applied to:", company)
	}

	fmt.Println("\nExercise 2 - Maps")
	// Create a map[string]int:
	// company → applications sent
	// Print values
	// Safely check for a missing company
	myMap := map[string]int{
		"OpenSesame":  3,
		"Pizza Renzo": 5,
	}
	for _, company := range mySlice {
		value, exists := myMap[company]
		if exists {
			fmt.Println("Company:", company, "Applications Sent:", value)
		} else {
			fmt.Println("Company:", company, "No entry found")
		}
	}

	fmt.Println("\nExercise 3 — Struct")
	// Define a JobApplication struct:
	// company
	// role
	// response
	// Create one instance and print fields.
	type JobApplication struct {
		Company  string
		Role     string
		Response bool
	}
	exerciseApp := JobApplication{
		Company:  "Spotify",
		Role:     "Database Engineer",
		Response: false,
	}
	fmt.Println("Applied to", exerciseApp.Company,
		"for the role of", exerciseApp.Role,
		". Response:", exerciseApp.Response)

	fmt.Println("\nExercise 4 — Slice of Structs")
	// Create 3 job applications in a slice.
	// Loop and print:
	// company
	// response
	exerciseApps := []JobApplication{
		{Company: "OpenSesame", Role: "Seeed Engineer", Response: true},
		{Company: "Pizza Renzo", Role: "Quality Assurance Engineer", Response: false},
		{Company: "Cromulent Electromotive", Role: "Fullstack Taster", Response: true},
	}
	for _, app := range exerciseApps {
		fmt.Println("Applied to", app.Company, "Response:", app.Response)
	}

	// Exercise 5 — Comparison (Written)
	// In 1–2 sentences, explain:
	// How do Go’s data structures compare to Rust’s in terms of safety and simplicity?
	// Answer: Go's data structures like slices, maps, and structs are designed for simplicity and ease of use,
	// with built-in safety features such as bounds checking for slices and safe access patterns for maps.
	// Rust's data structures, while also safe, often require more explicit management of ownership and lifetimes,
	// which can add complexity but provides stronger guarantees about memory safety.

	fmt.Printf("\nGo Further (Optional, Strong Signal)")
	// Try one:
	// Use map[string]JobApplication
	// Write a function that accepts a slice of structs
	// Explain Go’s zero values (what happens if you read a missing map key?)
	// Go's zero values are the default values assigned to variables when they are declared without initialization.
	// For example, a missing map key returns the zero value for the value type (e.g., false for bool, 0 for int).
	mapOfApps := map[string]JobApplication{
		"OpenSesame":  {Company: "OpenSesame", Role: "Seed Engineer", Response: true},
		"Pizza Renzo": {Company: "Pizza Renzo", Role: "Quality Assurance Engineer", Response: false},
	}
	fmt.Println("\nMap of Job Applications:")
	for company, app := range mapOfApps {
		fmt.Println("Company:", company, "Role:", app.Role, "Response:", app.Response)
	}
	fmt.Println("\nWrite a function that accepts a slice of structs:")
	for _, app := range exerciseApps {
		printApplications(app.Company, app.Response)
	}

}

func printApplications(company string, response bool) {
	fmt.Println("Applied to", company, "Response:", response)
}
