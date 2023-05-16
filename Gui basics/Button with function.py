from tkinter import *

root = Tk()
root.title("Buttons")


# making function
def callback():
    label.config(text="You clicked me!", fg="red", bg="yellow")
    button["state"] = "disabled"  # disabling the button


# creating the label
label = Label(root, text="Hello python")
label.pack()

# creating button with command
button = Button(root, text="Click Me!", command=callback)

button.pack()

root.geometry("400x400")
root.mainloop()
