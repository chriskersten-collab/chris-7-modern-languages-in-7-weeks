package main

import (
	"errors"
	"fmt"
	"log"
	"os"
	"strconv"
)

// Define a sentinel error using errors.New
var ErrDidNotApply = errors.New("did not apply")
var ErrRejected = errors.New("application rejected")

func applyToJob(arg int) error {
	if arg == 2 {
		// Return the specific sentinel error
		return ErrDidNotApply
	} else if arg == 4 {
		// Wrap the sentinel error ErrRejected with added context using %w
		return fmt.Errorf("applying to job: %w", ErrRejected)
	}
	return nil
}

func demoLogReturn() error {
	err := fmt.Errorf("this is a sample error")
	if err != nil {
		log.Println("Logged error:", err)
		return err
	}
	return nil
}

func checkCompanyResponse(company string, responses map[string]bool) (bool, error) {
	response, ok := responses[company]
	if !ok {
		return false, fmt.Errorf("company %s not found", company)
	}
	return response, nil
}

func readLogFile(path string) (string, error) {
	data, err := os.ReadFile(path)
	if err != nil {
		return "", fmt.Errorf("readLogFile failed: %w", err)
	}
	return string(data), nil
}

func parseApplications(input string) (int, error) {
	applications, err := strconv.Atoi(input)
	if err != nil {
		return 0, err
	}
	return applications, nil
}

func main() {

	fmt.Println("\nExercise 1 — Safe Parsing")
	/* Write a function:
	func parseApplications(input string) (int, error)
	Rules:
	Convert string → int
	If invalid, return an error
	Caller must handle it
	parseApplications is declared above
	test code:
	*/
	test_applications, err := parseApplications("10")
	if err != nil {
		fmt.Println("Error:", err)
		return
	}
	fmt.Println("Applications:", test_applications)

	fmt.Println("\nExercise 2 — File Read with Context")
	/* Write:
	func readLogFile(path string) (string, error)
	Rules:
	Use os.ReadFile
	Wrap errors with context using fmt.Errorf */
	log_content, err := readLogFile("logfile.txt")
	if err != nil {
		fmt.Println("Error reading log file:", err)
		return
	}
	fmt.Println("Log file content:", log_content)

	fmt.Println("\nExercise 3 — Map Lookup Safety")
	/* Given:
	responses := map[string]bool{
		"OpenAI": true,
		"Google": false,
	}

	Write a function that:
	Returns (bool, error)
	Errors if the company is missing

	see checkCompanyResponse above.
	Test code: */
	responses := map[string]bool{
		"OpenAI": true,
		"Google": false,
	}
	company_response, err := checkCompanyResponse("OpenAI", responses)
	if err != nil {
		fmt.Println("Error:", err)
		return
	}
	fmt.Println("Company response:", company_response)

	fmt.Println("\nExercise 4 — Logging vs Returning Errors")
	/* Write code that:
	Logs an error using log.Println
	Returns the error instead of exiting
	🧠 Explain in a comment why libraries should not call os.Exit()

	Libraries should not call os.Exit() because it would terminate the entire program,
	preventing the caller from handling the error gracefully or performing any cleanup.
	Instead, libraries should return errors to allow the caller to decide how to handle them.

	See demoLogReturn() above.
	test code: */
	demoLogReturn()

	/* Exercise 5 — Comparison (Written)
	In 1–2 sentences, explain:
	How does Go’s error handling philosophy differ from Rust’s and Python’s?
	(Add as a comment.)

	Go emphasizes explicit error handling through return values, requiring developers to check for errors at each step.
	In contrast, Rust uses the Result type for error propagation, and Python employs exceptions for error handling. */

	/* Go Further (Optional, Strong Signal)
	Try one:
	Use errors.Is
	Add structured logging (log.Printf with context)

	Define a sentinel error (var ErrNotFound = errors.New(...))
	see makeTea above. */
	fmt.Println("\nGo Further — Sentinel Errors and errors.Is")
	for i := 1; i <= 4; i++ {
		err := applyToJob(i)
		if errors.Is(err, ErrDidNotApply) {
			log.Printf("Did not apply error: %v", err)
		} else if errors.Is(err, ErrRejected) {
			log.Printf("Rejected error: %v", err)
		} else if err != nil {
			log.Printf("Other error: %v", err)
		} else {
			fmt.Println("No error for i =", i)
			//			log.Printf("No error for i = %d", i)
		}
	}

	// Explain when panic is acceptable in Go
	/* In Go, panic is acceptable in situations where the program encounters an unrecoverable error,
	such as a critical failure during initialization or a situation that should never occur during normal operation.
	Panic is also used in testing to indicate that a test has failed unexpectedly. */
}
