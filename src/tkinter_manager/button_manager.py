from .tkinter_element import TKinterElement
from tkinter.ttk import Button
from .utils import return_clean_text
from typing import Union, Callable


class ButtonManager(TKinterElement):
    def __init__(
        self, root, element_name: str, hook_function: Union[Callable, None]
    ) -> None:
        TKinterElement.__init__(
            self, element_name, Button(root, text=return_clean_text(element_name))
        )
        self.set_hook(hook_function)

    def set_hook(self, input_function: Union[Callable, None]) -> None:
        self.element_object.configure(command=input_function)
