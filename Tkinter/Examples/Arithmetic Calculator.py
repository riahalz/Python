### Create a Calculator ###

# Create tkinter window
import tkinter as tk
root = tk.Tk()
root.title("Arithmetic Calculator")
root.resizable(True, True)
input_text = tk.StringVar()

# Entry widget for input display
display = tk.Entry(root, textvariable=input_text, font=("Arial", 20), bd=10, insertwidth=4, width=30, borderwidth=4, justify="right")
display.grid(row=0, column=0, columnspan=4)

# Button click function to update display
def button_click(item):
    current = input_text.get()
    input_text.set(current + str(item))

# Function to clear display
def button_clear():
    input_text.set("")

# Function to calculate expression
def button_equal():
    try:
        result = str(eval(input_text.get())) # Evaluate expression
        input_text.set(result)
    except:
        input_text.set("Error") # Display error for invalid expression

# Define buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Create button widgets and add them to grid
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, width=10, height=3, font=("Arial", 12), bd=1, command=button_equal)
    elif text == 'C':
        button = tk.Button(root, text=text, width=10, height=3, font=("Arial", 12), bd=1, command=button_clear)
    else:
        button = tk.Button(root, text=text, width=10, height=3, font=("Arial", 12), bd=1, command=lambda t=text: button_click(t))
    button.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
