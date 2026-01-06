package main

import (
	"fmt"
	"os"
	"strconv"
)

func loadConfig(path string) (string, error) {
	data, err := os.ReadFile(path)
	if err != nil {
		return "", fmt.Errorf("loadConfig failed: %w", err)
	}
	return string(data), nil
}

func readFile(path string) (string, error) {
	data, err := os.ReadFile(path)
	if err != nil {
		return "", err
	}
	return string(data), nil
}

func parseHours(input string) (int, error) {
	hours, err := strconv.Atoi(input)
	if err != nil {
		return 0, err
	}
	return hours, nil
}

// func main() {
func examples() {

	fmt.Println("\nExample 1 — Basic Error Return")
	// See also func parseHours
	first_hours, err := parseHours("5")
	if err != nil {
		fmt.Println("Error:", err)
		return
	}
	fmt.Println("Parsed hours:", first_hours)

	/*
		second_hours, err := parseHours("five")
		if err != nil {
			fmt.Println("Error:", err)
			return
		}
		fmt.Println("Parsed hours:", second_hours)
	*/

	fmt.Println("\nExample 2 — File Read with Error Handling")
	// See also func readFile
	first_content, err := readFile("example2data.txt")
	if err != nil {
		fmt.Println("Failed to read file:", err)
		return
	}
	fmt.Println(first_content)

	second_content, err := readFile("missing.txt")
	if err != nil {
		fmt.Println("Failed to read file:", err)
		return
	}
	fmt.Println(second_content)

	/* Example 3 — Wrapping Errors (Best Practice)
	see func loadConfig */

}
