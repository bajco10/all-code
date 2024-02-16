import matplotlib.pyplot as ppt
subor = open("NRSR2023.csv", encoding="utf-8-sig")

strany_hlasy = {}

for riadok in subor:
    riadok = riadok.strip()
    # riadok.replace('"', '')
    veci = riadok.split(",")
    for vec in veci:
        treba = True
        if '""' in vec:
            strana = vec
            treba = False
    if treba:
        strana = veci[7]
    # print(strana)
    if strana in strany_hlasy:
        strany_hlasy[strana] += 1
    else:
        strany_hlasy[strana] = 1

for strana, pocet_hlasov in strany_hlasy.items():
    print(strana, pocet_hlasov)



