### Get Text from Widget ###

import tkinter as tk

def get_text():
    text_content = text.get("1.0", tk.END)
    print (text_content)
root = tk.Tk()
root.title("Get Text from Widget")

# create text box widget
text = tk.Text(root, height = 5, width = 40, font = "courier", bg = "yellow")
# insert text into widget
text.insert(tk.END, "Enter text here...")
text.pack()

# create button widget
button = tk.Button(root, text = "Get text", command = get_text)
button.pack()

root.mainloop()
