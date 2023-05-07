import tkinter
from random import randrange as rr

c = tkinter.Canvas(width=500, height=400)
c.pack()
while True:
    n = 4
    r = 20
    x, y = rr(100, 400), rr(100, 300)
    px, py = rr(-10, 11), rr(-10, 11)

    co = c.create_oval(x-r, y-r, x+r, y+r, fill="red")
    if py>0:
        c.itemconfig(co, fill="blue")
    co2 = c.create_text(x, y, text=n, font="arial 20")
    while True:
        if not(20<x<480):
            px=-px
            n-=1
            c.itemconfig(co2, text=n)
        if not(20<y<380):
            py=-py
            n-=1
            c.itemconfig(co2, text=n)
        if py>0:
            c.itemconfig(co, fill="blue")
        else:
            c.itemconfig(co, fill="red")
        if n == 0:
            c.delete("all")
            break

        c.move(co, px, py)
        c.move(co2, px, py)
        c.update()
        c.after(40)
        x+=px
        y+=py

tkinter.mainloop()

