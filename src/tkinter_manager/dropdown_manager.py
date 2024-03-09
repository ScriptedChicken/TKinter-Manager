from .tkinter_element import TKinterElement
from tkinter.ttk import Combobox
from typing import List


class DropdownManager(TKinterElement):
    def __init__(self, root, element_name: str, input_values: List[str]) -> None:
        TKinterElement.__init__(self, element_name, Combobox(root))
        self.set(input_values)

    def set_values(self, input_values: List[str]) -> None:
        self.element_object["values"] = input_values

    def get_values(self) -> str:
        return self.element_object.get()
