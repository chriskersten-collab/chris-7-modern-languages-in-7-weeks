from pathlib import Path
from datetime import date
# Exercise 1 — Write a File
# Write a file called study_log.txt containing:
# Your name
# Today's date
# Hours studied today
path = Path("study_log.txt")
with open(path, "w") as file:
    file.write("Name: Chris\n")
    file.write("Today's Date:",date.today().isoformat(),"\n")
    file.write("Hours Studied Today: 1\n")

print("Exercise 2 — Read and Print the File")
print("Read the contents of study_log.txt and print them to the console.")
with open(path, "r") as file:
    contents = file.read()
    print(contents)

print("""Exercise 3 — CSV-style Data
Create a list of job applications:
company,applications_sent,response
Write them to applications.csv, then read and print them formatted.""")
my_list_of_applications = [
    "OpenAI,3,True",
    "Google,2,False",
    "Spotify,4,True",
]
path = Path("applications.csv")
with open(path, "w") as file:
    for row in my_list_of_applications:
        file.write(row + "\n")

with open(path, "r") as file:
    for row in file:
        company, applications_sent, response = row.strip().split(",")
        print(f"Company: {company}, Applications Sent: {applications_sent}, Response Received: {response}")
print("them formatted.")

print("""\nExercise 4 — JSON
Create a dictionary representing one job application.
Write it to application.json
Read it back
Print the company name""")
import json
application_json = {
    "company": "OpenAI",
    "applications_sent": 3,
    "response": True
}
path = Path("application.json")
with open(path, "w") as file:
    json.dump(application_json, file, indent=2)
with open(path, "r") as file:
    read_application = json.load(file)
    print("The company name:", read_application["company"])

# Exercise 5 — Comparison (Written)
# In 1–2 sentences, explain:
# Why is JSON preferred over CSV for structured data?
# JSON is preferred over CSV for structured data because JSON can represent complex nested structures and data types 
# (like lists and dictionaries), whereas CSV is limited to flat, tabular data. JSON also includes metadata 
# through key-value pairs, making it easier to understand the context of the data.

print("""\nGo Further (Optional, Strong Signal)
Try one:
Use pathlib.Path everywhere (done!)
Append multiple logs to the same file
Handle a missing file with try/except""")
path = Path("logfile.txt")
with open(path, "w") as file:
    file.write("What rolls down stairs\n")
with open(path, "a") as file:
    file.write("alone or in pairs\n")
with open(path, "a") as file:
    file.write("""and over your neighbor's dog?
What's great for a snack,
And fits on your back?
It's log, log, log
It's log, it's log,
It's big, it's heavy, it's wood.
It's log, it's log, it's better than bad, it's good."
Everyone wants a log
You're gonna love it, log
Come on and get your log
Everyone needs a log
log log log          
""")
try:
    no_such_path = Path("non_existent_file.txt")
    with open(no_such_path, "r") as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print("File not found:", no_such_path, "does not exist.")