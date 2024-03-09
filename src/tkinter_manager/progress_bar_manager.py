from .tkinter_element import TKinterElement
from tkinter.ttk import Progressbar
from datatypes import Root, Number


class ProgressBarManager(TKinterElement):
    def __init__(self, root: Root, element_name: str) -> None:
        TKinterElement.__init__(self, element_name, Progressbar(root))

    def get(self, decimal_places: int = 0) -> None:
        return round(self.element_object["value"], decimal_places)

    def set(self, value: Number) -> None:
        self.element_object["value"] = int(value) / 100

    def start(self) -> None:
        self.element_object.start()

    def stop(self) -> None:
        self.element_object.stop()
