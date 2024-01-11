"""import tkinter

canvas = tkinter.Canvas()
canvas.pack()

zoznam = []

def klik(event):
    global ciara
    zoznam[:] = [event.x, event.y]
    ciara = canvas.create_line(0, 0, 0, 0)

def tahanie(event):
    zoznam.extend([event.x, event.y])
    canvas.coords(ciara, zoznam)

canvas.bind('<Button-1>', klik)
canvas.bind('<B1-Motion>', tahanie)
canvas.mainloop()"""

"""import tkinter
import random

canvas = tkinter.Canvas()
canvas.pack()

zoznam = []

def klik(event):
    global poly
    zoznam[:] = [event.x, event.y]
    farba = f'#{random.randrange(256**3):06x}'
    poly = canvas.create_polygon(0, 0, 0, 0, fill=farba)

def tahanie(event):
    zoznam.extend([event.x, event.y])
    canvas.coords(poly, zoznam)

canvas.bind('<Button-1>', klik)
canvas.bind('<B1-Motion>', tahanie)
canvas.mainloop()"""

# 1
"""import tkinter

canvas = tkinter.Canvas()
canvas.pack()

def klik(event):
    x, y = event.x, event.y
    canvas.create_text(x, y, text=f"({x}, {y})", font="Arial 10")
canvas.bind("<1>", klik)
canvas.mainloop()"""
# 2
"""import tkinter

c = tkinter.Canvas()
c.pack()

zoznam = list("PYTHON")
zoznam = 'python java pascal c++ ruby php logo javascript'.split()

def klik(e):
    global zoznam
    x, y = e.x, e.y
    if zoznam:
        slovo = zoznam.pop(0)
        c.create_text(x, y, text=slovo, font="Arial 22")
c.bind("<1>", klik)
c.mainloop()"""
# 3
"""import tkinter
import random
c = tkinter.Canvas(width=600, height=300, bg="white")
c.pack()

x, y, r = 100, 100, 50
for i in range(8):
    c.create_rectangle(x, y, x+r, y+r)
    x+=50

def klik(e):
    global r
    index = (e.x-100)//r
    if index >=0:
        c.itemconfig(index+1, fill=f"#{random.randrange(255**3):06x}")
c.bind("<1>", klik)
c.mainloop()"""
# 4
"""import tkinter
import random
c = tkinter.Canvas(width=600, height=300, bg="white")
c.pack()

x, y, r = 100, 100, 50
stvorce = []
for i in range(8):
    c.create_rectangle(x, y, x+r, y+r)
    x+=50
    stvorce.append(0)

def klik(e):
    global r
    global stvorce
    index = (e.x-100)//r
    if index >=0 and index<len(stvorce) and y+r>e.y>y:
        stvorce[index]+=1
        if stvorce[index] > 2:
            stvorce[index] = 0
        farby = ["white", "blue", "red"]
        c.itemconfig(index+1, fill=farby[stvorce[index]])
c.bind("<1>", klik)
c.mainloop()"""

# 5
import tkinter
import random
c = tkinter.Canvas(width=600, height=200, bg="white")
c.pack()
n = 8
zoznam = []
for i in range(n):
    zoznam.append(i)
random.shuffle(zoznam)

x, y, r = 100, 100, 50
for i in zoznam:
    c.create_rectangle(x, y, x+r, y+r)
    if i != 0:
        c.create_text(x+r/2, y+r/2, text=i)
    x+=50
# print(zoznam)
def klik(e):
    global r
    global zoznam
    x, y=100, 100
    index = (e.x-100)//r
    if index >= 0 and index<len(zoznam) and y+r>e.y>y:
        prazdne = zoznam.index(0)
        zoznam[prazdne] = zoznam[index]
        zoznam[index] = 0
        # print(zoznam)
        c.update()
        c.delete("all")
        for i in zoznam:
            c.create_rectangle(x, y, x+r, y+r)
            if i != 0:
                c.create_text(x+r/2, y+r/2, text=i)
            x+=50
        c.update()
        dobry_zoznam = sorted(zoznam)
        dobry_zoznam.remove(0)
        if zoznam[:-1] == dobry_zoznam:
            print("Hura!")

c.bind("<1>", klik)
c.mainloop()
