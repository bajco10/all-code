"""
import tkinter
import random
c = tkinter.Canvas(width=800, height=500)
c.pack()
n = 30
r = 20

for i in range(n):
    x, y = random.randrange(20, 780), random.randrange(20, 480)
    cislo = random.randrange(1, 100)
    f1 = random.randrange(255**3)
    c.create_oval(x-r, y-r, x+r, y+r, fill=f"#{f1:06x}")
    c.create_text(x, y, text=i, font="Arial 20", fill=f"#{(255**3)-f1:06x}")

tkinter.mainloop()
"""
# cifernik na hodinach
"""
import tkinter
import random
import math
c = tkinter.Canvas(width=800, height=500)
c.pack()

suradnice = []
uhol = -60
n = 12
sx, sy = 400, 250
r = 150
c.create_oval(sx-r, sy-r, sx+r, sy+r, width=3)
for i in range(1, n+1):
    x = sx + (r+25)*math.cos(math.radians(uhol)) 
    y = sy + (r+25)*math.sin(math.radians(uhol))
    c.create_text(x, y, text=i, font="Arial 25")
    uhol += 360//n
    suradnice.append(x)
    suradnice.append(y)
uhol = -90
for i in range(100000):
    x = sx + (r-10) * math.cos(math.radians(uhol))
    y = sy + (r-10) * math.sin(math.radians(uhol))
    c.create_line(sx, sy, x, y, fill="red", tags="sek")
    uhol += 360/60
    c.after(10)
    c.update()
    c.delete("sek")
# c.create_polygon(suradnice, fill="", width=1, outline="black")
tkinter.mainloop()
"""
"""
import tkinter
import random
c = tkinter.Canvas()
c.pack()
slovo = "lubim python" # input("slovo: ")
slovo = slovo.upper()
x, y = 40, 100
for j in slovo:
    c.create_rectangle(x-15, y-15, x+15, y+15, fill=f"#{random.randrange(255**3):06x}")
    c.create_text(x, y, text=j, fill=f"#{random.randrange(255**3):06x}", font="Arial 25")
    x += 30

tkinter.mainloop()
"""
import tkinter
import math
canvas = tkinter.Canvas()
canvas.pack()
x0, y0 = 300, 200
r = 100
krok = 20
for uhol in range(0, 360, krok):
    x = x0 + r * math.cos(math.radians(uhol))
    y = y0 + r * math.sin(math.radians(uhol))
    x1 = x0 + r * math.cos(math.radians(uhol+krok))
    y1 = y0 + r * math.sin(math.radians(uhol+krok))
    
    canvas.create_line(x, y, x1, y1)
tkinter.mainloop()
















