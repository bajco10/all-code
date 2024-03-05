# cez asci
'''print(ord("a"))
print(ord("b"))
print(ord("A"))
print(ord("B"))'''

# sifruj("Test je super")
def sifruj(text):
    sifrovany = ""
    tlacitka = []
    for znak in text:
        znak = znak.upper()
        if znak == " ":
            sifrovany+= "0" + " "
            tlacitka.append(0)
        elif 64 < ord(znak) < 91:
            kde_v_tlacidku = (ord(znak)-65) % 3 + 1 # +1 aby to boli cisla gombikov, nie indexy
            kde_na_klavesnici = (ord(znak)-65)//3 + 1 # +1 aby to boli cisla gombikov, nie indexy
            tlacitka.append(kde_na_klavesnici)
            konvertovane = str(kde_na_klavesnici) * kde_v_tlacidku
            sifrovany+=konvertovane + " "
        else: 
            sifrovany += znak
    tlacitko_stlacenia = {}
    for i in tlacitka:
        i = str(i)
        if i in tlacitko_stlacenia:
            tlacitko_stlacenia[i] += 1
        else:
            tlacitko_stlacenia[i] = 1

    print(sifrovany)
    print(tlacitka)
    print(tlacitko_stlacenia)


sifruj("jablko ")

'''print((ord("F")-65)%3) # zistim ktore je v tlacitu -> tymto budem nasobit string gombiku
print((ord("F")-65)//3) # zistim, ktory gombik to je -> str() tohto vynasobim tym hore
print(ord("Z"))
# f je treti znak (index - 2) v druhom tlacitku (index - 1)
# pridat do zoznamu cislo'''