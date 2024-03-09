from .tkinter_element import TKinterElement
from tkinter.ttk import Combobox
from tkinter import Tk
from datatypes import InputValue
from typing import List


class DropdownManager(TKinterElement):
    def __init__(
        self, root: Tk, element_name: str, input_list: List[InputValue]
    ) -> None:
        TKinterElement.__init__(self, element_name, Combobox(root))
        self.set(input_list)

    def set(self, input_values: List[InputValue]) -> None:
        self.element_object["values"] = input_values

    def get(self) -> None:
        return self.element_object.get()
