from .tkinter_element import TKinterElement
from tkinter.ttk import Progressbar


class ProgressBarManager(TKinterElement):
    """Controls progress bars in a TKinter Manager application.

    Args:
        root: The root of the TKinter Manager application. This is defined automatically by the TKinterManager() class.
        element_name: The unique name of the element.
    """

    def __init__(self, root, element_name: str) -> None:
        TKinterElement.__init__(self, element_name, Progressbar(root))

    def get(self, decimal_places: int = 0) -> float:
        return round(self.element_object["value"], decimal_places)

    def set(self, value: int) -> None:
        self.element_object["value"] = int(value) / 100

    def start(self) -> None:
        """Starts the progress bar."""
        self.element_object.start()

    def stop(self) -> None:
        """Stops the progress bar."""
        self.element_object.stop()
