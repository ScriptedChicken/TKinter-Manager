from tkinter_manager import TKinterManager

class App(object):
    def __init__(self):
        pass

    def execute(self):
        print("Hello, world!")

app = App()
manager = TKinterManager("This is the title")
manager.add_element(
	element_name='Category',
	element_type='dropdown',
    values=['A', 'B', 'C']
)
manager.add_element(
	element_name='Username',
	element_type='text_input',
)
manager.add_element(
	element_name='Notes',
	element_type='text_input',
	label_text='Enter notes'
)
manager.add_element(
	element_name='Start Button',
	element_type='button',
	hook_function=app.execute
)
manager.centre_elements()
manager.run()