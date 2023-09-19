# cvp
"""import tkinter
c = tkinter.Canvas()
c.pack()
def kresli():
    with open(f"/home/tomas/Desktop/all-code/SCHOOL/hodiny/2023/24/aster.orava.sk_files_cotuje.txt") as subor:
        x,y, n = 0, 0, 0
        s, v = 0, 0
        for riadok in subor:
            riadok = riadok.replace("\n", "")
            # print(len(riadok)/6)
            for i in range(len(riadok)//6):
                a = 6*i
                b = a+6
                farba = f"#{riadok[a:b]}"
                print(farba)
                c.create_rectangle(x, y, x+1, y+1, fill=farba, outline="")
                x+=1
                n+=6
            s=x
            x=0
            y+=1
        v = y
    c["width"]=s
    c["height"]=v

kresli()"""

"""import tkinter
c = tkinter.Canvas()
c.pack()
def kresli():
    with open(f"/home/tomas/Desktop/all-code/SCHOOL/hodiny/2023/24/aster.orava.sk_files_cotuje.txt") as subor:
        x,y, n = 0, 0, 0
        s, v = 0, 0
        for riadok in subor:
            riadok = riadok.replace("\n", "")
            # print(len(riadok)/6)
            for i in range(len(riadok)//6):
                a = 6*i
                b = a+6
                farba = f"{riadok[a:b]}"
                r = f"{int(farba[:2], 16):03d}"
                g = f"{int(farba[2:4], 16):03d}"
                b = f"{int(farba[4:6], 16):03d}"
                # m = max(r, g, b)
                m = (int(r)+int(g)+int(b))//3
                farba = f"{int(m):02x}{int(m):02x}{int(m):02x}"
                print(farba)
                c.create_rectangle(x, y, x+1, y+1, fill="#"+farba, outline="")
                x+=1
                n+=6
            s=x
            x=0
            y+=1
        v = y
    c["width"]=s
    c["height"]=v

kresli()

c.mainloop()"""

import tkinter
c = tkinter.Canvas()
c.pack()
def kresli():
    with open(f"/home/tomas/Desktop/all-code/SCHOOL/hodiny/2023/24/aster.orava.sk_files_cotuje.txt") as subor:
        x,y, n = 0, 0, 0
        s, v = 0, 0
        for riadok in subor:
            riadok = riadok.replace("\n", "")
            # print(len(riadok)/6)
            for i in range(len(riadok)//6):
                a = 6*i
                b = a+6
                farba = f"{riadok[a:b]}"
                r = f"{int(farba[:2], 16):03d}"
                g = f"{int(farba[2:4], 16):03d}"
                b = f"{int(farba[4:6], 16):03d}"
                # m = max(r, g, b)
                #m = (int(r)+int(g)+int(b))//3
                r = abs(255-int(r))
                g = abs(255-int(g))
                b = abs(255-int(b))
                farba = f"{int(r):02x}{int(g):02x}{int(b):02x}"
                print(farba)
                c.create_rectangle(x, y, x+1, y+1, fill="#"+farba, outline="")
                x+=1
                n+=6
            s=x
            x=0
            y+=1
        v = y
    c["width"]=s
    c["height"]=v

kresli()

c.mainloop()

import random
subor = open("SCHOOL/hodiny/2023/24/ciselka.txt", "w")
for i in range(11):
    print(random.randrange(1, 100, 2), random.randrange(1, 100, 2)-1, file=subor)
subor.close()
subor = open("SCHOOL/hodiny/2023/24/ciselka.txt")

def nsd(a, b):
    while b:
        a, b = b, a%b
    return a

for riadok in subor:
    riadok=riadok.strip()
    cisla = riadok.split(" ")
    a, b = int(cisla[0]), int(cisla[1])
    x = nsd(a, b)
    print(f"NSD({a}, {b})={nsd(a, b)}")

