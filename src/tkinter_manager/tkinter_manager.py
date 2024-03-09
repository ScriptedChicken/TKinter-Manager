from tkinter import Tk, Menu
from .label_manager import LabelManager
from .button_manager import ButtonManager
from .dropdown_manager import DropdownManager
from .text_input_manager import TextInputManager
from .layout_manager import LayoutManager
from .progress_bar_manager import ProgressBarManager
from .container_manager import ContainerManager
from typing import Any, Union, List, Callable, Tuple


class TKinterManager(object):
    def __init__(self, title: str, width: int = None, height: int = None) -> None:
        self.root = Tk()
        self.root.title(title)
        if width and height:
            self.root.geometry(f"{width}x{height}")
        self.elements_dict = {}
        self.layout_manager = LayoutManager(self.root)
        self.menubar = None

    def run(self) -> None:
        self.root.mainloop()

    def add_element(
        self,
        element_name: str,
        element_type: Any,
        label_text: str = None,
        hook_function: Union[Callable, None] = None,
        values: List[str] = None,
    ) -> None:
        is_duplicate_element = element_name in self.elements_dict
        if is_duplicate_element:
            raise Exception(
                f"Multiple elements with name of '{element_name}' - rename your elements so they are unique."
            )

        label_name = f"{element_name}_label"
        label = LabelManager(self.root, label_name)

        if label_text:
            label.set_text(label_text)
            self.elements_dict[label_name] = label

        if element_type == "button":
            element = ButtonManager(self.root, element_name, hook_function)

        elif element_type == "dropdown":
            element = DropdownManager(self.root, element_name, values)

        elif element_type == "text_input":
            element = TextInputManager(self.root, element_name)

        elif element_type == "progress_bar":
            element = ProgressBarManager(self.root, element_name)

        elif element_type == "label":
            element = LabelManager(self.root, element_name)

        elif element_type in ["checkboxes", "radio_buttons"]:
            element = ContainerManager(self.root, element_name, element_type, values)

        self.elements_dict[element_name] = element

    def add_menu_group(
        self, group_name: str, group_config=List[Tuple[str, Callable, str]]
    ) -> None:
        if not self.menubar:
            self.menubar = Menu(self.root)

        menu = Menu(self.menubar, tearoff=0)
        for name, command, shortcut in group_config:
            menu.add_command(label=name, command=command)
            if shortcut:
                self.root.bind_all(shortcut, command)

        self.menubar.add_cascade(label=group_name, underline=0, menu=menu)
        self.root.config(menu=self.menubar)

    def remove_menu(self) -> None:
        self.root.config(menu=None)
        self.menubar = None

    def get_element(self, element_name: str) -> Any:
        return self.elements_dict[element_name]

    def centre_elements(self) -> None:
        self.layout_manager.centre_elements(self.elements_dict)

    def set_layout(self, layout_schema: List[List[str]]) -> None:
        self.layout_manager.set_layout(layout_schema, self.elements_dict)
