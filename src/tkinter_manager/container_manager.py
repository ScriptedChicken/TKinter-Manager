from .tkinter_element import TKinterElement
from tkinter.ttk import Frame
from tkinter import StringVar
from .checkbox_manager import CheckboxManager
from .radio_button_manager import RadioButtonManager
from typing import List, Union, Any, Literal


class ContainerManager(TKinterElement):
    """Controls the container that wraps checkboxes and radio buttons in a TKinter Manager application..

    Args:
        root: The root of the TKinter Manager application. This is defined automatically by the TKinterManager() class.
        element_name: The unique name of the element.
        children_type: The type of the child elements contained by the widget.
        values: The values to assign to the child elements.
    """

    def __init__(
        self,
        root,
        element_name: str,
        children_type: Literal["checkboxes", "radio_buttons"],
        values: List[str],
    ) -> None:
        self.root = root
        self.children_type = children_type
        self.children_dict = {}
        TKinterElement.__init__(self, element_name, Frame(root))
        self.set(values)

    def get(self, checkbox_name: str) -> Union[CheckboxManager, RadioButtonManager]:
        """Gets the child object value of the container."""
        return self.children_dict[checkbox_name]

    def set(self, values: Any) -> None:
        """Sets the child object values of the container."""
        if self.children_type == "checkboxes":
            for value in values:
                child_name = f"{value}_checkbox"
                child = CheckboxManager(self.element_object, child_name, value)

                self.children_dict[value] = child
                child.element_object.pack()

        elif self.children_type == "radio_buttons":
            self.state = StringVar()
            for value in values:
                child_name = f"{value}_radio_button"
                child = RadioButtonManager(
                    self.element_object, child_name, value, self.state
                )

                self.children_dict[value] = child
                child.element_object.pack()

    def get_children_names(self) -> List[str]:
        """Gets names of children objects."""
        return list(self.children_dict.keys())

    def get_selected(self) -> Union[List[str], str]:
        """Returns the value(s) of the child objects."""
        if self.children_type == "checkboxes":
            selected_values = []
            for child_name, child in self.children_dict.items():
                is_selected = child.get()
                if is_selected:
                    selected_values.append(child_name)
            return selected_values
        elif self.children_type == "radio_buttons":
            return self.state.get()
