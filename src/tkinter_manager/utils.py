def return_clean_text(input_text: str) -> str:
    return input_text.replace("_", " ").capitalize()

def return_bind_event(input_text: str) -> str:
    
    return shortcut.notation