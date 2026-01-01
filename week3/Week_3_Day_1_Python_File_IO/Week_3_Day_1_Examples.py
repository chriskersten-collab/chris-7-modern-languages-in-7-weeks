# Example 1: Reading a log or notes file
with open("notes.txt", "r") as file:
    contents = file.read()

print("\nExample 1: Contents of notes.txt:")
print(contents)

print("\nAnother example 1: Reading a log or notes file line by line")
with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())

# Example 2: Writing to a file
with open("output.txt", "w") as file:
    file.write("This is a sample output file.\n")
    file.write("It contains multiple lines of text.\n")
print("\nExample 2: Wrote to output.txt")

print("Another example 2: Appending to a file")
with open("output.txt", "a") as file:
    file.write("This line was appended to the file.\n")

print("\nExample 3. Working with Structured Data (CSV-style)")
applications = [
    "OpenAI,12,True",
    "Google,5,False",
    "Microsoft,8,True",
]
with open("applications.csv", "w") as file:
    for row in applications:
        file.write(row + "\n")
print("Wrote applications to applications.csv")
print("More of example 3: Reading it back")
with open("applications.csv", "r") as file:
    for line in file:
        company, applications_sent, response = line.strip().split(",")
        print("Company:", company, "Applications Sent:", int(applications_sent), "Response Received:", response == "True")

print("\nExample 4. JSON — Most Important Format")
import json
application = {
    "company": "OpenAI",
    "applications_sent": 12,
    "response": True
}
with open("application.json", "w") as file:
    json.dump(application, file, indent=2)
with open("application.json", "r") as file:
    data = json.load(file)
print("Read from application.json:", data)

# Example 5. File Paths (Important!)
# same folder
with open("data.txt") as file:
    data = file.read()
# Subfolder
with open("data/applications.txt") as file:
    data = file.read()
# Cross-platform safe paths
from pathlib import Path
path = Path("data") / "applications.txt"
with open(path) as file:
    print(file.read())