### Multiple Buttons, each performing different action ###
 
import tkinter as tk
root = tk.Tk()
root.title("Button Click Counter")

def button_click():
    print("Button clicked")

def sometext():
    print ("Some text")

button1 = tk.Button (root, text = "Button 1", command = button_click())
button1.pack()
button2 = tk.Button (root, text = "Button 2", command = sometext())
button2.pack()

root.mainloop()
