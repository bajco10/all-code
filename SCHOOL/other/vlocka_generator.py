import tkinter, math, random

c = tkinter.Canvas(width=1900, height=1900)
c.pack()

x, y, r1 = 450, 450, 400



def kruzok(x, y, r1, uhol, i):
    c.create_oval(x-r1, y-r1, x+r1, y+r1, tags="k")
    r2 = r1/2
    r3 = r2/2
    r4 = r3/2
    r5 = r4/2
    r6 = r5/2
    r7 = r6/2
    r8 = r7/2
    r9 = r8/2
    r10 = r9/2
    r11 = r10/2
    r12 = r11/2

    r1-=r2
    x1 = x + r1*math.cos(math.radians(i**1)*(uhol))
    y1 = y + r1*math.sin(math.radians(i**1)*(uhol))
    r2-=r3
    x2 = x1 + r2*math.cos(math.radians(-i**2)*(uhol))
    y2 = y1 + r2*math.sin(math.radians(-i**2)*(uhol))
    r3-=r4
    x3 = x2 + r3*math.cos(math.radians(i**3)*(uhol))
    y3 = y2 + r3*math.sin(math.radians(i**3)*(uhol))
    r4-=r5
    x4 = x3 + r4*math.cos(math.radians(-i**4)*(uhol))
    y4 = y3 + r4*math.sin(math.radians(-i**4)*(uhol))
    r5-=r6
    x5 = x4 + r5*math.cos(math.radians(i**5)*(uhol))
    y5 = y4 + r5*math.sin(math.radians(i**5)*(uhol))
    r6-=r7
    x6 = x5 + r6*math.cos(math.radians(-i**6)*(uhol))
    y6 = y5 + r6*math.sin(math.radians(-i**6)*(uhol))
    r7-=r8
    x7 = x6 + r7*math.cos(math.radians(i**7)*(uhol))
    y7 = y6 + r7*math.sin(math.radians(i**7)*(uhol))
    r8-=r9
    x8 = x7 + r8*math.cos(math.radians(-i**8)*(uhol))
    y8 = y7 + r8*math.sin(math.radians(-i**8)*(uhol))
    r9-=r10
    x9 = x8 + r9*math.cos(math.radians(i**9)*(uhol))
    y9 = y8 + r9*math.sin(math.radians(i**9)*(uhol))
    r10-=r11
    x10 = x9 + r10*math.cos(math.radians(-i**10)*(uhol))
    y10 = y9 + r10*math.sin(math.radians(-i**10)*(uhol))
    r11-=r12
    x11 = x10 + r11*math.cos(math.radians(i**11)*(uhol))
    y11 = y10 + r11*math.sin(math.radians(i**11)*(uhol))
    return x11, y11


    
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

n =  random.choice(primes)
print(n)

while True:
    uhol = 0
    while True:
        # kruzok(x, y, 400, 200, 100, 50, 25, 15, 8, 4, uhol, 1.5)
        uhol+=1
        # kruzok(x, y, 400, 200, 100, 50, 25, 15, 8, 4, uhol, 1.5)
        c.create_line(kruzok(x, y, 400, uhol, n), kruzok(x, y, 400, uhol-1, n), width=0.3)
        #c.create_line(kruzok(x, y, 400, 200, 100, 50, 25, 12.5, 6.25, 3.125, 1.5625, 0.78125, 0.390625, 0.1953125, uhol, n), kruzok(x, y, 400, 200, 100, 50, 25, 12.5, 6.25, 3.125, 1.5625, 0.78125, 0.390625, 0.1953125, uhol-1, n), width=1)
        c.after(0)
        c.update()
        c.delete("k")
tkinter.mainloop()

"""
for i in range(1, 12):
    if i%2==0:
        print(f"r{i}-=r{i+1}")
        print(f"x{i} = x{i-1} + r{i}*math.cos(math.radians(i**{-i})*(uhol))")
        print(f"y{i} = y{i-1} + r{i}*math.sin(math.radians(i**{-i})*(uhol))")
    else:
        print(f"r{i}-=r{i+1}")
        print(f"x{i} = x{i-1} + r{i}*math.cos(math.radians(i**{i})*(uhol))")
        print(f"y{i} = y{i-1} + r{i}*math.sin(math.radians(i**{i})*(uhol))")
    # print(f"r{i+1}-=r{i+2}")
    # print(f"x{i+1} = x{i} + r{i+1}*math.cos(math.radians(i**{-(i+1)})*(uhol))")
    # print(f"y{i+1} = y{i} + r{i+1}*math.sin(math.radians(i**{-(i+1)})*(uhol))")
"""
