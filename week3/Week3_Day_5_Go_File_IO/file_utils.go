package main

import (
	"encoding/json"
	"fmt"
	"os"
)

func readFileToString(path string) (string, error) {
	data, err := os.ReadFile(path)
	if err != nil {
		return "", err
	}
	return string(data), nil
}

func appendLine(path, line string) error {
	f, err := os.OpenFile(path, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		return err
	}
	defer f.Close()
	_, err = f.WriteString(line + "\n")
	return err
}

/*
	Exercise 1 — Write a File

Write study_log.txt containing:
Your name,
Today’s date,
Hours studied today.
*/
func writeStudyLog() {
	fmt.Println("Exercise 1 — Write a File")
	content := []byte("Your name: Chris\nToday's Date: 2026-Jan-03\nHours studied today: 2\n")
	err := os.WriteFile(studyLogPath, content, 0644)
	if err != nil {
		fmt.Println("Error writing file:", err)
		return
	}
	fmt.Println("File written successfully")
}

/*
	Exercise 2 — Read the File

Read study_log.txt and print its contents.
data, err := os.ReadFile("study_log.txt")
*/
func readStudyLog() {
	fmt.Println("\nExercise 2 — Read the File")
	contents, err := readFileToString(studyLogPath)
	if err != nil {
		fmt.Println("Error: err")
		return
	}
	fmt.Println(contents)
}

/*
	Exercise 3 — Append Instead of Overwrite

Append a new line to study_log.txt without deleting existing content.
💡 Hint:
os.OpenFile("file.txt", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
*/
func appendStudyLog() {
	fmt.Println("Exercise 3 — Append Instead of Overwrite")
	if err := appendLine(studyLogPath, "New line appended"); err != nil {
		fmt.Println("Append failed:", err)
	}
	fmt.Println("New line appended successfully")
}

/*
	Exercise 4 — Write CSV-Style Data

Write this to applications.csv:
company,applications_sent,response
OpenAI,3,true
Google,2,false
*/
func writeCSV() {
	fmt.Println("\nExercise 4 — Write CSV-Style Data")
	csvcontent := []byte("company,applications_sent,response\nOpenAI,3,true\nGoogle,2,false\n")
	csverr := os.WriteFile(applicationsPath, csvcontent, 0644)
	if csverr != nil {
		fmt.Println("Error writing file:", csverr)
		return
	}
	fmt.Println("File written successfully")
}

/*
	Exercise 4 — Read CSV-Style Data

Read the data written to applications.csv and print it
*/
func readCSV() {
	fmt.Println("Exercise 4 — Read CSV-Style Data")
	csvdata, csverr := os.ReadFile(applicationsPath)
	if csverr != nil {
		fmt.Println("Error reading file:", csverr)
		return
	}
	fmt.Println(string(csvdata))
}

/* Use encoding/json to write JSON */
func writeJSON() {
	fmt.Println("Use encoding/json to write JSON")
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
	jsonFile, jsonErr := os.Create(jsonPath)
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
}

/*
Use encoding/json to write JSON
*/
func readJSON() {
	fmt.Println("Use encoding/json to read JSON")
	type Application struct {
		Company          string `json:"company"`
		ApplicationsSent int    `json:"applications_sent"`
		Response         bool   `json:"response"`
	}

	/* apps := []Application{
		{Company: "OpenAI", ApplicationsSent: 3, Response: true},
		{Company: "Google", ApplicationsSent: 2, Response: false},
	} */

	// Read from JSON file
	jsonData, jsonErr := os.ReadFile(jsonPath)
	if jsonErr != nil {
		fmt.Println("Error reading JSON file:", jsonErr)
		return
	}
	fmt.Println(string(jsonData))

}
