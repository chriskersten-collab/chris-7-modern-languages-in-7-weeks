package main

import (
	"fmt"
	"os"
)

const (
	studyLogPath     = "study_log.txt"
	applicationsPath = "applications.csv"
	jsonPath         = "applications.json"
)

func main() {
	writeStudyLog()
	readStudyLog()
	appendStudyLog()
	writeCSV()
	readCSV()

	/* Exercise 5 — Comparison (Written)
	In 1–2 sentences, explain:
	How does Go’s file I/O model compare to Rust’s in terms of safety and complexity?
	(Add this as a comment.)
	Go's file I/O prioritizes developer speed and simplicity with simpler error handling (multi-return)
	and built-in concurrency (goroutines), making it great for I/O-bound services,
	while Rust offers superior compile-time safety via its ownership model and explicit error handling (Result, Option),
	demanding more upfront effort but preventing whole classes of bugs,
	making it ideal for performance-critical systems where correctness is paramount,
	though its I/O code can become more verbose. */

	/* Go Further (Optional, Strong Signal)
	Try one:
	Write a function that returns (string, error)
	Use encoding/json to write/read JSON
	Explain why Go avoids exceptions (comment) */

	fmt.Println("Go Further (Optional, Strong Signal): Write a function that returns (string, error)")
	/* See printApplications function below. Also including code to use the function. */
	funcdata, funcerr := printApplications(studyLogPath)
	if funcerr != nil {
		fmt.Println("Error: ", funcerr)
	}
	fmt.Println(funcdata)

	writeJSON()
	readJSON()

}

func printApplications(filename string) (string, error) {
	/* return "", errors.err */
	data, err := os.ReadFile(filename)
	if err != nil {
		return "", fmt.Errorf("Error reading file: %v", err)
	}
	return string(data), nil

}
