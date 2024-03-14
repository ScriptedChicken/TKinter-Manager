from .tkinter_element import TKinterElement
from tkinter.ttk import Radiobutton
from tkinter import StringVar


class RadioButtonManager(TKinterElement):
    """Controls radio buttons in a TKinter Manager application.

    Args:
        root: The root of the TKinter Manager application. This is defined automatically by the TKinterManager() class.
        element_name: The unique name of the element.
        value: The value to assign to the checkbox.
        state: The variable tracking which radio button is selected.
    """

    def __init__(self, root, element_name: str, value: str, state: StringVar) -> None:
        TKinterElement.__init__(
            self, element_name, Radiobutton(root, text=value, value=value, var=state)
        )

    def get(self) -> str:
        return self.element_object.get()
