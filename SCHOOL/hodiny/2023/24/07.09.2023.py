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
"""
import tkinter
c = tkinter.Canvas()
c.pack()
def kresli(meno_suboru):
    with open(f"python/SCHOOL/hodiny/2023/24/{meno_suboru}", encoding="UTF-8") as subor:
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
#pouzity ten isty subor ako v 7 ale zmeneny - preto 7 nejde
"""import tkinter
c = tkinter.Canvas()
c.pack()"""
# python/SCHOOL/hodiny/2023/24/body.txt
"""def kresli(meno_suboru):
    with open(f"python/SCHOOL/hodiny/2023/24/{meno_suboru}", encoding="UTF-8") as subor:
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
c.mainloop()"""
#9
"""
# subor na generaciu farieb
import random, tkinter
c = tkinter.Canvas()
c.pack()

far=["blue", "green", "yellow", "red"]
subor = open("/home/tomas/Desktop/all-code/SCHOOL/hodiny/2023/24/farby.txt", "w")
for i in range(40):
    print(random.choice(far), file=subor)
subor.close()

def do_riadkov(sirka):
    with open(f"/home/tomas/Desktop/all-code/SCHOOL/hodiny/2023/24/farby.txt", encoding="UTF-8") as subor:
        x, y = 0, 0
        l = subor.readlines()
        n = 0
        #print(l)
        for i in l:
            i = i.strip()
            if n==sirka:
                x=0
                y+=30
                n=0
            else:
                c.create_rectangle(x, y, x+30, y+30, fill=i)
                x+=30
                n+=1

do_riadkov(6)
c.mainloop()
"""   
#10
"""def vypis_slova(meno_suboru):
    with open(f"/home/tomas/Desktop/all-code/SCHOOL/hodiny/2023/24/{meno_suboru}", encoding="UTF-8") as subor:
        n = 0
        m = 0
        for riadok in subor:
            #riadok = riadok.replace("\n", "")
            riadok = riadok.strip()
            if m != n:
                print(riadok, end=" ")
                m+=1
            elif m==n:
                print(riadok)
                m=0
                n+=1
vypis_slova("slova.txt")"""
#11
"""import random
def nahodne_cisla(meno_suboru, pocet):
    subor = open(f"python/SCHOOL/hodiny/2023/24/{meno_suboru}", "w")
    for i in range(pocet+1):
        print(random.randrange(100, 999), file=subor)
    subor.close()

nahodne_cisla("nahodne_cisla.txt", 5)"""

#12
"""def vyrob(meno_suboru, text):
    subor = open(f"python/SCHOOL/hodiny/2023/24/{meno_suboru}", "w")
    s = f"for i in range(100): print('{text}')"
    subor.write(s)
    subor.close()
vyrob("skript.py", "programujem v pythone")"""
#13
"""subor = open(f"python/SCHOOL/hodiny/2023/24/pridavanie.txt", "w")
subor.write("prvy riadok\ndruhy riadok\n")
subor.close()
def pridaj(meno_suboru, text):
    subor = open(f"python/SCHOOL/hodiny/2023/24/{meno_suboru}", "a")
    subor.write(text+"\n")
    subor.close()

pridaj("pridavanie.txt", "predposledny")
pridaj("pridavanie.txt", "posledny riadok")"""
#13-stazena
# subor = open(f"/home/tomas/Desktop/all-code/SCHOOL/hodiny/2023/24/farby.txt")
import random
def pridaj():
    farby = ["red", "green", "blue"]
    subor = open(f"/home/tomas/Desktop/all-code/SCHOOL/hodiny/2023/24/farby.txt", "a")
    for i in range(4):
        subor.write(random.choice(farby)+"\n")
    subor.close()
pridaj()
#14 - dorobit :)
"""def vyhod_riadok(meno_suboru, index):
    subor = f"python/SCHOOL"""










