import tkinter, math
c = tkinter.Canvas(width=800, height=600)
c.pack()

# for a multi-pendulum project
"""def stationary_pendulum(x, y):
    c.create_line(x, y-500, x, y)
    c.create_oval(x-30, y-30, x+30, y+30, fill="grey")"""

def moving_pendulum(x, y, r, angle):
    x1 = x + r*math.cos(math.radians(angle))
    y1 = y + r*math.sin(math.radians(angle))
    c.create_line(x, y,x1, y1)
    c.create_oval(x1-30, y1-30, x1+30, y1+30, fill="red")


x, y = 400, 0

uhol = 180

max_uhol= 180
min_uhol = 0
pripocet = 3
while True:
    if max_uhol == min_uhol:
        moving_pendulum(x, y, 350, 90)
        break
    elif uhol == min_uhol:
        while uhol < max_uhol:
            moving_pendulum(x, y, 350, uhol)
            uhol += pripocet
            c.after(10)
            c.update()
            c.delete("all")
        uhol = max_uhol
        min_uhol+=10
        if pripocet>1:
            pripocet-=0.4
        
    elif uhol == max_uhol:
        while uhol > min_uhol:
            moving_pendulum(x, y, 350, uhol)
            uhol -= pripocet
            c.after(10)
            c.update()
            c.delete("all")
        uhol = min_uhol
        max_uhol-=10
    print(max_uhol, min_uhol)
c.mainloop()