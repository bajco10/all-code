with open(r"/home/tomas/Desktop/all-code/SCHOOL/ulohy/23-24/znamky.txt", "r") as subor:
    riadky = subor.readlines() 
    predmety = riadky[0].strip().split(" ") # rozdelim si prvy riadok suboru na predmety
    predmety_priemery = {} # slovnik na ulozenie priemeru kazdeho predmetu
    predmety_pocet_znamok = {} # slovnik na ulozenie poctu znamok kazdeho predmetu (dolezite kvoli nenapisanym testom-> "x")
    ziaci={} # slovnik na ulozenie mena ziaka a jeho priemeru znamok

    for predmet in predmety: 
        predmety_priemery[predmet] = 0 
        predmety_pocet_znamok[predmet] = 0
    
    riadky.pop(0) # vymazem prvy riadok z listu readlines, kedze predmety som uz spracoval
    for riadok in riadky:
        riadok = riadok.strip() # odstranenie \n
        for i in riadok:
            if i in "0123456789": # ak je i cislica tak viem ze uz som za menom -> mozem rozseknut riadok podla indexu tohto i
                idx = riadok.index(i) 
                meno, znamky = riadok[:idx-1], riadok[idx:] # rozseknutie riadku
                znamky_list = znamky.split() # rozdelenie znamok do listu aby som nevedel vyselektovat cislice od x
                sucet, pocet_z, priemer, idx_predmetu, znamok_z_predmetu=0, 0, 0, 0, 0 
                # sucet -> sucet znamok jedinca
                # pocet_z -> pocet znamok jedinca (neratam x)
                # idx_predmetu -> neznama na zlepsenie readability
                # znamok_z_predmetu -> odkladam si pocet znamok z kazdeho predmetu, aby som vedel spravit priemery
            
                for j in znamky_list:
                        if j != "x":
                            pocet_z+=1
                            sucet += int(j)
                            # pouzivam list predmety, aby som "vytvoril" "indexovanie" v slovniku 
                            # -> vdaka poradiu znamky viem z akeho predmetu znamka je 
                            # -> viem na ktorom indexe v mojom liste je tento predmet
                            # -> vdaka tomuto indexu zistim meno predmetu do ktoreho idem scitavat/priratavat
                            predmety_priemery[f"{predmety[idx_predmetu]}"] += int(j) # pre kluc naprd."Matematika" zvysim sucet znamok o danu hodnotu j
                            predmety_pocet_znamok[f"{predmety[idx_predmetu]}"] += 1 # pre kluc naprd."Matematika" zvysim celkovy pocet znamok z predmetu o 1
                        idx_predmetu +=1 
                priemer = sucet/pocet_z # vyratam priemer znamok kazdeho ziaka
                ziaci[meno] = round(priemer, 2) # priradim priemer znamok ziaka ku jeho menu
                break # keby nedam break pokracuje mi program aj po prvej najdenej znamke (if i in "0123456789")

            
    for key, value in predmety_priemery.items():
        predmety_priemery[key] = round(int(value)/int(predmety_pocet_znamok[key]), 2) # priradujem priemery z predmetov ku ich menam
    
    # moze sa stat ze viac ako 1 ziak bude mat najmänsi priemer
    # to iste plati aj pre predmety ale je to ovela menej pravdepodobne
    najlepsi_ziaci = [key for key,value in ziaci.items() if value==min(ziaci.values())]
    najlepsi_predmet = min(predmety_priemery, key=predmety_priemery.get)
    print(f"Najlepší priemer známok {min(ziaci.values())} má/majú: {', '.join(najlepsi_ziaci)}")
    print(f"Najlepšie výsledky boli dosiahnuté v predmete: {najlepsi_predmet}")
        
