from tkinter import *

root = Tk()

# Creating a label
label = Label(root, text="Hello Python")
label.pack()

# Creating a button(does not have a command so will not do anything)
button = Button(root, text="Click Me!")
button.pack()

root.geometry("400x400")
root.mainloop()  # Run the code