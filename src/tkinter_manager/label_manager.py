from .tkinter_element import TKinterElement
from tkinter.ttk import Label


class LabelManager(TKinterElement):
    def __init__(self, root, element_name: str) -> None:
        TKinterElement.__init__(self, element_name, Label(root))

    def set_text(self, input_text: str) -> None:
        """Sets the text in the label."""
        self.element_object.config(text=input_text)

    def get_text(self) -> str:
        """Gets the text in the label."""
        return self.element_object.cget("text")
