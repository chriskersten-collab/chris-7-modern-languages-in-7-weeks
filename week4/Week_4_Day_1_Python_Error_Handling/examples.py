print("Example 1: Basic try / except")
try:
    hours = int("five")
except ValueError:
    print("That is not a valid number of hours.")

print("\nExample 2 — Specific Errors")
try:
    with open("non_existent_file.txt") as file:
        content = file.read()
except FileNotFoundError:
    print("The file was not found.")
except PermissionError:
    print("You do not have permission to read this file.")

print("\nExample 3 — else and finally")
try:
    number = int("10")
except ValueError:
    print("Conversion failed.")
else:
    print(f"Conversion succeeded: {number}")
finally:
    print("This always executes.")

print("\nExample 4 — Raising Exceptions")
def validate_hours(hours: int):
    if hours < 0:
        raise ValueError("Hours cannot be negative.")
    return hours
try:
    validate_hours(-5)
except ValueError as e:
    print(f"Validation error: {e}")