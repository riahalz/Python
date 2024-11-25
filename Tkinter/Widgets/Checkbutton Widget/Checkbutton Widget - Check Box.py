### Checkbutton Widget - Check Box ###

import tkinter as tk
root = tk.Tk()
root.title("Checkbutton Widget - Check Box")
root.geometry("600x400")

# define variables
var1 = tk.IntVar()
var2 = tk.IntVar()

# define function which will execute on clicking checkbox
def click():
    print ("Checkbox!")
    
# create Checkbutton widgets with command
CheckButton1 = tk.Checkbutton(root, text = "Option 1", variable = var1, command = click)
CheckButton1.pack()
CheckButton2 = tk.Checkbutton(root, text = "Option 2", variable = var2, command = click)
CheckButton2.pack()

root.mainloop()
