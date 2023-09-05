#generator cisel ako kocka, ktory sa zastavi, ked "padnu" tri sestky + vypise pocet hodov
"""import random
def kocka():
    x, y, z = 0, 0, 0
    sucet = 0
    while True:
        x, y, z = random.randrange(1, 7), random.randrange(1, 7), random.randrange(1, 7)
        sucet+=1
        if x+y+z == 18:
            print(f"{x}{y}{z}", end="")
            break
        print(f"{x}{y}{z}", end="")
    print(f"\n{sucet}")
kocka()"""
#to iste ale akekolvek cisla 5x za sebou
"""import random
def kockas():
    pom = 0
    cislo = 0
    while pom < 5:
        x = random.randrange(1, 7)
        if x !=cislo:
            cislo = x
            pom = 0
        elif x ==cislo:
            pom +=1
        print(x, end="")
kockas()"""
#stvorced farbickovy
"""import tkinter, random
c = tkinter.Canvas(width=800, height=800)
c.pack()
def rgb():
    return f"#{random.randrange(255**3):06x}"

def stvorcek(x, y, farba):
    c.create_rectangle(x, y, x+100, y+100, fill=farba, outline="")

def main():
    x, y = 0, 0
    for i in range(9):
        for j in range(9):
            if i==j or j==7-i:
                stvorcek(x, y, "white")
                x+=100
            else:
                stvorcek(x, y, rgb())
                x+=100
        y+=100
        x=0
main()
c.mainloop()"""
#gradient - prechod
import tkinter, random
c = tkinter.Canvas(width=600, height=600)
c.pack()
def farba(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"
def prechod():
    x, y = 0, 0
    r,g,b = random.randrange(0, 60), random.randrange(0, 255), random.randrange(0, 60)
    for i in range(61):
        for j in range(61):
            c.create_rectangle(x, y, x+10, y+10, fill=farba(r, g, b), outline = "")
            y+=10
        b+=2
        r+=3
        x+=10
        y=0
prechod()
c.mainloop()
