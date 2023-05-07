import tkinter

c = tkinter.Canvas(width=400, height=400, bg="black")
c.pack()

def obdlznik1(x, y):
    c.create_rectangle(x, y, x+50, y+300 , fill="white", outline="", tags="o1")

def obdlznik2(x,y):
    c.create_rectangle(x, y, x+300, y+50, fill="white", outline="", tags="o2")

def stvorcek(x, y):
    c.create_rectangle(x, y, x+50, y+50, fill="grey", outline="", tags="s")

x1, y1 = 50, 50
x2, y2 = 50, 50
x3, y3 = 50, 50

stvorcek(x3, y3)

while True:
    if x1 < 300:
        obdlznik1(x1, y1)
        obdlznik2(x2, y2)
        stvorcek(x3, y3)
        c.after(20)
        c.delete("o1", "o2", "s")
        x1+=5
        y2+=5
        x3 = x1
        y3 = y2
        obdlznik1(x1, y1)
        obdlznik2(x2, y2)
        stvorcek(x3, y3)
        c.update()
    elif x1 >= 300:
        while x1 > 50:
            c.delete("o1", "o2", "s")
            obdlznik1(x1, y1)
            obdlznik2(x2, y2)
            stvorcek(x3, y3)
            c.after(20)
            x1-=5
            y2-=5
            x3 = x1
            y3 = y2
            obdlznik1(x1, y1)
            obdlznik2(x2, y2)
            stvorcek(x3, y3)
            c.update()

tkinter.mainloop()
