import tkinter as tk

parent = tk.Tk()

# create the widget
my_text = tk.Text(parent)

# insert a string at the beginning
my_text.insert("1.19", "Practice")

# delete the first and last character (including a new line)
my_text.delete("1.0")
my_text.delete("end - 2 chars")
my_text.pack()
parent.mainloop()