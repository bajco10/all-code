import tkinter
import math, random

c = tkinter.Canvas(width=800, height=800)
c.pack()
r1=300
minuty = 3
c.create_line( 300, 300,
                  300+r1*math.cos(-math.pi/2 + math.radians(6*minuty)),
                  300+r1*math.sin(-math.pi/2+math.radians(6*minuty)),
                  fill="black", width=4, tags="rucicky"
                  )

tkinter.mainloop()