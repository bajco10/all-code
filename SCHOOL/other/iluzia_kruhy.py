import tkinter
import random
from math import sin, cos, radians

canvas = tkinter.Canvas(width=800, height=600)
canvas.pack()

x, y = 0, 0

def kruh(x, y):
    canvas.create_oval(x-70, y-70, x+70, y+70, fill="grey", outline="")

def sipka_hore(x, y):
    canvas.create_line(x, y-20,x, y+20, arrow="first", width=5)

def sipka_dole(x, y):
    canvas.create_line(x, y-20,x, y+20, arrow="last", width=5)

def sipka_vlavo(x, y):
    canvas.create_line(x-20, y, x+20, y, arrow="first", width=5)

def sipka_vpravo(x, y):
    canvas.create_line(x-20, y, x+20, y, arrow="last", width=5)

def ostatne(x, y):
    canvas.create_oval(x-200, y-200, x+200, y+200, fill="", outline="grey", width=110)
    canvas.create_rectangle(0, 0, 800, 150, fill="grey", outline="")
    canvas.create_rectangle(0, 450, 800, 600, fill="grey", outline="")



i = 0
while True:
    canvas.create_rectangle(x, y+150, x+800, y+330, fill="black", outline="")
    kruh(200, 300)
    kruh(600, 300)
    ostatne(200, 300)
    ostatne(600, 300)
    if i <= 400:
        sipka_vlavo(200, 300)
        sipka_vpravo(600, 300)
        i+=1
    elif i <=800:
        sipka_vlavo(600, 300)
        sipka_vpravo(200, 300)
        i+=1
    else:
        i = 0
    
    canvas.after(4)
    canvas.update()
    canvas.delete("all")
    if y >= 600:
        y = 0
    else:
        y+=25
    



tkinter.mainloop()