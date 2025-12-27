# Exercise 1 - variables
name = "Chris"
targetJobRole = "Data Scientist"
numberofHoursPerWeek = 5
print(f"Hi, my name is {name}. I am aiming to become a {targetJobRole} and I can study for {numberofHoursPerWeek} hours every week.")

# Exercise 2 - conditional statements
appsSent = input("How many job applications have you sent this week? ")
if int(appsSent) == 0:
    print(f"You need to start applying!")
elif int(appsSent) < 9: 
    print(f"Good momentum")
else:
    print(f"High volume - track quality" )

# Exercise 3 - Loops and lists
applications = [0, 1, 3, 7, 12]
for app in applications:
    if app == 0:
        print(f"{app} applications is Low")
    elif app == 1:
        print(f"{app} application is Medium")  
    elif app < 9:
        print(f"{app} applications is Medium")  
    else:
        print(f"{app} applications is High")

# Exercise 4 - Automation-Style Task
n = int(input("Enter a number: "))
for i in range(1, n+1):
    if i % 3 == 0 or i % 5 == 0:
        print(f"{i}")

# Exercise 5 - Data Filtering (Job-Relevant)
skills = ["python", "sql", "excel", "git", "aws"]
vowels = ["a","e","i","o","u"]
for skill in skills:
    if len(skill) > 3:
        print(f"{skill} is longer than 3 characters")
    # print(f"{skill} starts with {skill[0]} ")
    if skill[0] in vowels:
        print(f"{skill} starts with a vowel")

# Validate user input (what if it’s not a number?)
try:
    n = int(input("Enter a number: "))
    for i in range(1, n+1):
        if i % 3 == 0 or i % 5 == 0:
            print(f"{i}")
except:
    print("Please enter a valid number.")

# Use enumerate() in a loop
for index, skill in enumerate(skills):
    print(f"Index {index} is {skill}")

# Use continue or break
for skill in skills:
    if skill == "git":
        print("Found git, stopping the search.")
        break
    if skill == "sql":
        print("Found sql, I know just a little of that.")
        continue
    print(f"Checking skill: {skill}")