from tkinter_element import TKinterElement
from tkinter.ttk import Label
from utils import return_clean_text

class LabelManager(TKinterElement):
    def __init__(self, root, element_name):
        TKinterElement.__init__(self, element_name, Label(root))

    def set(self, input_text, clean_text=False):
        if clean_text:
            input_text = return_clean_text(input_text)
        self.element_object.config(text=input_text)

    def get(self):
        return self.element_object.cget('text')