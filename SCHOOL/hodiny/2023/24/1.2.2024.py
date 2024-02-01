# efekt štetca
# 10 -> akcie v grafickej ploche
"""import tkinter
import random
c = tkinter.Canvas(width=800, height=800)
c.pack()

pocet = 50
farba = 'green'
vzd = 40
r = 1

def kresli(sx, sy):
    global pocet, faprba, vzd
    for i in range(pocet):
        px = random.randrange(-vzd, vzd)
        py = random.randrange(-vzd, vzd)
        c.create_oval(sx+px+r, sy+py+r, sx+px-r, sy+py-r, fill=farba, outline="")

def hover(e):
    kresli(e.x, e.y)

def tahaj(e):
    kresli(e.x, e.y)

# c.bind("<Button-1>", klik)
# c.bind("<B1-Motion>", tahanie)
c.bind("<Motion>", hover)
c.mainloop()"""

# 11
# nabindovat sipky na pohyb obrazku!
import tkinter
c = tkinter.Canvas(width = 800, height=800)
c.pack()

obr = tkinter.PhotoImage(file="retro_mario.png").subsample(2, 2)
c.create_image(400, 400, image=obr, tags="mario")


c.mainloop()