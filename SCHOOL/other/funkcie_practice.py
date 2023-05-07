import tkinter
import random
canvas = tkinter.Canvas()
canvas.pack()
def farba_generator():
    return f"#{random.randrange(255**3):06x}"
def stvorec_maker(x, y, x1, y1, farba):
    canvas.create_rectangle(x, y, x1, y1, fill=farba)

for x in range(20, 230, 35):
    for y in range(20, 230, 35):
        stvorec_maker(x, y, x+30, y+30, farba=farba_generator())
 
tkinter.mainloop()

def fibonacci(n):
    a, b = 0, 1
    while n:
        a, b = b, a+b
        n -= 1
    return a

print(fibonacci(23))