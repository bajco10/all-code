karticky = input().split(" ")

for i in range(5):
    karticky[i] = int(karticky[i])

def pozitivne(ls):
    c = 0
    for i in ls:
        if i < 0:
            c += 1
    return c==5

def najvacsie_kombo(ls):
    najv = 0
    if pozitivne(ls):
        return max(ls)
    else:
        for i in ls:
            if i > 0:
                najv += i
    return najv

print(najvacsie_kombo(karticky))

