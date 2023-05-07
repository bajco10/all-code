import tkinter, math


def kocka(x, y, strana):
    a = [x, y+strana]
    b = [x+strana, y+strana]
    c = [x+strana, y]
    d = [x, y]
    
    x1 = x + (3/5)*strana*math.cos(math.radians(-50))
    y1 = y + (3/5)*strana*math.sin(math.radians(-50))

    e = [x1, y1+strana]
    f = [x1+strana, y1+strana]
    g = [x1+strana, y1]
    h = [x1, y1]

    """
    #body
    m = 0
    for i in a, b, c, d, e, f, g, h:
        body = ["A", "B", "C", "D", "E", "F", "G", "H"]
        i[0]+=20
        i[1]+=20
        canvas.create_text(i, text=body[m], font="arial 20")
        m+=1
    """
    
    canvas.create_line(a, b, c, d, a, width=2)
    # canvas.create_line(e, f, g, h, e, width=2)
    canvas.create_line(d, h, width=2)
    canvas.create_line(c, g, width=2)
    canvas.create_line(b, f, width=2)
    canvas.create_line(h, g, width=2)
    canvas.create_line(f, g, width=2)
    canvas.create_line(a, e, width=2, dash=(5, 3))
    canvas.create_line(e, f, width=2, dash=(5, 3))
    canvas.create_line(e, h, width=2, dash=(5, 3))



canvas = tkinter.Canvas(width=800, height=600)
canvas.pack()

kocka(200, 200, 300)

canvas.mainloop()