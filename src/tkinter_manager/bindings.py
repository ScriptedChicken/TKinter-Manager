from typing import Optional, Literal
from json import load
from os.path import join, dirname

with open(join(dirname(__file__), "config", "resources.json"), "r") as file:
    resources = load(file)
    special_keys = resources.get("special_keys")
    on_lookup = resources.get("on_lookup")
    button_lookup = resources.get("button_lookup")
    repetitions_lookup = resources.get("repetitions_lookup")
    del resources


def return_tag(string: str) -> str:
    """Returns an bind string as a tag.

    Args:
        string: A valid TKinter bind string.

    Returns:
        A valid TK bind tag."""
    return f"<{string}>"


def _return_arg_is_valid(arg: str) -> bool:
    """Returns whether an keyboard argument is a valid lower-case character or a TKinter special key.

    Args:
        arg: A string that represents a key on a keyboard.

    Returns:
        Whether the input argument is valid."""
    is_lower_char = (
        len(arg) == 1 and (arg.isnumeric() is False) and (arg == arg.lower())
    )
    return is_lower_char or arg in special_keys


def keyboard(*args: str) -> str:
    """Returns a TKinter tag for binding.

    Args:
        *args: Takes any number of strings that represent keys on a keyboard.

    Returns:
        A TKinter tag. (eg: <modifier-modifier-type-detail>)
    """
    for arg in args:
        if not _return_arg_is_valid(arg):
            raise Exception(
                f"'{arg}' is neither a special keyword nor a lower-case key."
            )

    return return_tag("-".join(args))


def click(
    button: Literal["Any", "Left", "Right", "Middle", "ScrollUp", "ScrollDown"] = "Any",
    on: Literal["Start", "End", None] = None,
    repetitions: Literal[1, 2, 3] = 1,
) -> str:
    """Returns a command string for the TKinter .bind() method.

    Args:
        button:  Which mouse button to bind the event to.
        on: Specifies on the start of a click, on the end, or just on a click.
        repetitions: Number of clicks. Value cannot be lower than 1 or higher that 3.

    Returns:

    """
    bind_string = "Button"

    if on:
        if repetitions != 1:
            raise ArithmeticError("Cannot specify start or end with repetitions.")

        on_options = list(on_lookup.keys())
        if on in on_options:
            bind_string += on_lookup[on]
        else:
            raise LookupError(f"'{on}' is not one of {on_options}")

    if button != "Any":
        bind_string += button_lookup[button]

    if repetitions < 1 or repetitions > 3:
        raise ArithmeticError(
            "Number of click repetitions must be greater than 0 and less than 4."
        )
    else:
        bind_string = repetitions_lookup[str(repetitions)] + bind_string

    return return_tag(bind_string)


def resized() -> str:
    """Returns the command string for binding an event to a window resize event.

    Returns:
        <Configure>"""
    return return_tag("Configure")
