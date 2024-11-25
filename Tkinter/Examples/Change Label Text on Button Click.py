### Change Label Text on Button Click

import tkinter as tk
root = tk.Tk()
root.title("Change Label Text on Button Click")
root.geometry("600x400")

# Function to change label text
def change_text():
    label.config(text="Text has been changed.")

# Create label with initial text
label = tk.Label(root, text="Original Text", font=("Arial", 16))
label.pack(pady=20)

# Create button to change label text
button = tk.Button(root, text="Click to Change Label Text", font=("Arial", 16), command=change_text)
button.pack(pady=10)

# Run the application
root.mainloop()
