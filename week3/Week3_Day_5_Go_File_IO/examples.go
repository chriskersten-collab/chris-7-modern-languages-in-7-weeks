package main

import (
	"fmt"
	"os"
)

func main() {
	fmt.Println("Example 1 — Write a File")
	content := []byte("Name:Chris\nDate:2026-Jan-03\nHours studied:2\n")
	err := os.WriteFile("study_log.txt", content, 0644)
	if err != nil {
		fmt.Println("Error writing file:", err)
		return
	}
	fmt.Println("File written successfully")

	fmt.Println("\nExample 2 — Read a File")
	data, err := os.ReadFile("study_log.txt")
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}
	fmt.Println(string(data))

	fmt.Println("\nExample 3 - Safe Error Handling (Missing File)")
	data, err = os.ReadFile("does_not_exist.txt")
	if err != nil {
		fmt.Println("Handled error:", err)
	} else {
		fmt.Println(string(data))
	}
}
