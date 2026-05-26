from tkinter import *

# Create window
root = Tk()
root.title("Modern Calculator")
root.geometry("360x500")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

# Display screen
entry = Entry(
    root,
    width=15,
    font=("Arial", 28),
    border=0,
    bg="#2d2d2d",
    fg="white",
    justify=RIGHT
)

entry.grid(row=0, column=0, columnspan=4, pady=20, padx=10)

# Functions
def click(value):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current + str(value))

def clear():
    entry.delete(0, END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, result)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

# Button style
button_style = {
    "font": ("Arial", 18),
    "width": 5,
    "height": 2,
    "bd": 0,
    "fg": "white"
}

# Buttons layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Create buttons
for (text, row, col) in buttons:

    if text == "=":
        Button(
            root,
            text=text,
            command=calculate,
            bg="#ff9500",
            **button_style
        ).grid(row=row, column=col, padx=5, pady=5)

    else:
        Button(
            root,
            text=text,
            command=lambda t=text: click(t),
            bg="#3a3a3a",
            **button_style
        ).grid(row=row, column=col, padx=5, pady=5)

# Clear button
Button(
    root,
    text="C",
    command=clear,
    bg="#ff3b30",
    **button_style
).grid(row=5, column=0, columnspan=4, sticky="we", padx=5, pady=10)

# Run app
root.mainloop()
