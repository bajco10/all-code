# zdroj https://input.sk/python2019/03.html

#1
"""
import tkinter
c = tkinter.Canvas()
c.pack()
x, y = 50, 50
c.create_rectangle(x, y, x+100, y+100, fill="red")
c.create_text(x+50, y+50, text="cerveny", fill="yellow", font="arial 20")
c.create_rectangle(x+110, y, x+210, y+100, fill="blue")
c.create_text(x+160, y+50, text="modry", fill="white", font="arial 20")
tkinter.mainloop()
"""

#2
"""
import tkinter
c = tkinter.Canvas()
c.pack()
x, y = 50, 50
a1, a2, a3 = 180, 150, 50
c.create_rectangle(x, y, x+a1, y+a1, fill="darkred")
c.create_rectangle(x+(a1-a2)/2, y+(a1-a2)/2,x+(a1-a2)/2+a2, y+(a1-a2)/2+a2, fill="cyan")
c.create_rectangle(x+(a1-a3)/2, y+(a1-a3)/2, x+(a1-a3)/2+a3, y+(a1-a3)/2+a3, fill="salmon")
c.create_text(x-5, y-5, text="A")
c.create_text(x+a1+5, y-5, text="B")
c.create_text(x+a1+5, y+a1+5, text="C")
c.create_text(x-5, y+a1+5, text="D")
tkinter.mainloop()
"""
#3
"""
import tkinter as tk
canvas = tk.Canvas(width=800, height=600, bg="white")
canvas.pack()
strana1 = 135
strana2 = 90
# nemecko
canvas.create_rectangle(10, 10, 10+(strana1), 10+(strana2/3), fill="black")
canvas.create_rectangle(10, 10+(strana2/3), 10+strana1, 10+2*(strana2/3), fill="red")
canvas.create_rectangle(10, 10+2*(strana2/3), 10+strana1, 10+strana2, fill="yellow")
# rusko
canvas.create_rectangle(200, 140, 200+(strana1), 140+(strana2/3), fill="white")
canvas.create_rectangle(200, 140+(strana2/3), 200+strana1, 140+2*(strana2/3), fill="blue")
canvas.create_rectangle(200, 140+2*(strana2/3), 200+strana1, 140+strana2, fill="red")
# francuzko
canvas.create_rectangle(10, 140, 10+(strana1/3), 140+strana2, fill="blue")
canvas.create_rectangle(10+(strana1/3), 140, 10+2*(strana1/3), 140+strana2, fill="white")
canvas.create_rectangle(10+2*(strana1/3), 140, 10+strana1, 140+strana2,fill="red")
# taliansko
canvas.create_rectangle(200, 10, 200+(strana1/3), 10+strana2, fill="green")
canvas.create_rectangle(200+(strana1/3), 10, 200+2*(strana1/3), 10+strana2, fill="white")
canvas.create_rectangle(200+2*(strana1/3), 10, 200+strana1, 10+strana2, fill="red")
canvas.mainloop()
"""

