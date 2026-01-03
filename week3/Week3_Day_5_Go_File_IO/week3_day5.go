package main

import (
	"encoding/json"
	"fmt"
	"os"
)

func main() {
	fmt.Println("Exercise 1 — Write a File")
	/* Write study_log.txt containing:
	Your name
	Today’s date
	Hours studied today */
	content := []byte("Your name: Chris\nToday's Date: 2026-Jan-03\nHours studied today: 2\n")
	err := os.WriteFile("study_log.txt", content, 0644)
	if err != nil {
		fmt.Println("Error writing file:", err)
		return
	}
	fmt.Println("File written successfully")

	fmt.Println("\nExercise 2 — Read the File")
	/* Read study_log.txt and print its contents. */
	data, err := os.ReadFile("study_log.txt")
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}
	fmt.Println(string(data))

	fmt.Println("\nExercise 3 — Append Instead of Overwrite")
	/* Append a new line to study_log.txt without deleting existing content.
	💡 Hint:
	os.OpenFile("file.txt", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644) */
	f, err := os.OpenFile("study_log.txt", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer f.Close()
	_, err = f.WriteString("New line appended\n")
	if err != nil {
		fmt.Println("Error writing to file:", err)
		return
	}
	fmt.Println("File appended successfully")

	fmt.Println("\nExercise 4 — CSV-Style Data")
	/* Write this to applications.csv:
	company,applications_sent,response
	OpenAI,3,true
	Google,2,false
	Then read and print the file. */
	csvcontent := []byte("company,applications_sent,response\nOpenAI,3,true\nGoogle,2,false\n")
	csverr := os.WriteFile("applications.csv", csvcontent, 0644)
	if csverr != nil {
		fmt.Println("Error writing file:", err)
		return
	}
	fmt.Println("File written successfully")
	csvdata, csverr := os.ReadFile("study_log.txt")
	if csverr != nil {
		fmt.Println("Error reading file:", err)
		return
	}
	fmt.Println(string(csvdata))

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
	funcdata, funcerr := printApplications("study_log.txt")
	if funcerr != nil {
		fmt.Println("Error: ", funcerr)
	}
	fmt.Println(funcdata)

	fmt.Println("Use encoding/json to write/read JSON")
	/* Example of using encoding/json to write/read JSON */
	type Application struct {
		Company          string `json:"company"`
		ApplicationsSent int    `json:"applications_sent"`
		Response         bool   `json:"response"`
	}

	apps := []Application{
		{Company: "OpenAI", ApplicationsSent: 3, Response: true},
		{Company: "Google", ApplicationsSent: 2, Response: false},
	}

	// Write to JSON file
	jsonFile, jsonErr := os.Create("applications.json")
	if jsonErr != nil {
		fmt.Println("Error creating JSON file:", jsonErr)
		return
	}
	defer jsonFile.Close()
	encoder := json.NewEncoder(jsonFile)
	jsonErr = encoder.Encode(apps)
	if jsonErr != nil {
		fmt.Println("Error encoding JSON:", jsonErr)
		return
	}
	fmt.Println("JSON file written successfully")

	// Read from JSON file
	jsonData, jsonErr := os.ReadFile("applications.json")
	if jsonErr != nil {
		fmt.Println("Error reading JSON file:", jsonErr)
		return
	}
	fmt.Println(string(jsonData))

	/* Explain why Go avoids exceptions (comment)
	Go avoids exceptions to maintain simplicity and clarity in error handling.
	By using explicit error returns, Go encourages developers to handle errors immediately,
	reducing unexpected control flow and making the code more predictable and easier to debug.
	*/
}

func printApplications(filename string) (string, error) {
	/* return "", errors.err */
	data, err := os.ReadFile(filename)
	if err != nil {
		return "", fmt.Errorf("Error reading file: %v", err)
	}
	return string(data), nil

}
