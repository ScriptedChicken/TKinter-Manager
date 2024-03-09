from .tkinter_element import TKinterElement
from tkinter.ttk import Radiobutton
from datatypes import InputValue
from tkinter import Tk, StringVar


class RadioButtonManager(TKinterElement):
    def __init__(
        self, root: Tk, element_name: str, value: InputValue, state: StringVar
    ) -> None:
        TKinterElement.__init__(
            self, element_name, Radiobutton(root, text=value, value=value, var=state)
        )

    def get(self) -> None:
        return self.element_object.get()
