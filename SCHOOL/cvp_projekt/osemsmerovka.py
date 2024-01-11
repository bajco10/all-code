import numpy as np

global_suradnice = [] # suradnice pismen, ktore budem "skrtat"
global_slova = [] # slova, kt. musim najst v osemsmerovke
global_vyskrtnute_slova = [] # slova, kt. som uz nasiel v osemsmerovke

def ziskaj_zadanie(meno_suboru):
    global global_slova
    osems = []
    vtip = []
    with open(meno_suboru, encoding="utf8") as subor:
        for riadok in subor:
            riadok = riadok.strip()
            if riadok == "":
                break
            else:
                global_slova.append(riadok)
        k = 0 # vytvorim si index, ktory sa bude zvacsovat ako pridavam polia (kedze neviem pocet riadkov 8smerovky)
        for riadok in subor:
            riadok = riadok.strip()
            if riadok =="":
                break
            else:
                osems.append([])
                for i in riadok:
                    osems[k].append(i) # vzdy appendujem do novo-vytvoreneho poľa
                k+=1
        for riadok in subor:
            riadok = riadok.strip()
            vtip.append(riadok)
    return osems, vtip

def v_riadku(idx, slovo, osems):
    """
    funkcia, kt. hlada slovo a jeho obratenu verziu v riadkoch
    - pridava do glob. neznamej suradnice , z ktorej sa neskor "skrtaju" pismenka
    - tak isto pridava do glob. neznamej vyskrtnute_slova, ktore potom vyhodim zo slov, kt. este musime najst
    """
    global global_suradnice
    global global_slova
    global global_vyskrtnute_slova
    str_riadok = "".join(osems[idx]) # z poľa písmen si spravim str aby som mohol hľadať index celeho slova
    obratene_slovko = slovo[::-1]
    
    if slovo in str_riadok:
        zaciatok_slova = str_riadok.find(slovo) # najdem index zaciatku slova v danom riadku
        for i in range(len(slovo)): # ziskam suradnice pismen pridavanim k pociatocnemu indexu
            global_suradnice.append((idx, zaciatok_slova)) # pridavam suradnice pismen tohto slova do globalnej premenej
            zaciatok_slova+=1 
        global_vyskrtnute_slova.append(slovo) # pridanie slova do neznamej na neskorsie vyskrtnutie
    elif obratene_slovko in str_riadok: # to iste, len slovo je obratene
        zaciatok_slova = str_riadok.find(obratene_slovko)
        for i in range(len(obratene_slovko)):
            global_suradnice.append((idx, zaciatok_slova))
            zaciatok_slova+=1

def v_stlpci(idx, slovo, osems):
    """
    -> otoci osemsmerovku, takze zo stlpcov sa stanu riadky
    -> idx je v tomto pripade vlastne index stlpca, v kt. chcem hladat
    """
    global global_suradnice
    global global_slova
    global global_vyskrtnute_slova
    m = len(osems) # pocet riadkov povodnej matice
    otocena_osems = np.rot90(osems, k=-1).tolist() # k=-1 mi otoci osesmerovku v smere hod. ruciciek!
    # nova_matica[M-i-1][j] = povodna_matica[j][i]
    # j=idx
    str_riadok = "".join(otocena_osems[idx]) # riadok (stlpec v povodnej osems)
    obratene_slovko = slovo[::-1]

    if slovo in str_riadok: # hladam v stlpci z dola hore
        zaciatok_slova = str_riadok.find(slovo) # najdem kde v stlpci zacina moje slovo
        for i in range(len(slovo)):
            global_suradnice.append((m-zaciatok_slova-1, idx)) # pridavam suradnice do globalnej premenej, pre neskorsie vyskrtnutie
            zaciatok_slova+=1
        global_vyskrtnute_slova.append(slovo)
    
    elif obratene_slovko in str_riadok: # to iste, len pre obratene slovo duh
        zaciatok_slova = str_riadok.find(obratene_slovko)
        for i in range(len(obratene_slovko)):
            global_suradnice.append((m-zaciatok_slova-1, idx))
            zaciatok_slova+=1
        global_vyskrtnute_slova.append(slovo)

def zozen_digy(osems):
    """
    -> spravi mi diagonaly, ktore su v osemsmerovke, ulozi ich do globalnej premenej
    """
    global global_digy_spracovane
    digy = {}
    for i in range(len(osems)):
        for j in range(len(osems[i])):
            if i-j in digy:
                digy[i-j].append(osems[i][j])
            else:
                digy[i-j] = [osems[i][j]]

    # slovnik, kde value je string poskladany z pismen
    global_digy_spracovane = {}
    for key, value in digy.items():
        global_digy_spracovane[key] = "".join(value)

def v_digach(slovo, osems, je_otocena, je_obratene):
    # je_obratene je strasne lenive riesenie :D
    """
    funkcia kt. zistuje:
    -> či sa slovo nachadza v diagonalach
    -> ak ano tak kde v nej sa nachadza a vyrata indexy pismen, z ktorych sa slovo sklada
    -> indexy ulozi do glob. premenej, nasledne sa vyskrtnu
    ! je dolezite, ci je index digy kladny alebo zaporny, pretoze potom zac_slova a idx_digy hraju rozlicne roly
    pri urcovani miesta vyskytu slova !
    """
    global global_suradnice
    global global_slova
    global global_vyskrtnute_slova
    idx_digy = None
    zac_slova = None
    je_tam = False # flag, kedze funkcia robi viac veci, nech zbytocne nehlada slova kt. tam ani niesu...
    for key, value in global_digy_spracovane.items():
        if slovo in value:
            idx_digy = key # vdaka tomuto viem, v ktorej dige sa slovo nachadza
            zac_slova = value.find(slovo) # viem, od akeho indexu sa slovo v dige nachadza, aby som vedel ratat suradnice pismen
            je_tam = True
    if je_otocena:
        if je_tam:
            if idx_digy >= 0:
                y, x = idx_digy+zac_slova, zac_slova
                for p in range(len(slovo)):
                    global_suradnice.append((x, len(osems)-y-1))
                    # suradnice konvertujem -> (stlpec, pocet_riadkov-riadok_pismena-1)
                    y += 1
                    x += 1
                if je_obratene:
                    global_vyskrtnute_slova.append(slovo[::-1])
                else:
                    global_vyskrtnute_slova.append(slovo)
            elif idx_digy < 0:
                y, x = zac_slova, zac_slova+abs(idx_digy)
                for p in range(len(slovo)):
                    global_suradnice.append((x, len(osems)-y-1))
                    y+=1
                    x+=1
                if je_obratene:
                    global_vyskrtnute_slova.append(slovo[::-1])
                else:
                    global_vyskrtnute_slova.append(slovo)
    else: # pre povodnu (neotocenu) osemsmerovku
        if je_tam:
            if idx_digy >= 0:
                y, x = idx_digy+zac_slova, zac_slova
                for p in range(len(slovo)):
                    global_suradnice.append((y, x))
                    # tu nemusim riesit nepekne konvertovanie suradnic
                    y += 1
                    x += 1
                if je_obratene:
                    global_vyskrtnute_slova.append(slovo[::-1])
                else:
                    global_vyskrtnute_slova.append(slovo)
            elif idx_digy < 0:
                y, x = zac_slova, zac_slova+abs(idx_digy)
                for p in range(len(slovo)):
                    global_suradnice.append((y, x))
                    y+=1
                    x+=1
                if je_obratene:
                    global_vyskrtnute_slova.append(slovo[::-1])
                else:
                    global_vyskrtnute_slova.append(slovo)

    

# nacitam si osemsmerovku a vtip
osems, vtip = ziskaj_zadanie("osemsmerovka 25x20 2021.txt") # ("osemsmerovka 12x12.txt") # ("osemsmerovka 21x21.txt") # ("osemsmerovka 25x20 2021.txt")# #  # # 

# najdenie slov v riadkoch
for i in global_slova:
    # ide pre range(pocet riadkov)
    for j in range(len(osems)):
        v_riadku(j, i, osems)
# vyskrtnutie slov, kt. som nasiel v riadkoch
for l in global_vyskrtnute_slova:
    global_slova.remove(l)
global_vyskrtnute_slova = []

# najdenie slov v stlpcoch
for i in global_slova:
    # ide pre range(dlzka riadku -> pocet stlpcov)
    for j in range(len(osems[0])):
        v_stlpci(j, i, osems)
# vyskrtnutie slov, kt. som nasiel v stlpcoch
for c in global_vyskrtnute_slova:
    global_slova.remove(c)
global_vyskrtnute_slova = []

# neotocena osemserovka
zozen_digy(osems) # najdem diagonaly, v ktorych neskor budem hladat
for s in global_slova:
    v_digach(s, osems, False, False)
    v_digach(s[::-1], osems, False, True) # hladanie slov, kt. idu opacne
# vyskrtnutie slov, kt. som nasiel v diagonalach
for c in global_vyskrtnute_slova:
    global_slova.remove(c)
global_vyskrtnute_slova = []
# otocena osemserovka
otocena_osems = np.rot90(osems).tolist() # rotujem osemsmerovku o 90° proti smeru hod. ruciciek
zozen_digy(otocena_osems) # najdem diagonaly, v ktorych neskor budem hladat
for t in global_slova:
    v_digach(t, otocena_osems, True, False)
    v_digach(t[::-1], otocena_osems, True, True)
# nemusim vyskrtavat slova, uz nebudem hladat dalsie :)

# kod pre "skrtanie pismen": 
osems_riesena = osems
for i in global_suradnice:
    osems_riesena[i[0]][i[1]] = "*"

zostali_pismenka = "" # pismena, z ktorych vytvorim riesenie
for j in osems_riesena:
    for i in j:
        if i!="*":
            zostali_pismenka += i

# formatovanie finalneho vystupu
dlzky = vtip[2]
slovicka_riesenia = []
zac = 0
for i in dlzky:
    slovicka_riesenia.append(zostali_pismenka[zac:zac+int(i)])
    zac+=int(i)
print(f"vtip:\n{''.join(vtip[1])}\n{' '.join(slovicka_riesenia)}")


