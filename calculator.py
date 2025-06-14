from tkinter import *
import math

def click(event):
    text = event.widget.cget("text")
    current = entry.get()

    if text == "=":
        try:
            result = eval(current)
            entry.delete(0, END)
            entry.insert(END, str(result))
            history_listbox.insert(END, f"{current} = {result}")
        except:
            entry.delete(0, END)
            entry.insert(END, "Error")
    elif text == "C":
        entry.delete(0, END)
    elif text == "←":
        entry.delete(len(current)-1)
    elif text == "√":
        try:
            result = math.sqrt(float(current))
            entry.delete(0, END)
            entry.insert(END, str(result))
        except:
            entry.delete(0, END)
            entry.insert(END, "Error")
    elif text == "x²":
        try:
            result = float(current)**2
            entry.delete(0, END)
            entry.insert(END, str(result))
        except:
            entry.delete(0, END)
            entry.insert(END, "Error")
    else:
        entry.insert(END, text)

def on_key(event):
    if event.char.isdigit() or event.char in "+-*/.()":
        entry.insert(END, event.char)
    elif event.keysym == "Return":
        click(Button(root, text="="))
    elif event.keysym == "BackSpace":
        click(Button(root, text="←"))

root = Tk()
root.title("Smart Calculator")
root.geometry("380x700")
root.config(bg="#e3f2fd")
root.resizable(False, False)

entry = Entry(root, font=("Helvetica", 28), bd=6, relief=RIDGE, justify=RIGHT, bg="#ffffff", fg="#333")
entry.pack(pady=20, padx=20, ipady=15, fill=X)

root.bind("<Key>", on_key)  # Keyboard support

def create_button(text, frame, bg="#f5f5f5", fg="#000"):
    btn = Button(
        frame,
        text=text,
        font=("Helvetica", 18, "bold"),
        bg=bg,
        fg=fg,
        relief=RAISED,
        bd=4,
        padx=10,
        pady=10,
        activebackground="#dcdcdc",
        activeforeground="#000",
    )
    btn.pack(side=LEFT, expand=True, fill=BOTH, padx=5, pady=5)
    btn.bind("<Button-1>", click)

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+'],
    ['.', 'x²', '√', '←']
]

button_colors = {
    '/': '#81ecec', '*': '#81ecec', '-': '#81ecec', '+': '#81ecec',
    '=': '#55efc4', 'C': '#fab1a0', '←': '#ffeaa7',
    '√': '#a29bfe', 'x²': '#a29bfe', '.': '#dfe6e9'
}

for row_vals in buttons:
    row = Frame(root, bg="#e3f2fd")
    row.pack(expand=True, fill="both", padx=10)
    for val in row_vals:
        create_button(val, row, bg=button_colors.get(val, "#f5f5f5"))

# History box
Label(root, text="History", bg="#e3f2fd", font=("Helvetica", 12, "bold")).pack()
history_listbox = Listbox(root, font=("Consolas", 12), height=5)
history_listbox.pack(padx=10, fill=BOTH, expand=False)

Label(root, text="Made by Rohit Saijare", bg="#e3f2fd", fg="#555", font=("Helvetica", 10)).pack(pady=5)

root.mainloop()
