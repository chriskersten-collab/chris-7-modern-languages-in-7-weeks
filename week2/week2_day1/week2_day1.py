print("Week 2 Day 1")

# Examples:
print("\nExamples:")

# Lists — Ordered, Mutable Collections
applications = ["OpenAI", "Google", "Amazon"]

applications.append("Microsoft")
applications.remove("Amazon")

print(applications)
print("First application:", applications[0])
print("Total applications:", len(applications))

for company in applications:
    print("Applied to:", company)

# Dictionaries — Records with Meaning (Most Important)
application = {
    "company": "OpenAI",
    "applications_sent": 12,
    "response": True,
}
print(application["company"])
application["response"] = False
application["role"] = "Data Scientist"
for key, value in application.items():
    print(key, "=>", value)

# Sets — Unique Values Only
skills = {"python", "sql", "git", "python"}
print(skills)
skills.add("aws")
skills.discard("git")
required = {"python", "sql", "aws"}
print("Meets requirements:", required.issubset(skills))

# Tuples — Immutable Data
coordinates = (40.7128, -74.0060)
print(coordinates)

# Exercises:
print("\nExercises:")

print("\nExercise 1 — List Basics")
# Create a list of at least 5 companies you’d apply to.
# Add one
# Remove one
# Print the final list
companies_to_apply = ["Apple", "Netflix", "Tesla", "Google", "Spotify"]
companies_to_apply.append("NVIDIA")
companies_to_apply.remove("Tesla")
print(companies_to_apply)

print("\nExercise 2 — Dictionary Records")
# Create a dictionary representing one job application, with:
# company
# role
# applications_sent
# response
# Print each field.
my_job_application = {
    "company": "Google",
    "role": "Data Scientist",
    "applications_sent": 12,
    "response": True,
}
for key, value in my_job_application.items():
    print(key, "=>", value)

print("\nExercise 3 — List of Dictionaries (Real Data Pattern) ")
# Create a list of 3 application dictionaries.
# Loop and print:
# company name
# response status
# (This pattern appears everywhere in data work.)
list_of_dictionaries = [
    {"company": "NVIDIA", "response": True},
    {"company": "Google", "response": False},
    {"company": "Apple", "response": True},
]
for app in list_of_dictionaries:
    print(app["company"], "=>", app["response"])
    for key, value in app.items():
        print(key, "=>", value)
        

print("\nExercise 4 — Sets for Skills")
# Create a set of skills.
# Add a duplicate
# Show that it only appears once
# Check if a required skills set is satisfied
my_skills = {"python", "sql", "git"}
print(my_skills)
my_skills.add("aws")
my_skills.add("python")  # duplicate
print(my_skills)
my_skills.discard("git")
required = {"python", "sql", "aws"}
print("Meets requirements:", required.issubset(my_skills))

# Exercise 5 — Tuple Safety (Written)
# In 1–2 sentences, explain: Why would you use a tuple instead of a list?
# Tuples are immutable, making them suitable for fixed data structures 
# like coordinates or database records where you want to prevent 
# accidental modification.

# Go Further (Optional)
# Try one:
# Convert a list to a set to remove duplicates
# Use dict.get() safely
# Sort a list of dictionaries by a key

# Convert a list to a set to remove duplicates
duplicate_list = ["python", "sql", "git", "python", "aws"]
unique_set = set(duplicate_list)
print("\nUnique set:", unique_set)

# Use dict.get() safely
my_dictionary_example = {
    "company": "Google",
    "role": "Data Scientist",
    "applications_sent": 12,
    "response": True,
}
print("\nUsing dict.get() safely:")
print(my_job_application.get("location", "Remote from anywhere in the world"))

print("\nSort a list of dictionaries by a key")
list_of_dictionaries = [
    {"company": "NVIDIA", "response": True},
    {"company": "Google", "response": False},
    {"company": "Apple", "response": True},
]
sorted_data = sorted(list_of_dictionaries, key=lambda x: x["company"])
print(sorted_data)