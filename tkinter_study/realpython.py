import tkinter as tk
root = tk.Tk()
"""
greeting = tk.Label(root, text="Python")
greeting.pack()
"""
button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="white"
).pack()
root.mainloop()