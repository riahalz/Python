import tkinter as tk
root = tk.Tk()
root.title = "Toggle Button"

# Function to toggle button states
def toggle_button():
    if button["text"] == "OFF":
        button.config(text="ON", bg="green")
    else:
        button.config(text="OFF", bg="red")

# Button with toggle command
button = tk.Button(root, text="OFF", bg="red", command=toggle_button)
button.pack()
root.mainloop
