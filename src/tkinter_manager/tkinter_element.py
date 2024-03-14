from typing import Any, Union, Callable


class TKinterElement(object):
    """Generic TKinter element class.

    Args:
        element_name: The unique name of the element.
        element_object: The parent object.
        hook: The function attached to the element.
    """

    def __init__(
        self, element_name: str, element_object: Any, hook: Union[Callable, None] = None
    ):
        self.name = element_name
        self.element_object = element_object
        self.hook = hook

    def bind(self, event: str, command: Callable) -> None:
        self.element_object.bind(event, command)
