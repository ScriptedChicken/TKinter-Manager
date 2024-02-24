from tkinter_manager import TKinterManager

class App(object):
    def __init__(self, manager):
        self.manager = manager
        self.count = 0
        self.recording_progress = False

    def execute(self):
        for name in ['Category', 'Username', 'Notes']:
            element = self.manager.get_element(name)
            print(f"{name}: {element.get()}")

        food_container = self.manager.get_element("Food Order")
        for value in food_container.get_selected():
            print(f"Checkbox: {value}")

        drinks_container = self.manager.get_element("Drinks Order")
        value = drinks_container.get_selected()
        print(f"Radio: {value}")

        if self.recording_progress:
            self.manager.get_element("Progress Bar").stop()
            self.recording_progress = False
        else:
            self.manager.get_element("Progress Bar").start()
            self.recording_progress = True

    def update_count(self):
        self.count += 1
        message = f"Count: {self.count}"
        self.manager.get_element("Message Box").set(message)
        self.manager.root.after(1000, self.update_count)

    def set_manager(self, manager):
        self.manager = manager

manager = TKinterManager(
    title="This is the title"
)
app = App(manager)

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
	element_name='Food Order',
	element_type='checkboxes',
	values=['Fish', 'Chips', 'Tomato Sauce']
)
manager.add_element(
	element_name='Drinks Order',
	element_type='radio_buttons',
    values=['Tea', 'Coffee', 'Milo']
)
manager.add_element(
	element_name='Message Box',
	element_type='label',
)
manager.add_element(
	element_name='Progress Bar',
	element_type='progress_bar',
)
manager.add_element(
	element_name='Start Button',
	element_type='button',
	hook_function=app.execute
)
manager.centre_elements()
app.update_count()
manager.run()