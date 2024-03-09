from datatypes import ManagerElement, Hook


class TKinterElement(object):
    def __init__(
        self, element_name: str, element_object: ManagerElement, hook: Hook = None
    ) -> None:
        self.name = element_name
        self.element_object = element_object
        self.hook = hook
