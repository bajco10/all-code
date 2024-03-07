# kolko zakaznikov bolo
# pomer ano ku nie
# kolko entries v jednotlive dni
# v ktoru hodinu bolo najvic nespokojnych


pocet_dni = 0
ano, nie = 0, 0
dni_entries = {}
hodina_nespokojnych = {}
cas_na_porovnanie = 23*60 + 59
den = 0
with open("spokojnost.txt") as subor:
    for riadok in subor:
        riadok = riadok.strip()
        pocet_dni += 1
        cas, spokojnost = riadok.split(" ")
        hodina, minuty = cas.split(":")
        casik = int(hodina)*60 + int(minuty)
        if casik < cas_na_porovnanie:
            den += 1
            cas_na_porovnanie = casik
        else:
            cas_na_porovnanie = casik

            
        if spokojnost == "ano":
            ano += 1
        else:
            nie += 1
            if hodina in hodina_nespokojnych:
                hodina_nespokojnych[hodina] += 1
            else:
                hodina_nespokojnych[hodina] = 1
        
        if den in dni_entries:
            dni_entries[den] += 1
        else:
            dni_entries[den] = 1
    print(f"ano: {ano} / nie: {nie}")
    x = 0
    for hodina, pocet in sorted(hodina_nespokojnych.items(), key = lambda x:x[1], reverse=True):
        if x < 1:
            print(f"najnespokojnesi boli v {hodina}, presne {pocet} nespokojnych zakaznikov")
        x+=1
#    for den, pocet in dni_entries.items():
#        print(f"Den č. {den} - nespokojnych {pocet} zakaznikov.")



