from tkinter import *
from tkinter import ttk

root = Tk()

# create entries
entry = ttk.Entry(root, width=30)
entry2 = ttk.Entry(root, width=30)

# create placeholder
entry.insert(0, "Please enter your name")
entry2.insert(0, "Please enter your password")

# create buttons and labels
button = ttk.Button(root, text="Enter")
lbl_title= ttk.Label(text="Our Title Here", font=("Arial", 22))
lbl_name = ttk.Label(text="Your Name: ")
lbl_pass = ttk.Label(text="Your Password")

# Position of the buttons, labels and entries
lbl_title.grid(row=0, column=0)
lbl_name.grid(row=1, column=0)
lbl_pass.grid(row=2, column=0)

entry.grid(row=1, column=1)
entry2.grid(row=2, column=1)
button.grid(row=3, column=1)

root.geometry("500x450")
root.mainloop()