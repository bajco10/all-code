import tkinter
import math
import random

def rgb_picker():
    return f"#{random.randrange(255**3):06x}"
c = tkinter.Canvas(width=800, height=500)
c.pack()
n = 30
uhol = -60
sx, sy = 400, 250
r = 150
h1, h2 = 100, 50
m = 0
krok = int(round(360/n, 0))

while True:
    for uhol in range(0, 360, krok):
        x = sx + r*math.cos(math.radians(uhol))
        y = sy + r*math.sin(math.radians(uhol))
        x1 = sx + r*math.cos(math.radians(uhol+krok))
        y1 = sy + r*math.sin(math.radians(uhol+krok))
        xv = sx + (r+h1)*math.cos(math.radians(uhol + krok/2))
        yv = sy + (r+h1)*math.sin(math.radians(uhol + krok/2))
        c.create_polygon(x, y, x1, y1,xv, yv, fill=rgb_picker(), outline="orange", tags="luce")
        h1, h2 = h2, h1
    c.create_oval(sx-(r+2), sy-(r+2), sx+(r+2), sy+(r+2), width=2, fill=rgb_picker(), 
        outline="")
    c.after(100)
    c.update()
    c.delete("luce")
    h1, h2 = h2, h1


tkinter.mainloop()


