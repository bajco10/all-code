import tkinter, math
c = tkinter.Canvas(width=640, height=480)
c.pack()

x, y = 320, 240

def ostatne():
    c.create_line(x-200, y, x+200, y, fill="red", width=3)
    c.create_oval(x-200, y-200, x+200, y+200, fill="", outline="blue", width=3)
    

def kruzok(x, y, uhol):
    x1 = x + 100 * math.cos(math.radians(uhol))
    y1 = y + 100 * math.sin(math.radians(uhol))

    l1 = x1 + 100 * math.cos(math.radians(360-uhol))
    l2 = y1 + 100 * math.sin(math.radians(360-uhol))
    l3 = x1 + 100 * math.cos(math.radians(360-uhol+180))
    l4 = y1 + 100 * math.sin(math.radians(360-uhol+180))
    
    m1 = x1 + 100 * math.cos(math.radians(360-uhol+90))
    m2 = y1 + 100 * math.sin(math.radians(360-uhol+90))
    m3 = x1 + 100 * math.cos(math.radians(360-uhol+180+90))
    m4 = y1 + 100 * math.sin(math.radians(360-uhol+180+90))
    
    c.create_oval(x1-100, y1-100, x1+100, y1+100, fill="", outline="black", width=3)
    c.create_oval(l1-7, l2-7, l1+7, l2+7, fill="red", outline="", tags="kruzok")
    c.create_line(l1, l2, l3, l4, width=3)
    c.create_line(m1, m2, m3, m4, width=3)

while True:
    uhol = 0
    while uhol >= -360:
        kruzok(320, 240, uhol)
        ostatne()
        # c.create_oval(x-100, y-100, x+100, y+100, fill="", outline="green", width=2)
        c.tag_raise("kruzok")
        uhol -= 1
        c.update()
        c.after(5)
        c.delete("all")


tkinter.mainloop()