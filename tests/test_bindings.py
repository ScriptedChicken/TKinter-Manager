import pytest
from tkinter import Tk
from src.tkinter_manager.bindings import keyboard, click, resized


def return_true():
    return True


root = Tk()


@pytest.mark.parametrize(
    "args, expected, raises_error",
    [
        pytest.param(["Control", "o"], "<Control-o>", False),
        pytest.param(["Control", "Shift", "f"], "<Control-Shift-f>", False),
        pytest.param(["Any"], "<Any>", False),
        pytest.param(["1", "thaiondw"], "<>", True),
        pytest.param(["1"], "<>", True),
    ],
)
def test_keyboard(args, expected, raises_error):
    if raises_error:
        with pytest.raises(Exception):
            keyboard(*args)
    else:
        result = keyboard(*args)
        assert result == expected
        root.bind_all(result)


@pytest.mark.parametrize(
    "button, on, repititions, expected, error",
    [
        pytest.param("Left", None, 1, "<Button-1>", None),
        pytest.param("Middle", None, 1, "<Button-2>", None),
        pytest.param("Right", None, 1, "<Button-3>", None),
        pytest.param("Other", None, 1, "<Button-3>", LookupError),
        pytest.param("Left", "Start", 1, "<ButtonPress-1>", None),
        pytest.param("Right", "End", 1, "<ButtonRelease-3>", None),
        pytest.param("Right", "Other", 1, "<ButtonRelease-3>", LookupError),
        pytest.param("Middle", None, 2, "<Double-Button-2>", None),
        pytest.param("Right", None, 3, "<Triple-Button-3>", None),
        pytest.param("Right", None, 4, "<Triple-Button-3>", ArithmeticError),
        pytest.param("Middle", "End", 3, "<Triple-ButtonRelease-2>", ArithmeticError),
    ],
)
def test_click(button, on, repititions, expected, error):
    if error:
        with pytest.raises(error):
            click(button, on, repititions)
    else:
        result = click(button, on, repititions)
        assert result == expected
        root.bind_all(result, return_true)
