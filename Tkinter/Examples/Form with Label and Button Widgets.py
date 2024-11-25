### Form Example ###
 
from tkinter import *

root = Tk()
root.title("Form Example")
root.geometry("600x400")

# Create label widget
lb1 = Label(root, text = "Form")
lb1.pack()

# Create text entry widget
e = Entry(root, width = 50)
e.pack()

# Define function to print input as label
def myClick():
    message = "Hello " + e.get()
    lb4 = Label(root, text = message)
    lb4.pack()
    
# Create button widget with command to print message
button = Button(root, text = "Click Me", command = myClick, bg = "blue", fg = "black")
button.pack()

root.mainloop()


