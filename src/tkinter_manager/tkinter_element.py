from typing import Any, Union, Callable

class TKinterElement(object):
    def __init__(self, element_name: str, element_object: Any, hook: Union[Callable, None]=None):
        self.name = element_name
        self.element_object = element_object
        self.hook = hook
