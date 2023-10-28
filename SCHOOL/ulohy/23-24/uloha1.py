with open("SCHOOL/ulohy/22-23/priklady.txt", "r") as subor:
    priklady = []
    for riadok in subor:
        riadok = riadok.strip()
        riadok_orig = riadok.replace(" ", "")
        riadok = riadok.replace(" ", "")
        if "+" in riadok:
            # iadok = riadok.replace(" ", "")
            riadok = riadok.replace("+", " ")
            riadok = riadok.replace("=", "")
            a, b = riadok.split(" ")
            if 0<int(a)+int(b)<100:
                priklady.append(riadok_orig+str(int(a)+int(b)))
        elif "-" in riadok:
            # riadok = riadok.replace(" ", "")
            riadok = riadok.replace("-", " ")
            riadok = riadok.replace("=", "")
            a, b = riadok.split(" ")
            if 0<int(a)-int(b)<100:
                priklady.append(riadok_orig+str(int(a)-int(b)))
print(priklady)
with open("SCHOOL/ulohy/22-23/priklady.txt", "w") as subor:
    for i in priklady:
        print(i, file=subor)