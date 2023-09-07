
import tkinter, random
c = tkinter.Canvas(width=400, height=400)
c.pack()

def rgb():
    return f"#{0:02x}{random.randrange(50, 255):02x}{0:02x}"


def kocka(x, y, a, farba):
    c.create_rectangle(x, y, x+a, y+a, fill=farba)

def rad(x, y, a, i):
     x = x - i*a/2
     print(x)
     farba = rgb()
     for j in range(i):
        kocka(x, y, a, farba)
        x+=a

def pyramida(n, x, y, a):
     for i in range(n+1):
          rad(x, y, a, i)
          y+=a

pyramida(5, 170, 30, 30)
c.mainloop()

"""
import tkinter, random
c = tkinter.Canvas(width=1000, height=600, bg="lightblue")
c.pack()

def zvyrazni():
    pass

def kresli():
    suradnice_bodov = []
    x = random.randrange(-200, 0)
    y = 599
    xstred = random.randrange(300, 700)
    while y < 600:
        if x < xstred:
            x += random.randrange(0, 10)
            y -= random.randrange(0, 7)
            bod = [x, y]
            suradnice_bodov.append(bod)
        else:
            x += random.randrange(0, 10)
            y += random.randrange(0, 7)
            bod = [x, y]
            suradnice_bodov.append(bod)
    f = f"#{0:02x}{random.randrange(30, 255):02x}{0:02x}"
    c.create_polygon(0, 600, suradnice_bodov, 0, 600, fill=f, outline="black", width=3)
    # bajana print(suradnice_bodov) 
    

def kopec(n):
    for i in range(n):
        kresli()

kopec(3)
c.mainloop()
"""