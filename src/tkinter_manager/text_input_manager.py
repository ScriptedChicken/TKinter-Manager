from .tkinter_element import TKinterElement
from tkinter.ttk import Entry


class TextInputManager(TKinterElement):
    def __init__(self, root, element_name: str) -> None:
        TKinterElement.__init__(self, element_name, Entry(root))

    def get(self) -> str:
        return self.element_object.get()
