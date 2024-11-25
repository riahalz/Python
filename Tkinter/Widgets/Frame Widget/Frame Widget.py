### Frame Widget ###
# container in which widgets are placed and organized
# frames can also be nested within each other

import tkinter as tk
root = tk.Tk()
root.title("Frame Widget")
root.geometry("600x400")

# Frame widget
frame1 = tk.Frame(root, bd=5, relief="ridge")
frame1.pack(padx=10, pady=10)

# Add widgets in frame
label = tk.Label(frame1, text="This is a label inside a frame")
label.pack(padx=15, pady=15)

button = tk.Button(frame1, text="Button inside frame")
button.pack(padx=15, pady=15)

root.mainloop()
