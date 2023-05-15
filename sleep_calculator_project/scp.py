import tkinter as tk

import logic

window=tk.Tk()
window.title("sleep calculator")
c = tk.Canvas()
c.pack()
button = tk.Button(window, text="Click me!")
button.pack()
# button.grid(row=2, column=4)
print(logic.sleep_logic.time_calculation(5,0))

window.mainloop()
