from .tkinter_element import TKinterElement
from tkinter.ttk import Entry
from tkinter import Tk


class TextInputManager(TKinterElement):
    def __init__(self, root: Tk, element_name: str) -> None:
        TKinterElement.__init__(self, element_name, Entry(root))

    def get(self) -> None:
        return self.element_object.get()
