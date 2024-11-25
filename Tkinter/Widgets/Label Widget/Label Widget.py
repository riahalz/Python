### Label Widget ###

from tkinter import *
root = Tk()
root.title("Label Widget")
root.geometry("600x400")
root.resizable(True, True)

# Create Label widgets
myLabel = Label(root, text = "Hello")
myLabel2 = Label(root, text = "Good Morning")

# place widgets using geometry manager
myLabel.pack()
myLabel2.pack()

root.mainloop()
