import tkinter, random
c = tkinter.Canvas(width=1000, height=300)
c.pack()

def rgb():
    return f"#{00:02x}{00:02x}{(random.randrange(100, 255)):02x}"

def trojuholnik(x, y, a, farba="red"):
    c.create_polygon(x-10, y, x+a/2, y-a, x+10+a, y, fill=farba, outline="")

def stvorec(x, y, a, farba="green"):
    c.create_rectangle(x, y, x+a, y-a, fill=farba, outline="")

def domcek(n, farba="green"):
    x, y = 20, 200
    for i in range(n):
        a = random.randrange(50, 100)
        if x + a > 900:
            pass
        else:
            if (i+1)%3==0:
                trojuholnik(x, y-a, a)
                stvorec(x, y, a, farba=rgb())
                x+=a+20
            else:
                trojuholnik(x, y-a, a)
                stvorec(x, y, a, farba=farba)
                x+=a+20


domcek(22, "pink")
c.mainloop()
