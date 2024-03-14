def return_clean_text(input_text: str) -> str:
    """Returns a formatted string."""
    return input_text.replace("_", " ").capitalize()
