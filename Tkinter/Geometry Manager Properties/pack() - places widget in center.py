### Geometry Manager - pack() ###

from tkinter import *
root = Tk()
root.title("Label Widget")
root.geometry("600x400")
root.resizable(True, True)

# Create widget
myLabel = Label(root, text = "Hello")

# pack() - places widget in center
myLabel.pack()

root.mainloop()
