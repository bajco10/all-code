# 6
'''import tkinter
canvas = tkinter.Canvas()
canvas.pack()

sur = []

def klik(event):
    global id
    sur[:] = [event.x, event.y]*2
    id = canvas.create_line(sur)

def tahanie(event):
    sur[2:4] = [event.x, event.y]
    canvas.coords(id, sur)

canvas.bind("<Button-1>", klik)
canvas.bind("<B1-Motion>", tahanie)
canvas.mainloop()'''
# 7
"""import tkinter, random
canvas = tkinter.Canvas()
canvas.pack()

sur = []

def klik(event):
    global id
    sur[:] = [event.x, event.y]*2
    f = f"#{random.randrange(255**3):06x}"
    id = canvas.create_rectangle(sur, fill=f)


def tahanie(event):
    sur[2:4] = [event.x, event.y]
    canvas.coords(id, sur)
def zmaz(e):
    canvas.delete(id)
canvas.bind("<Button-1>", klik)
canvas.bind("<B1-Motion>", tahanie)
canvas.bind("<ButtonRelease>", zmaz)
canvas.mainloop()"""
# 8, # 9
import tkinter
c = tkinter.Canvas(width = 800, height=800)
c.pack()
x1, y1 = 100, 200
#  x2, y2 = 150, 300
dx, dy = None, None
c.create_rectangle(x1, y1, x1+50, y1+50, fill="red", tag="stv")
c.create_rectangle(x1+200, y1+100, x1+350, y1+200, fill="blue", tag="obd")
def klik(e):
    global dx, dy, klik, aky
    dx, dy = None, None
    for prvok in "stv","obd":
        sur = c.coords(prvok)
    # klik = False
        if sur[0] <= e.x <= sur[2] and sur[1] <= e.y <= sur[3]:
            dx, dy = e.x-sur[0], e.y-sur[1]
            aky = prvok
            c.lift(aky)
        # klik = True

def tahanie(e):
    # global klik
    sur = c.coords(aky)
    if dx != None:
        sirka, vyska = abs(sur[0]-sur[2]), abs(sur[1]-sur[3])
        c.coords(aky, e.x-dx, e.y-dy, e.x-dx+sirka, e.y-dy+vyska)


c.bind("<Button-1>", klik)
c.bind("<B1-Motion>", tahanie)
c.mainloop()