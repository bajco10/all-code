def bez_medzier(slovo):
    return slovo.replace(" ","")
nove = bez_medzier('Mon   tyPy thon    ')
#11
def nahrad_samo(text, znaky):
    text_novy = ""
    for i in text:
        if i in ("aeiou"):
            i=znaky
        text_novy += i
    return text_novy


xd = nahrad_samo("sedi mucha na stene", "uo")
#12 - zakaz pouzitia formatovania
def do_desiatkovej(cislo):
    slovo=""
    if cislo < 0:
        pom = "-"
        cislo = abs(cislo)
    else: 
        slovo = ""
        pom=""
    while cislo > 0:
        cifra = cislo%10
        cislo = cislo //10
        slovo += str(cifra)
    print(pom+slovo)

# do_desiatkovej(-14561)

# 13 - dorobit tak nech ide pre desatine cisla (negativne indexy "i")
def zo_sestnastkovej(retazec):
    retazec = retazec.upper()
    hex_digits="0123456789ABCDEF"
    if "." in retazec:
        cele, desatine = retazec.split(".")
    else:
        cele, desatine = retazec, ""
    
    desiatkove_cele = 0
    for i in range(len(cele)):
        mocnina = len(cele) -1 -i
        cislica = hex_digits.index(cele[i])
        desiatkove_cele += cislica * (16**mocnina)
    
    if desatine:
        desiatkove_desatine = 0
        for i in range(len(desatine)):
            mocnina = -(i+1)
            cislica = hex_digits.index(desatine[i])
            desiatkove_desatine += cislica * (16**mocnina)
        desiatkove_cele += desiatkove_desatine
    return desiatkove_cele

print(zo_sestnastkovej("3.14A7"))



#14
"""def rozsekaj(text, sirka):
    for i in range(0, len(text), sirka):
        print(f"{text[i:i+sirka]:^20}")"""

# rozsekaj("Anicka dusicka, kde si bola", 5)

#15
"""def sifra2(text):
    n_text = ""
    for i in range(0, len(text), 2):
        if i+1 >= len(text):
            n_text+= text[i:i+1]
        else:
            n_text+= (text[i+1:i+2] + text[i:i+1])
    print(n_text)"""

# sifra2("programujem")
# sifra2("rpgoarumejm")

#16 - dorobit!
# print(ord("A"), ord("Z"), ord("a"), ord("z"))
def sifra1(text, x):
    novy_text=""
    for i in text:
        if ord(i)+x > 90:
            novy_text += str((chr(ord(i)+x-(25))))
        elif  ord(i)+x > 90:
            novy_text += str((chr(ord(i)+x)-26))
    return novy_text

"""print(sifra1("python", 1))
print(sifra1("qzuipo", -1))"""