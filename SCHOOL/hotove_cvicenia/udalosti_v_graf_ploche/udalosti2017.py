# 1
"""
import tkinter
c = tkinter.Canvas()
c.pack()

def klik(e):
    c.create_text(e.x, e.y, text = f"({e.x}, {e.y})")

c.bind("<Button-1>", klik)
c.mainloop()
"""
# 2
"""
import tkinter
c = tkinter.Canvas()
c.pack()

zoznam = list("PYTHON")
zoznam2 = "python java pascal c++ ruby php logo javascript".split()
print(zoznam2)
def klik(e):
    if len(zoznam) > 0:
        c.create_text(e.x, e.y, text=zoznam[0], font="arial 22")
        zoznam.pop(0)
c.bind("<Button-1>", klik)
c.mainloop()
"""
# 3
"""
import tkinter
c = tkinter.Canvas(width=500, height=300) 
c.pack()

x0, y0 = 20, 100
for i in range(8):
    c.create_rectangle(x0, y0, x0+50, y0+50, fill="white")
    x0+=55

def klik(e):
    naco = c.find_withtag("current")
    idcko = naco[0]
    c.itemconfig(idcko, fill="red")

c.bind("<Button-1>", klik)
c.mainloop()
"""