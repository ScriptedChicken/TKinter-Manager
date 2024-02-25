import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from src.tkinter_manager import TKinterManager

def print_hello():
	print("Hello")

manager = tkinter_manager.TKinterManager("This is the title")
manager.add_element(
	element_name='category',
	element_type='dropdown',
	label_text='Category',
	values=['A', 'B', 'C']
)
manager.add_element(
	element_name='username',
	element_type='text_input',
	label_text='Username'
)
manager.add_element(
	element_name='notes',
	element_type='text_input',
	label_text='Enter notes'
)
manager.add_element(
	element_name='start_button',
	element_type='button',
	hook_function=print_hello
)
manager.centre_elements()
manager.run()