"""import tkinter as tk
root = tk.Tk()
greeting = tk.Label(root, text="Python")
greeting.pack()
button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="white"
).pack()
root.mainloop()"""


"""import tkinter as tk
window = tk.Tk()

label = tk.Label(text="Name")
entry = tk.Entry().get

label.pack()
entry.pack()
name = entry.get()
print(name)


window.mainloop()
"""
# frame widgets
"""import tkinter as tk

border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}

window = tk.Tk()

for relief_name, relief in border_effects.items():
    frame = tk.Frame(master=window, relief=relief, borderwidth=5)
    frame.pack(side=tk.LEFT)
    label = tk.Label(master=frame, text=relief_name)
    label.pack()

window.mainloop()"""

# check your understanding - entry
"""import tkinter as tk
window = tk.Tk()

entry = tk.Entry(width=40, bg="white", fg="black")
entry.pack()
entry.insert(0, "What is your name?")

window.mainloop()
"""

# geometry managers - pack()
"""import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(master=window, width=200, height=100, bg="red")
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame2 = tk.Frame(master=window, width=100, bg="yellow")
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame3 = tk.Frame(master=window, width=50, bg="blue")
frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

window.mainloop()"""

# geometry managers - place()
# few drawbacks - usually not used 
# can place using coordinates
"""import tkinter as tk

window = tk.Tk()

frame = tk.Frame(master=window, width=150, height=150)
frame.pack()

label1 = tk.Label(master=frame, text="I'm at (0, 0)", bg="red")
label1.place(x=0, y=0)

label2 = tk.Label(master=frame, text="I'm at (75, 75)", bg="yellow")
label2.place(x=75, y=75)

window.mainloop()
"""

# geometry managers - grid()
# most common
"""import tkinter as tk

window = tk.Tk()

for i in range(10):
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)
    for j in range(10):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)
        if i==j:
            label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}", bg="lime")
        else:
            label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}", bg="white")
        label.pack(padx=5, pady=5)

window.mainloop()
"""
"""import tkinter as tk

window = tk.Tk()
window.columnconfigure(0, minsize=250)
window.rowconfigure([0, 1], minsize=100)

label1 = tk.Label(text="A")
label1.grid(row=0, column=0, sticky="ne")

label2 = tk.Label(text="B")
label2.grid(row=1, column=0, sticky="sw")

window.mainloop()"""

"""import tkinter as tk

window = tk.Tk()

window.rowconfigure(0, minsize=50)
window.columnconfigure([0, 1, 2, 3], minsize=50)

label1 = tk.Label(text="1", bg="black", fg="white")
label2 = tk.Label(text="2", bg="black", fg="white")
label3 = tk.Label(text="3", bg="black", fg="white")
label4 = tk.Label(text="4", bg="black", fg="white")

label1.grid(row=0, column=0)
label2.grid(row=0, column=1, sticky="ew")
label3.grid(row=0, column=2, sticky="ns")
label4.grid(row=0, column=3, sticky="nsew")

window.mainloop()"""

# address entry form
"""import tkinter as tk
window = tk.Tk()

frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
frm_form.pack()

# first_name
lbl_first_name = tk.Label(master=frm_form, text="First Name:")
ent_first_name = tk.Entry(master=frm_form, width=50)
lbl_first_name.grid(row=0, column=0, sticky="e")
ent_first_name.grid(row=0, column=1)
# last_name
lbl_last_name = tk.Label(master=frm_form, text="Last Name:")
ent_last_name = tk.Entry(master=frm_form, width=50)
lbl_last_name.grid(row=1, column=0, sticky="e")
ent_last_name.grid(row=1, column=1)
# Address Line 1
lbl_address_line1 = tk.Label(master=frm_form, text="Address Line 1:")
ent_address_line1 = tk.Entry(master=frm_form, width=50)
lbl_address_line1.grid(row=2, column=0, sticky="e")
ent_address_line1.grid(row=2, column=1)
# Address line 2
lbl_address_line2 = tk.Label(master=frm_form, text="Address Line 2:")
ent_address_line2 = tk.Entry(master=frm_form, width=50)
lbl_address_line2.grid(row=3, column=0, sticky="e")
ent_address_line2.grid(row=3, column=1)
# City
lbl_city = tk.Label(master=frm_form, text="City:")
ent_city = tk.Entry(master=frm_form, width=50)
lbl_city.grid(row=4, column=0, sticky="e")
ent_city.grid(row=4, column=1)
# State/Province
lbl_state = tk.Label(master=frm_form, text="State/Province:")
ent_state = tk.Entry(master=frm_form, width=50)
lbl_state.grid(row=5, column=0, sticky="e")
ent_state.grid(row=5, column=1)
# Postal Code
lbl_code = tk.Label(master=frm_form, text="Postal Code:")
ent_code = tk.Entry(master=frm_form, width=50)
lbl_code.grid(row=6, column=0, sticky="e")
ent_code.grid(row=6, column=1)
# Country
lbl_country = tk.Label(master=frm_form, text="Country:")
ent_country = tk.Entry(master=frm_form, width=50)
lbl_country.grid(row=7, column=0, sticky="e")
ent_country.grid(row=7, column=1)

frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

btn_submit = tk.Button(master=frm_buttons, text="Submit")
btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)

btn_clear = tk.Button(master=frm_buttons, text="Clear")
btn_clear.pack(side=tk.RIGHT, ipadx=10)

window.mainloop()"""

# making your applications interactive

import tkinter as tk

window = tk.Tk()

def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)

# Bind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)

window.mainloop()