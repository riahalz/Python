### Display Word Count of Text in Field ###

import tkinter as tk
root = tk.Tk()
root.title("Display Word Count of Text in Field")
root.geometry("600x400")

def count_words():
    userinput = textentry.get()
    word_count = len(userinput.split())
    label.config(text=f"Word Count: {word_count}")
    
textentry = tk.Text(root, font=("Arial", 16))
textentry.pack()

label = tk.Label(root, text = "Enter some text", font=("Arial", 16))
label.pack()

button = tk.Button(root, text="Count Words", font=("Arial", 16), command=count_words)
button.pack()

root.mainloop()
