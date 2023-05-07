import tkinter
import math
c = tkinter.Canvas(width=600, height=600)
c.pack()
r1, r2 = 90, 70
def hodiny(minuty, sekundy):
    c.create_rectangle(200, 100, 400, 175)
    c.create_oval(200, 200, 400, 400)
    c.create_text(300, 140, text=f"{minuty:02} : {sekundy:02}", font="helvetica 45", tags="hodiny")
    c.create_line( 300, 300,
                  300+r1*math.cos(-math.pi/2 + math.radians(6*minuty)),
                  300+r1*math.sin(-math.pi/2+math.radians(6*minuty)),
                  fill="black", width=4, tags="rucicky"
                  )
    c.create_line(300, 300, 
                  300+r2*math.cos(-math.pi/2+math.radians(6*sekundy)),
                  300+r2*math.sin(-math.pi/2+math.radians(6*sekundy)),
                  fill="red", width=3, tags="rucicky"
                  )

zaciatok = 1
minuty = zaciatok
sekundy = 0
aktiv = True
while aktiv:
    hodiny(minuty, sekundy)
    c.update()
    c.after(1000)
    if minuty == 0 and sekundy == 0:
        c.delete("all")
        c.create_text(300, 300, text="Dobru chut!", font="calibri 90")
        c.update()
        aktiv=False
    else:
        c.delete("rucicky", "hodiny")
        c.update()
    sekundy-=1
    if sekundy < 0:
        sekundy=59
        minuty-=1
tkinter.mainloop()