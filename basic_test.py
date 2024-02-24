from tkinter import *

def print_var(*_):
    print(option.get())

root = Tk()
root.geometry("400x400")

option = StringVar()
R1 = Radiobutton(root, text="MALE", value="male", var=option)
R2 = Radiobutton(root, text="FEMALE", value="female", var=option)
R1.pack()
R2.pack()

option.trace_add('write', print_var)

root.mainloop()