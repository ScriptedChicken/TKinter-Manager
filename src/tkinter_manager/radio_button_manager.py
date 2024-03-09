from .tkinter_element import TKinterElement
from tkinter.ttk import Radiobutton
from tkinter import StringVar


class RadioButtonManager(TKinterElement):
    def __init__(self, root, element_name: str, value: str, state: StringVar) -> None:
        TKinterElement.__init__(
            self, element_name, Radiobutton(root, text=value, value=value, var=state)
        )

    def get(self) -> str:
        return self.element_object.get()
