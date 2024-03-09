from typing import Optional
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
        bind_string = repetitions_lookup[str(repetitions)] + bind_string

    return return_tag(bind_string)


def resized() -> str:
    return return_tag("Configure")
