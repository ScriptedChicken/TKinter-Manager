from .tkinter_element import TKinterElement
from tkinter.ttk import Checkbutton
from tkinter import StringVar, Tk
from datatypes import InputValue


class CheckboxManager(TKinterElement):
    def __init__(self, root: Tk, element_name: str, value: InputValue) -> None:
        self.state = StringVar()
        TKinterElement.__init__(
            self, element_name, Checkbutton(root, text=value, variable=self.state)
        )

    def get(self) -> None:
        return self.state.get()

    def set(self, value: InputValue) -> None:
        self.state.set(value)
