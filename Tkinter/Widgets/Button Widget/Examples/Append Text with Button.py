### Append Text ###

import tkinter as tk

# define function to append text
def append_text():
    text_content = entry.get()
    textbox.insert(tk.END, text_content +  "\n")
    entry.delete(0, tk.END) # clears entry after appending
    
root = tk.Tk()
root.title("Append Text")
root.geometry("600x400")

# create entry widget
entry = tk.Entry(root)
entry.pack(pady = 10)

# create text widget to display appended content
textbox = tk.Text(root, height = 10, width = 40)
textbox.pack(pady = 10)

# create button to append content 
append_btn = tk.Button(root, text = "Append Text", command = append_text)
append_btn.pack(pady = 10)

root.mainloop()
