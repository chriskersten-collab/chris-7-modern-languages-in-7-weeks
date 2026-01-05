print("\nExercise 1 — Safe File Read")
# Try to read study_log.txt.
# If it exists → print contents
# If not → print a friendly message
try:
    with open("study_log.txt") as file:
        content = file.read()
except FileNotFoundError:
    print("The file was not found.")
else:
    print(f"File contents:\n{content}")

print("\nExercise 2 — Numeric Input Validation")
# Given:
hours = "five"
# Try to convert to int.
# Catch the error
# Print a helpful message
try:
    hours_int = int(hours)
except ValueError:
    print("Cannot convert input to an integer. Please enter a valid number.")

print("\nExercise 3 — Multiple Exceptions")
# Simulate:
# A missing file
# A bad integer conversion
# Catch each with a different except block.

def read_and_convert(file_name: str, bad_number: str):
    try:
        with open(file_name) as file:
            data = file.read()
        number = int(bad_number)
    except FileNotFoundError:
        print(f"The file '{file_name}' was not found.")
    except ValueError:
        print(f"Cannot convert '{bad_number}' to an integer.")

file_name = "missing_file.txt"
bad_number = "ten"
read_and_convert(file_name, bad_number)

file_name = "study_log.txt"
bad_number = "ten"
read_and_convert(file_name, bad_number)

print("\nExercise 4 — Raise Your Own Error")
# Write a function:
# def validate_applications(count: int) -> None:
#     ...
# Rules:
# count < 0 → raise ValueError
# Otherwise → print "Valid count"

def validate_applications(count: int) -> None:
    if count < 0:
        raise ValueError("Application count cannot be negative.")
    print("Valid count")

try:
    validate_applications(-3)
except ValueError as e:
    print(f"Error: {e}")

try:
    validate_applications(3)
except ValueError as e:
    print(f"Error: {e}")

# Exercise 5 — Comparison (Written)
# In 1–2 sentences, explain:
# How does Python’s exception-based error handling differ from Go’s explicit error returns?
# (Add as a comment.)
# In Python, error handling is done using exceptions that can be raised and caught, 
# allowing for a separation of normal code flow and error handling. 
# In contrast, Go uses explicit error returns, 
# where functions return an error value that must be checked by the caller, 
# leading to more verbose but clear error handling.

print("\nGo Further (Optional, Strong Signal)")
# Try one:
# Use else + finally
# Catch Exception as e and log the message
# Show why bare except: is dangerous (comment)

def convert_to_int(input_value: str) -> int:
    try:
        result = int(input_value)
    except Exception as e: # Catch Exception as e and log the message
        print(f"An error occurred: {e}")
    else:
        print(f"Conversion succeeded: {result}")
        return result
    finally:
        print("Execution of convert_to_int is complete.")
# Example usage
print("Use else + finally")
convert_to_int("20")
convert_to_int("twenty")

# Bare except is dangerous because it catches all exceptions,
# including system-exiting exceptions like KeyboardInterrupt,
# which can make debugging difficult and may hide critical errors.
