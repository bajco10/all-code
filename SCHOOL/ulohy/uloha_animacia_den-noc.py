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
