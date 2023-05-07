import tkinter, math, random
c = tkinter.Canvas(width=640, height=480)
c.pack()

x, y = 320, 240

c.create_oval(x-200, y-200, x+200, y+200, fill="", outline="blue", width=3)

def kresliaci_kruzok(x, y, uhol, r_velke, farba, r_male=50):
    x1 = x + r_velke * math.cos(math.radians(uhol))
    y1 = y + r_velke * math.sin(math.radians(uhol))

    l1 = x1 + r_male * math.cos(math.radians(1/3*uhol))
    l2 = y1 + r_male * math.sin(math.radians(1/3*uhol))

    c.create_oval(x1-50, y1-50, x1+50, y1+50, fill="", outline="green", width=3, tags="kruh")
    c.create_oval(l1-3, l2-3, l1+3, l2+3, fill=farba, outline="", tags="kruzok")

r_velke=300
while True:
    uhol = 0
    farba = f"#{random.randrange(255**3):06x}"
    while uhol >= -360:
        kresliaci_kruzok(320, 240, uhol, r_velke, farba)
        uhol-=1
        c.update()
        c.after(2)
        c.delete("kruh")
    if r_velke >= 150:
        r_velke = 3
    else:
        r_velke+=10

    # c.delete("kruzok")


tkinter.mainloop()