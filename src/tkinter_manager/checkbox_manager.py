from .tkinter_element import TKinterElement
from tkinter.ttk import Checkbutton
from tkinter import StringVar


class CheckboxManager(TKinterElement):
    """Controls a checkbox in a TKinter Manager application.

    Args:
        root: The root of the TKinter Manager application. This is defined automatically by the TKinterManager() class.
        element_name: The unique name of the element.
        value: The value to assign to the checkbox.
    """

    def __init__(self, root, element_name: str, value: str) -> None:
        self.state = StringVar()
        TKinterElement.__init__(
            self, element_name, Checkbutton(root, text=value, variable=self.state)
        )

    def get(self) -> None:
        return self.state.get()

    def set(self, value: str) -> None:
        self.state.set(value)
