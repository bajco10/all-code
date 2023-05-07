"""
import tkinter, random, math
c = tkinter.Canvas(width=600, height=600)
c.pack()

x, y, r = 300, 300, 200
c.create_oval(x-r, y-r, x+r, y+r, fill="cyan", outline="")

def rucicka(x, y, uhol, r=200):
    x1 = x + r*math.cos(math.radians(uhol))
    y1 = y + r*math.sin(math.radians(uhol))
    c.create_line(x, y, x1, y1, width=2, arrow="last", tags="rucicka")


uhol = 0
while True:
    c.delete("rucicka")
    rucicka(x, y, uhol)
    uhol+=1
    c.after(10)
    c.update()
    


c.mainloop()
"""
"""
import tkinter

c = tkinter.Canvas(width=1200, height=800)
c.pack()

obr = tkinter.PhotoImage(file="/home/tomas/Desktop/programovanie/SKOLA/ulohy/strom1.png")
def strom():
    c.create_image(1000, 400, image=obr, tags="strom")

def zem():
    c.create_rectangle(0,800, 1200, 600, fill="green", outline="", tags="zem")

def mesiac(x, y):
    c.create_oval(x-60, y-60, x+60, y+60, fill="white", outline="", tags="mesiac")
    c.create_oval(x+20-50, y-50, x+20+50, y+50, fill="black", outline="", tags="mesiac")

def slnko(x, y):
    c.create_oval(x-60, y-60, x+60, y+60, fill="yellow", tags="slnko")
    c.create_text(x, y-13, text=f"{chr(9786)}", font="arial 152", tags="slnko")

def pozadie(r, g, b):
    c.create_rectangle(0, 0, 1200, 800, fill=f"#{r:02x}{g:02x}{b:02x}")


while True:
    r, g, b = 127, 127, 255
    x = 0
    for i in range(124):
        pozadie(r, g, b)
        if r <= 30:
            r, g, b = 0, 0, 0
        else:
            r-=20
            g-=20
            b-=40
        zem()
        mesiac(x, 150)
        strom()
        c.update()
        x+=10
        c.after(20)
        c.delete("all")
    x=0
    for i in range(124):
        pozadie(r, g, b)
        if r >= 120:
            r, g, b = 127, 127, 255
        else:
            r+=20
            g+=20
            b+=40
        zem()
        slnko(x, 150)
        strom()
        c.update()
        x+=10
        c.after(20)
        c.delete("all")
tkinter.mainloop()
"""


import tkinter
c = tkinter.Canvas()
c.pack()

def vlajka(smer, x, y, f1, f2, f3):
    if smer=="horizontalna":
        c.create_rectangle(x, y, x+100, y+20, fill=f1, outline="")
        c.create_rectangle(x, y+20, x+100, y+40, fill=f2, outline="")
        c.create_rectangle(x, y+40, x+100, y+60 ,fill=f3, outline="")
    else:
        c.create_rectangle(x, y, x+20, y+50, fill=f1, outline="")
        c.create_rectangle(x+20, y, x+40, y+50, fill=f2, outline="")
        c.create_rectangle(x+40, y, x+60, y+50, fill=f3, outline="")
    
vlajka("horizontalna", 100, 100, "red", "white", "green")

c.mainloop()