"""
import tkinter

c = tkinter.Canvas(width=800, height=400, bg="black")
c.pack()
x, y = 50, 350

def farba(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"


def obdlznik(x, y, farba):
    c.create_rectangle(x, y, x+50, y-300, fill=farba, tags="o")


r = 255
g = 0
b = 0
while True:
    if x < 700:
        obdlznik(x, y, farba = farba(r, g, b))
        c.after(20)
        c.delete("o")
        x+=9
        r-=3
        b+=3
        obdlznik(x, y, farba = farba(r, g, b))
        c.update()
    elif x >= 700:
        r = 0
        b = 255
        while x > 50:
            c.delete("o")
            obdlznik(x, y, farba = farba(r, g, b))
            c.after(20)
            x-=9
            r+=3
            b-=3
            obdlznik(x, y, farba = farba(r, g, b))
            c.update()

tkinter.mainloop()
"""


import tkinter, math
canvas = tkinter.Canvas(width=800, height=800)
canvas.pack()
r1 = 75
r2 = 125
def clock(minutes, seconds):
    canvas.create_rectangle(175, 30, 325, 90, width=5)
    canvas.create_oval(100, 100, 400, 400, width= 5)
    canvas.create_text(250, 60, text=f'{minutes:02d}:{seconds:02d}', font='arial 20')
    canvas.create_line(250, 250,
    250 + r1 * math.cos(-math.pi/2 + math.radians(6*minutes)),
    250 + r1 * math.sin(-math.pi/2 + math.radians(6*minutes)),
    fill='red',
    width=4)
    canvas.create_line(250, 250,
    250 + r2 * math.cos(-math.pi/2 + math.radians(6*seconds)),
    250 + r2 * math.sin(-math.pi/2 + math.radians(6*seconds)),
    width=4)



start = 1
minutes = start
seconds = 0
active = True
while active:
    clock(minutes, seconds)
    canvas.update()
    canvas.after(1000)
    if minutes == 0 and seconds == 0:
        canvas.create_text(250, 450, text='dobru chut')
        active=False
    else:
        canvas.create_rectangle(0, 0, 800, 800, width = 0, fill='white')
    seconds -=1
    if seconds < 0:
        seconds = 59
        minutes -= 1


canvas.mainloop()