from .tkinter_element import TKinterElement
from tkinter.ttk import Label
from tkinter import Tk


class LabelManager(TKinterElement):
    def __init__(self, root: Tk, element_name: str) -> None:
        TKinterElement.__init__(self, element_name, Label(root))

    def set(self, input_text: str) -> None:
        self.element_object.config(text=input_text)

    def get(self) -> None:
        return self.element_object.cget("text")
