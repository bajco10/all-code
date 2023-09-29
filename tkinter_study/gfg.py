#root explanation
"""from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("First_Program")

label = Label(root, text="Hello World !").pack()

root.mainloop()"""

#button(widget) introduction
"""from tkinter import *

root=Tk()
frame = Frame(root)
frame.pack()
button = Button(frame, text="Hello")
button.pack()
root.mainloop()"""

#hello world in tkinter
"""from tkinter import *
root=Tk()
a = Label(root, text="Hello, world!")
a.pack()
root.mainloop()"""

#first GUI application
from tkinter import *

root=Tk()

#root window title and dimensions
root.title("Welcome to the first GUI.")
root.geometry("350x200")
#adding a label to the root window
lbl = Label(root, text="Are you welcome?")
lbl.grid()
#adding an Entry Field
txt=Entry(root,width=10)
txt.grid(column=1, row=0)
#function to display text when button is clicked
def clicked():
    res = "You wrote" + txt.get()
    lbl.configure(text= res)
#button widget with red text
btn = Button(root, text="Click me",
            fg="red", command=clicked)
btn.grid(column=2, row=0)

root.mainloop()