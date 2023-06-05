#1

#kodovanie cisel cez indexy sifroveho "kluca"
# volanie funkcie: sifruj("jablko je cervene", 903)
#je to tak 95%reprezentacia testu
def sifruj(ret, kluc):
    abc_m = "abcdefghijklmnopqrstuvwxyz"
    abc_v = abc_m.upper()
    k = 0
    res=""
    kluc = str(kluc)
    for i in ret:
        if k >= len(kluc):
            k = 0
        if i in abc_m:
            if abc_m.find(i)+int(kluc[k]) > len(abc_m):
                abc_m = abc_m*2
            x = abc_m.find(i)+int(kluc[k])
            res+=abc_m[x]
            k+=1
        elif i in abc_v:
            if abc_v.find(i)+int(kluc[k]) > len(abc_v):
                abc_v = abc_v*2
            y = abc_v.find(i)+int(kluc[k])
            res+=abc_v[y]
            k+=1
        else:
            res+=i
    return res

#print(sifruj("Janko", 12))
#print(sifruj("jablko je cervene", 903))

#2 - riesenie s listom! - ten .split() sa da nahradit for-loopom ktory hlada medzery atd.

#zadany retazec s farbami a velkostami, ak nie je velkost tak je 30px
#volanie funkcie: kresli("200emiL60elpruP50deR100atnegaM")
#hlada podla velkych pismen

import tkinter
c = tkinter.Canvas(width=600, height=400)
c.pack()
def kresli(ret):
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ret = ret[::-1]
    for i in ret:
        if i in abc:
            ret = ret.replace(i, f" {i}")
    farby = ret.split(" ")
    x, y = 100, 200
    for i in farby:
        cislo = ""
        if i!="":
            for j in i.lower():
                if j in "0123456789":
                    cislo+=j
            i = i.replace(cislo, "")
            if cislo!="":
                c.create_oval(x, y-int(cislo[::-1])/2, x+int(cislo[::-1]), y+int(cislo[::-1])/2, fill=i)
                x+=int(cislo[::-1])
            else:
                c.create_oval(x, y-15, x+30, y+15, fill=i)
                x+=30
#kresli("200emiL60elpruP50deR100atnegaM")
#kresli("BlueRedBlackGold"[::-1])
kresli("RedGoldPurpleCyan09"[::-1])
c.mainloop()


