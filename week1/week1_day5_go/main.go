package main

import "fmt"

func main() {
	fmt.Println("OK, Go!")
	name := "Chris"
	someStudyHours := 6
	var moreStudyHours int = 6

	fmt.Println("Examples")
	fmt.Println("Hello,", name)
	fmt.Println("Total study hours:", someStudyHours+moreStudyHours)
	applicationsSent := 12

	if applicationsSent == 0 {
		fmt.Println("Start applying")
	} else if applicationsSent < 10 {
		fmt.Println("Good momentum")
	} else {
		fmt.Println("High volume")
	}
	for i := 1; i <= 5; i++ {
		fmt.Println(i)
	}

	demoApplications := []int{0, 2, 6, 11}

	for _, count := range demoApplications {
		if count == 0 {
			fmt.Println("None")
		} else if count < 10 {
			fmt.Println("Some")
		} else {
			fmt.Println("A lot")
		}
	}

	switch {
	case applicationsSent == 0:
		fmt.Println("None")
	case applicationsSent < 10:
		fmt.Println("Some")
	default:
		fmt.Println("A lot")
	}

	applicationsSent = 7
	effortLevel := ""

	switch {
	case applicationsSent == 0:
		effortLevel = "None"
	case applicationsSent < 10:
		effortLevel = "Some"
	default:
		effortLevel = "A lot"
	}

	fmt.Println("Effort level:", effortLevel)

	/* Exercise 1 — if / else
	   Create studyHours and print:
	   Low if < 5
	   Good if 5–9
	   High if >= 10 */

	fmt.Println()
	fmt.Println("Exercise 1")
	var studyHours int = 6
	if studyHours < 5 {
		fmt.Println("Low")
	} else if studyHours < 10 {
		fmt.Println("Good")
	} else {
		fmt.Println("High")
	}

	/* Exercise 2 — Loop + if
	   Given:
	   applications := []int{0, 2, 6, 11}
	   Loop and print:
	   None
	   Some
	   A lot */
	fmt.Println()
	fmt.Println("Exercise 2")

	applications := []int{0, 2, 6, 11}
	for _, count := range applications {
		if count == 0 {
			fmt.Println("None")
		} else if count < 10 {
			fmt.Println("Some")
		} else {
			fmt.Println("A lot")
		}
	}

	/* Exercise 3 — switch
	   Rewrite Exercise 2 using switch.
	*/
	fmt.Println()
	fmt.Println("Exercise 3")

	for _, count := range applications {
		switch {
		case count == 0:
			fmt.Println("None")
		case count < 10:
			fmt.Println("Some")
		default:
			fmt.Println("A lot")
		}
	}

	/* Exercise 4 — switch Assigning a Value
	   Use switch to assign an effortLevel variable, then print it.
	*/

	fmt.Println()
	fmt.Println("Exercise 4")
	for _, count := range applications {

		switch {
		case count == 0:
			effortLevel = "None"
		case count < 10:
			effortLevel = "Some"
		default:
			effortLevel = "A lot"
		}
		fmt.Println("Effort level ", count, " is ", effortLevel)
	}
	/* Exercise 5 — Comparison (Written)
	   In 1–2 sentences, explain:
	   How does Go’s switch differ from Rust’s match?
	   Go's switch is a more traditional control-flow
	   statement for value comparison, while Rust's match
	   is a powerful pattern-matching expression that
	   guarantees all possibilities are handled by the compiler
	   and can destructure complex data types.
	*/
	/* Go Further (Optional)
	   Try one:
	   Use switch with multiple values in a case
	   Write a small function returning a string
	   Explain why Go avoids expressions in switch
	*/

	// Extra Credit — switch with multiple values in a case
	fmt.Println()
	fmt.Println("Extra Credit")

	day := "Saturday"

	switch day {
	case "Saturday", "Sunday":
		fmt.Println("Weekend")
	case "Monday", "Tuesday", "Wednesday", "Thursday", "Friday":
		fmt.Println("Weekday")
	}

	// Extra Credit — small function returning a string
	dayType := func(day string) string {
		switch day {
		case "Saturday", "Sunday":
			return "Weekend"
		case "Monday", "Tuesday", "Wednesday", "Thursday", "Friday":
			return "Weekday"
		default:
			return "Unknown"
		}
	}
	fmt.Println("Day type for Friday:", dayType("Friday"))

	/* Explanation: Go avoids expressions in switch to maintain clarity
	   and simplicity in control flow, focusing on straightforward value comparisons
	   rather than complex evaluations. */
}
