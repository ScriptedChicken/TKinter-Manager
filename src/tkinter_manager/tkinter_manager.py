from tkinter import Tk, Menu
from .label_manager import LabelManager
from .button_manager import ButtonManager
from .dropdown_manager import DropdownManager
from .text_input_manager import TextInputManager
from .layout_manager import LayoutManager
from .progress_bar_manager import ProgressBarManager
from .container_manager import ContainerManager
from typing import Any, Union, List, Callable, Tuple, Literal, Optional


class TKinterManager(object):
    """The main class in the TKinter Manager. Controls all of the high-level creation, retrieval, and execution of the application.

    Args:
        title: The title of the application.
        width: The width of the application.
        height: The height of the application.
    """

    def __init__(self, title: str, width: int = None, height: int = None) -> None:
        self.root = Tk()
        self.root.title(title)
        if width and height:
            self.root.geometry(f"{width}x{height}")
        self.elements_dict = {}
        self.layout_manager = LayoutManager(self.root)
        self.menubar = None

    def run(self) -> None:
        """Runs the application."""
        self.root.mainloop()

    def add_element(
        self,
        element_name: str,
        element_type: Literal[
            "button",
            "dropdown",
            "text_input",
            "progress_bar",
            "label",
            "checkboxes",
            "radio_buttons",
        ],
        label_text: Optional[str] = None,
        hook_function: Optional[Callable] = None,
        values: Optional[str] = None,
    ) -> None:
        """Allows a GUI element to be added to the application.

        Args:
            element_name: The name of the element. Must be unique.
            element_type: The type of the element.
            label_text: Label text, if desired.
            hook_function: The function to apply to 'button' elements.
            values: A list of value to apply to 'checkboxes' or 'radio_buttons' elements.
        """
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
        """Adds a menu if one doesn't exist already. Adds a menu group.

        Args:
            group_name: The name of the menu group.
            group_config: A list of (command_name:str, command:Callable, shortcut:Optional[str]) to add to the menu group.
        """
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
        """Removes a menu and all of its groups from the application."""
        self.root.config(menu=None)
        self.menubar = None

    def get_element(self, element_name: str) -> Any:
        """Returns an element by name."""
        return self.elements_dict[element_name]

    def centre_elements(self) -> None:
        """Centres all elements."""
        self.layout_manager.centre_elements(self.elements_dict)

    def set_layout(self, layout_schema: List[List[str]]) -> None:
        """Sets a layout explicitly by using a layout schema.

        Args:
            layout_schema: A nested list of element names."""
        self.layout_manager.set_layout(layout_schema, self.elements_dict)
