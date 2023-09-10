"""#otvorenie suboru do pythonu
subor = open("/home/tomas/Desktop/python/SCHOOL/hodiny/2023/24/subor.txt", encoding="UTF-8")
#citanie jednotlivych riadkov
x = subor.readline()
print(x.strip())
y = subor.readline()
print(y.strip())

#najjednoduchsie otvaranie suboru
for riadok in subor:
    print(riadok.strip())

subor.close()
#ina moznost ako otvorit subor pre pracu
with open("SCHOOL/hodiny/2023/24/subor.txt", encoding="utf8") as subor:
    for riadok in subor:
        print(riadok.strip())

#umiestnenie celeho suboru do jednej eznamen
cely_subor = subor.read()

#otvorenie suboru pre zapis do neho
#subor = open("SCHOOL/hodiny/2023/24/subor.txt", "w")

#pisane do suboru cez print
subor = open("SCHOOL/hodiny/2023/24/subor.txt", "w")
import random
for i in range(100):
    print(random.randint(1, 100), file=subor)
subor.close"""

#cvicenia - Input
#2 - kodovanie nie je v tomto pripade treba
"""s = input("zadaj meno suboru: ")
subor = open(f"SCHOOL/hodiny/2023/24/{s}", "r")
n = 0
m = 0
for riadok in subor:
    if len(riadok) > m:
        m = len(riadok)
    n+=1
print(f"meno suboru: {s}")
print(f"pocet riadok suboru: {n}")
print(f"najdlhsi ma {m} znakov")"""
#3
"""def riadky_s_textom(meno_suboru, text):
    with open(f"SCHOOL/hodiny/2023/24/{meno_suboru}", encoding="UTF-8") as subor:
        for riadok in subor:
            if text in riadok:
                print(riadok)

riadky_s_textom("text2.txt", "for")"""
#4
"""def posledny_riadok(meno_suboru):
    with open(f"SCHOOL/hodiny/2023/24/{meno_suboru}", encoding="UTF-8") as subor:
        x = subor.readlines()
        n = 0
        idx = 0
        for riadok in x:
            #print(x.index(riadok), len(riadok))
            if len(riadok)>n:
                n = len(riadok)
                idx = x.index(riadok)
        print(f"posledny riadok:\n {x[-1]}")
        print(f"predposledny riadok:\n {x[-2]}")
        print(f"najdlhsi riadok:\n {x[idx]}")
posledny_riadok("text1.txt")"""
#5
"""def priemer(meno_suboru):
    with open(f"SCHOOL/hodiny/2023/24/{meno_suboru}", encoding="UTF-8") as subor:
        x, n = 0, 0
        for riadok in subor:
            x += int(riadok)
            n+=1
        print(f"priemer = {x/n}")
priemer("text3.txt")"""
#6
"""import tkinter
c = tkinter.Canvas()
c.pack()

def vypis_subor(meno_suboru):
    x, y = 0, 0
    with open(f"SCHOOL/hodiny/2023/24/{meno_suboru}", encoding="UTF-8") as subor:
        for riadok in subor:
            c.create_text(x, y, text=riadok, font="arial 12", anchor="nw")
            y+=20

vypis_subor("text2.txt")
c.mainloop()"""
#7
"""import tkinter
c = tkinter.Canvas()
c.pack()
def kresli(meno_suboru):
    with open(f"SCHOOL/hodiny/2023/24/{meno_suboru}", encoding="UTF-8") as subor:
        body = []
        for riadok in subor:
            riadok = riadok.replace("\n", "")
            print(riadok)
            body.append(riadok.split(" "))
        print(body)
        for i in range(len(body)-1):
            c.create_line(body[i], body[i+1], width=2)
kresli("body.txt")
c.mainloop()"""
#8
import tkinter
c = tkinter.Canvas()
c.pack()
def kresli(meno_suboru):
    with open(f"SCHOOL/hodiny/2023/24/{meno_suboru}", encoding="UTF-8") as subor:
        body = []
        for riadok in subor:
            for i in riadok:
                if i !=" ":
                    riadok = riadok.replace("\n", "")
                    body.append(riadok.split(" "))
                    break
                body.append(" ")
        # print(body)
        for i in range(len(body)-1):
            if len(body[i]) !=1 and len(body[i+1]) != 1:
                print(body[i], body[i+1])
                c.create_line(body[i], body[i+1])
                
kresli("body.txt")
c.mainloop()






