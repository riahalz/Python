### Button Widget ###

import tkinter as tk
root = tk.Tk()
root.title("Button Widget")
root.geometry("600x400")

def button_click():
    print("Button clicked")
    
# Create Button widgets
Button1 = tk.Button(root, text = "Option 1", command = button_click())
    
# pack() - places widgets in center
Button1.pack()

# Execute theloop
root.mainloop()
