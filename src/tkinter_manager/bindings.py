from typing import Optional

button_lookup = {
    "Left": "-1",
    "Middle": "-2",
    "Right": "-3",
    "ScrollUp": "-4",
    "ScrollDown": "-5",
}

repetitions_lookup = {
    1: "",
    2: "Double-",
    3: "Triple-",
}

on_lookup = {
    "Start": "Press",
    "End": "Release",
}

special_keys = [
    "Cancel",
    "BackSpace",
    "Tab",
    "Return",
    "Shift_L",
    "Control_L",
    "Alt_L",
    "Pause",
    "Caps_Lock",
    "Escape",
    "Prior",
    "Next",
    "End",
    "Home",
    "Left",
    "Up",
    "Right",
    "Down",
    "Print",
    "Insert",
    "Delete",
    "F1",
    "F2",
    "F3",
    "F4",
    "F5",
    "F6",
    "F7",
    "F8",
    "F9",
    "F10",
    "F11",
    "F12",
    "Num_Lock",
    "Scroll_Lock",
    "Any",
    "Control",
    "Shift",
    "Alt",
]


def return_tag(string: str) -> str:
    return f"<{string}>"


def _return_arg_is_valid(arg):
    is_lower_char = (
        len(arg) == 1 and (arg.isnumeric() is False) and (arg == arg.lower())
    )
    return is_lower_char or arg in special_keys


def keyboard(*args) -> str:
    for arg in args:
        if not _return_arg_is_valid(arg):
            raise Exception(
                f"'{arg}' is neither a special keyword nor a lower-case key."
            )

    return return_tag("-".join(args))


def click(
    button: Optional[str] = "Any",
    on: Optional[str] = None,
    repetitions: Optional[int] = 1,
) -> str:
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
        bind_string = repetitions_lookup[repetitions] + bind_string

    return return_tag(bind_string)


def resized() -> str:
    return return_tag("Configure")
