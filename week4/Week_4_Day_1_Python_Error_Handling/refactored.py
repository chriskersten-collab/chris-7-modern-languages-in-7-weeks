from pathlib import Path


# ---------- Helper Functions ----------

def read_file_safe(path: Path) -> str:
    """Read a file and return its contents."""
    try:
        return path.read_text()
    except FileNotFoundError:
        raise FileNotFoundError(f"{path} does not exist")


def convert_to_int(value: str) -> int:
    """Convert a string to int or raise ValueError."""
    return int(value)


def validate_applications(count: int) -> None:
    """Validate application count."""
    if count < 0:
        raise ValueError("Application count cannot be negative")


# ---------- Main Script ----------

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
        print("Cannot convert input to an integer. Please enter a valid number.")

    print("\nExercise 3 — Multiple Exceptions")
    try:
        read_file_safe(Path("missing_file.txt"))
        convert_to_int("ten")
    except FileNotFoundError as e:
        print(e)
    except ValueError:
        print("Invalid number provided")

    print("\nExercise 4 — Raise Your Own Error")
    try:
        validate_applications(-3)
    except ValueError as e:
        print("Error:", e)

    try:
        validate_applications(3)
        print("Valid count")
    except ValueError as e:
        print("Error:", e)

    print("\nGo Further — else + finally")
    try:
        result = convert_to_int("20")
    except ValueError as e:
        print("Conversion failed:", e)
    else:
        print("Conversion succeeded:", result)
    finally:
        print("Conversion attempt complete")


if __name__ == "__main__":
    main()
