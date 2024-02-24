from tkinter_manager import TKinterManager

class App(object):
    def __init__(self, manager):
        self.manager = manager
        self.count = 0
        self.recording_progress = False

    def execute(self):
        for name in ['category', 'username', 'notes']:
            element = self.manager.get_element(name)
            print(f"{name}: {element.get()}")

        food_container = self.manager.get_element("food_order")
        for value in food_container.get_selected():
            print(f"Checkbox: {value}")
            
        drinks_container = self.manager.get_element("drinks_order")
        value = drinks_container.get_selected()
        print(f"Radio: {value}")

        if self.recording_progress:
            self.manager.get_element("progress_bar").stop()
            self.recording_progress = False
        else:
            self.manager.get_element("progress_bar").start()
            self.recording_progress = True

    def update_count(self):
        self.count += 1
        message = f"Count: {self.count}"
        self.manager.get_element("message_box").set(message)
        self.manager.root.after(1000, self.update_count)

    def set_manager(self, manager):
        self.manager = manager

manager = TKinterManager(
    title="This is the title"
)
app = App(manager)

manager.add_element(
	element_name='category',
	element_type='dropdown',
    values=['A', 'B', 'C']
)
manager.add_element(
	element_name='username',
	element_type='text_input',
)
manager.add_element(
	element_name='notes',
	element_type='text_input',
	label_text='Enter notes'
)
manager.add_element(
	element_name='food_order',
	element_type='checkboxes',
	values=['Fish', 'Chips', 'Tomato Sauce']
)
manager.add_element(
	element_name='drinks_order',
	element_type='radio_buttons',
    values=['Tea', 'Coffee', 'Milo']
)
manager.add_element(
	element_name='message_box',
	element_type='label',
)
manager.add_element(
	element_name='progress_bar',
	element_type='progress_bar',
)
manager.add_element(
	element_name='start_button',
	element_type='button',
	hook_function=app.execute
)
# layout = [
#     ["category_label", "category",],
#     ["username_label", "username"],
#     ["notes_label", "notes"],
#     [None, "start_button"],
# ]
# manager.set_layout(layout)
manager.centre_elements()
app.update_count()
manager.run()