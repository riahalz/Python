### Get Input from Entry Widget ###
 
import tkinter as tk

# Define function to get input from entry widget
def get_input():
    name = entry.get()
    print ("Hello ", name)

root = tk.Tk()
root.title("Fetch Input from Entry Widget")
root.geometry("600x400")

# Create label widget
label = tk.Label(root, text = "Enter your name:")
label.pack()

# Create text input/entry widget
entry = tk.Entry(root, width = 50)
entry.pack()

# Create button widget with command to get input
button = tk.Button(root, text = "Submit", command = get_input)
button.pack()

root.mainloop()

## Output: Hello name
