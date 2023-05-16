from tkinter import *
from tkinter import ttk

root = Tk()

entry = ttk.Entry(root, width=30)  # size of the entry box
entry2 = ttk.Entry(root, width=30)
entry.insert(0, "Please enter your name")  # 0 is the index - first character
entry2.config(show="*")  # hide the password

entry.pack()
entry2.pack()

root.geometry("400x400")
root.mainloop()
