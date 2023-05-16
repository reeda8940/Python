import tkinter as tk
from tkinter import ttk

root = tk.Tk()
my_boolean_var = tk.BooleanVar()

my_checkButton = ttk.Checkbutton(
    text="Check when the option is True"
)
my_checkButton.pack()
root.mainloop()