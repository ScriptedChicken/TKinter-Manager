from .tkinter_element import TKinterElement
from tkinter.ttk import Checkbutton
from tkinter import StringVar


class CheckboxManager(TKinterElement):
    def __init__(self, root, element_name: str, value: str) -> None:
        self.state = StringVar()
        TKinterElement.__init__(
            self, element_name, Checkbutton(root, text=value, variable=self.state)
        )

    def get(self) -> None:
        return self.state.get()

    def set(self, value: str) -> None:
        self.state.set(value)
