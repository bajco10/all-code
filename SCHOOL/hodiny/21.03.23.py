#12
def pocet_samohlasok(slovo):
    pocet = 0
    for znak in slovo:
        if znak in "aeiouy":
            pocet+=1
    print(pocet)

#pocet_samohlasok("stolik")
"""
# kreslenie domcekov
import tkinter, random
c = tkinter.Canvas(width=900, height=600, bg="lightblue")
c.pack()

def stvorec(x, y, a, farba):
    c.create_rectangle(x, y, x+a, y-a, fill=farba, outline="")


def trojuholnik(x, y, a, farba):
    c.create_polygon(x, y-a, x+a, y-a, x+a/2, y- 2*a, fill=farba, outline="")

def domcek(x, y, a=50, farba1="blue", farba2="red"):
    stvorec(x, y, a, farba=farba1)
    trojuholnik(x, y, a, farba=farba2)


for i in range(10):
    x, y = random.randrange(0, 850), random.randrange(100, 550)
    if i%2!=0:
        domcek(x, y)
    else:
        a = random.randrange(50, 160)
        domcek(x, y, a=a, farba1=f"#{random.randrange(255**3):06x}")

c.mainloop()
"""

import tkinter, random
c = tkinter.Canvas(width=800, height=600)
c.pack()

def kruh(x, y, r):
    c.create_oval(x-r, y-r, x+r, y+r, fill=f"#{random.randrange(255**3):06x}")


def sustredne(n, x, y):
    r = n*10
    for i in range(n):
        kruh(x, y, r)
        r-=10

def kresli(i):
    for i in range(i):
        x, y = random.randrange(50, 750), random.randrange(50, 550)
        n = random.randrange(5, 10)
        sustredne(n, x, y)

kresli(17)
c.mainloop()
