import tkinter as tk

def click_button(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Advanced Calculator")

entry = tk.Entry(root, width=30, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0
for button in buttons:
    if button == '=':
        tk.Button(root, text=button, width=8, command=calculate).grid(row=row, column=col)
    elif button == '0':
        tk.Button(root, text=button, width=8, command=lambda b=button: click_button(b)).grid(row=row, column=col, columnspan=2)
        col += 1
    else:
        tk.Button(root, text=button, width=8, command=lambda b=button: click_button(b)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(root, text='C', width=8, command=clear).grid(row=row, column=0, columnspan=4)

root.mainloop()