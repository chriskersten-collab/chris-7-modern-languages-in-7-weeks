def convert_to_int(value: str) -> int:
    """Convert a string to int or raise ValueError."""
    return int(value)


def validate_applications(count: int) -> None:
    """Validate application count."""
    if count < 0:
        raise ValueError("Application count cannot be negative")
