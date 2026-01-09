package main

import (
	"errors"
	"fmt"
	"log"
	"sort"
)

type StatusReporter interface {
	Status() string
}

type JobApplication struct {
	Company  string
	Sent     int
	Response bool
}

func (j JobApplication) Status() string {
	if j.Response {
		return "Responded"
	}
	return "Pending"
}

func (j JobApplication) StatusWithError() (string, error) {
	if j.Response {
		return "Responded", nil
	}
	return "Pending", errors.New("no response yet") // ⭐ Go Further (Strong Signal) Use errors.Is with a sentinel error
}

func PrintStatus(reporter StatusReporter) {
	fmt.Println("Application Status:", reporter.Status())
}

func TotalSent(apps []JobApplication) int {
	total := 0
	for _, app := range apps {
		total += app.Sent
	}
	return total
}

/*
	Exercise 4 Write: A function that sums total applications sent

Example pattern:
*/
func ExFourTotalSent(apps []JobApplication) int {
	total := 0
	for _, a := range apps {
		total += a.Sent
	}
	return total
}

/* Exercise 4 Write: A function that filters responded applications */
func FilterResponded(apps []JobApplication) []JobApplication {
	var responded []JobApplication
	for _, a := range apps {
		if a.Response {
			responded = append(responded, a)
		}
	}
	return responded
}

// Exercise 5 — Error-Aware Design Write:
func FindApplication(apps []JobApplication, company string) (JobApplication, error) {
	for _, app := range apps {
		if app.Company == company {
			return app, nil
		}
	}
	return JobApplication{}, fmt.Errorf("application for %s not found", company)
}

/* Return an error if not found
Caller must handle it */

func RunExercises() {
	fmt.Println("\nWeek 5 Day 5 — Go Interfaces")

	fmt.Println("\nExercise 2 — Interface Function")
	/*
		Write a function that accepts the interface:
		PrintStatus
		Call it with a JobApplication.

		🧠 Key idea:
		Go has implicit interfaces — no implements keyword. */
	app := JobApplication{"OpenAI", 3, true}
	PrintStatus(app)

	fmt.Println("\nExercise 3 — Slice of Interface Values")
	// Create multiple applications and store them as:
	apps := []JobApplication{
		{"OpenAI", 3, true},
		{"Google", 2, false},
	}
	// Loop and print statuses.
	for _, application := range apps {
		fmt.Println(application.Company)
		PrintStatus(application)
	}
	// Calculate and print total sent using:
	fmt.Println("Total sent:", TotalSent(apps))

	fmt.Println("\nExercise 4 — Functional Style")
	// Given:
	ex_four_apps := []JobApplication{
		{"OpenAI", 3, true},
		{"Google", 2, false},
		{"Meta", 4, true},
	}
	// demonstrate:
	// 1. Total applications sent.
	fmt.Println("Total sent:", ExFourTotalSent(ex_four_apps))
	// 2. Filtered responded applications.
	respondedApps := FilterResponded(ex_four_apps)
	fmt.Println("Responded Applications:")
	for _, app := range respondedApps {
		fmt.Println("-", app.Company)
	}

	// demonstrate FindApplication function:
	fmt.Println("\nExercise 5 — Error-Aware Design")
	appToFind := "Google"
	foundApp, err := FindApplication(ex_four_apps, appToFind)
	if err != nil {
		fmt.Println("Error:", err)
	} else {
		fmt.Println("Found application for:", foundApp.Company)
	}
	anotherAppToFind := "Apple"
	anotherFoundApp, err := FindApplication(ex_four_apps, anotherAppToFind)
	if err != nil {
		fmt.Println("Error:", err)
	} else {
		fmt.Println("Found application for:", anotherFoundApp.Company)
	}

	/* Comparison (Write as Comments)
	In 1–2 sentences each:
	1. How do Go interfaces differ from Rust traits?
	2. How does Go’s FP style differ from TypeScript?
	3. Why does Go avoid inheritance?

	Answers:
	1. Go interfaces are implicit and focus on method sets,
	while Rust traits are explicit and can include default implementations.
	2. Go's FP style emphasizes simplicity and avoids complex abstractions,
	whereas TypeScript allows for more advanced functional programming patterns.
	3. Go avoids inheritance to promote composition over inheritance, leading to more flexible and maintainable code.
	*/

	/* ⭐ Go Further (Strong Signal)
	Try one:
	Use errors.Is with a sentinel error */

	fmt.Println("\n⭐ Go Further (Strong Signal) — Error Handling with Sentinel Error")
	application := JobApplication{"OpenAI", 3, false}
	applyResults, err := application.StatusWithError()
	if err != nil {
		fmt.Println("Error:", err)
	} else {
		fmt.Println("Status:", applyResults)
	}

	fmt.Println()
	log.Println("\n⭐ Go Further (Strong Signal) — Add logging without exiting")

	fmt.Println("\nUse sort.Slice on applications")
	// Sort applications by Company name
	sort.Slice(ex_four_apps, func(i, j int) bool {
		return ex_four_apps[i].Company < ex_four_apps[j].Company
	})
	fmt.Println("Sorted Applications by Company:")
	for _, app := range ex_four_apps {
		fmt.Println("-", app.Company)
	}
	/*	Explain why Go avoids generics-heavy FP (comment)
		Go avoids a generics-heavy functional programming (FP) style primarily due to its core philosophy of simplicity,
		readability, and explicitness. The language design prioritizes code that is easy to write, read, and maintain
		over powerful, abstract features that might increase complexity.
	*/
}
