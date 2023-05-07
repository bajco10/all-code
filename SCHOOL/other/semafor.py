import tkinter
c = tkinter.Canvas(width=700, height=700)
c.pack()
c.create_rectangle(280, 100, 420, 440, fill="black")
c.create_oval(300, 110, 400, 210, fill="#450a0a")
c.create_oval(300, 220, 400, 320, fill="#8B4000")
c.create_oval(300, 330, 400, 430, fill="#0a450a")
n = 5
while True:
    for i in range(n, 0, -1):
        c.create_oval(300, 110, 400, 210, fill="red", tags="cervena")
        c.create_text(350, 160, text=i, tags="t", font="arial 30")
        c.update()
        c.after(1000)
        c.delete("t")
        c.create_text(350, 160, text=i, tags="t", font="arial 30")
        c.update()
        if i ==1:
            c.create_oval(300, 220, 400, 320, fill="orange", tags="orange")
            c.delete("t")
            c.update()
            c.after(500)
            c.delete("cervena", "orange")
            c.update()
    for i in range(n, 0, -1):
        c.create_oval(300, 330, 400, 430, fill="green", tags="zelena")
        c.create_text(350, 380, text=i, tags="t", font="arial 30")
        c.update()
        c.after(1000)
        c.delete("t")
        c.create_text(350, 380, text=i, tags="t", font="arial 30")
        c.update()
        if i == 1:
            c.delete("zelena", "t")
            c.update()
    c.create_oval(300, 220, 400, 320, fill="orange", tags="orange")
    c.update()
    c.after(500)
    c.delete("orange")
    c.create_oval(300, 110, 400, 210, fill="red", tags="cervena")
    c.update()
tkinter.mainloop()