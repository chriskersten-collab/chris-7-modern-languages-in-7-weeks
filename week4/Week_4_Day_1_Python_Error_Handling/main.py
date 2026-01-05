from pathlib import Path

from file_utils import read_file_safe
from validation import convert_to_int, validate_applications


def main() -> None:
    print("\nExercise 1 — Safe File Read")
    file_path = Path("study_log.txt")

    try:
        contents = read_file_safe(file_path)
    except FileNotFoundError as e:
        print(e)
    else:
        print(f"File contents:\n{contents}")

    print("\nExercise 2 — Numeric Input Validation")
    hours = "five"

    try:
        hours_int = convert_to_int(hours)
        print("Converted hours:", hours_int)
    except ValueError:
        print("Cannot convert input to an integer.")

    print("\nExercise 4 — Raise Your Own Error")
    try:
        validate_applications(-3)
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
