# heslo -> "covid"
def ziskaj_text():
    text = ""
    with open("text.txt", encoding="utf8") as subor:
        for riadok in subor:
            text += riadok
    return text

def ziskaj_tabulku():
    tabulka = {}
    with open("tabulka.txt", encoding="utf8") as subor:
        je_prvy = True
        for riadok in subor:
            if je_prvy:
                abc = riadok.strip().split(" ")
                je_prvy = False
            else:
                riadok = riadok.strip().split(" ")
                kluc = riadok[0]
                tabulka[kluc] = riadok[1:]
                # print(kluc, "-", tabulka[kluc])
    return tabulka, abc
def desifruj(text, heslo):
    heslo = heslo.upper()
    tabulka, abc = ziskaj_tabulku()
    idx_heslo=0
    novy_text = ""
    for znak in text:
        if idx_heslo > len(heslo) - 1:
            idx_heslo = 0
        if znak.upper() in abc:
            kluc = heslo[idx_heslo]
            index_v_abc = tabulka[kluc].index(znak)
            novy_text += abc[index_v_abc]
            idx_heslo+=1
        else:
            novy_text += znak
    return novy_text

print(desifruj(ziskaj_text(), "covid"))
        

    

ziskaj_tabulku()