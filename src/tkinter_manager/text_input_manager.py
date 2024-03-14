from .tkinter_element import TKinterElement
from tkinter.ttk import Entry


class TextInputManager(TKinterElement):
    """Controls text input elements in a TKinter Manager application.

    Args:
        root: The root of the TKinter Manager application. This is defined automatically by the TKinterManager() class.
        element_name: The unique name of the element.
    """

    def __init__(self, root, element_name: str) -> None:
        TKinterElement.__init__(self, element_name, Entry(root))

    def get(self) -> str:
        return self.element_object.get()
