#2
"""def porovnaj(slovo1, slovo2):
    if slovo1 > slovo2:
        return f"{slovo1} > {slovo2}"
    elif slovo1 < slovo2:
        return f"{slovo1} < {slovo2}"
    else:
        return f"{slovo1} = {slovo2}"

print(porovnaj("abc", "def"))"""
#3-6 su primitivne
#7
"""def vypis(retazec):
    for i in range(len(retazec)):
        print(i, retazec[i], ord(retazec[i]), chr(ord(retazec[i])+1))

vypis('Monty Python')"""
#8
"""def pocet(retazec, podretazec):
    c = 0
    dr = len(retazec)
    dp = len(podretazec)
    for i in range(dr-dp+1):
        if retazec[i:i+dp] == podretazec:
            c+=1
    return c

print(pocet('mama ma emu a ema ma mamu', 'ma '))
print(pocet('mama ma emu a ema ma mamu', 'am'))"""
#9
"""def prevrat(retazec):
    res = ""
    for i in range(len(retazec)-1,-1, -1):
        res+=retazec[i]
    print(res)
prevrat('tseb eht si nohtyP')"""
#10
"""def bez_medzier(text):
    res = ""
    for i in text:
        if i!=" ":
            res+=i
    return res
print(bez_medzier("   Mon tyPy   thon     "))"""
#11
"""def nahrad_samo(text, znaky):
    samo = "aeiouy"
    res = ""
    for i in text:
        if i in samo:
            res+=znaky
        else:
            res+=i
    return res

print(nahrad_samo('sedi mucha na stene', 'uo'))"""
#12 - extremne lenive riesenie
"""def do_desiatkovej(cislo):
    res = ""
    for i in range(len(str(cislo))):
        res+=str(cislo//10**i)
    return res[:len(str(cislo))]
print(do_desiatkovej(370042))"""
#13
"""def zo_sestnastkovej(retazec):
    sustava = "0123456789abcdef"
    retazec = retazec.lower()
    res = 0
    for i in range(len(retazec)):
        power = len(retazec)-1-i
        cislica = sustava.index(retazec[i])
        res+= cislica * (16**power)
    return res

print(zo_sestnastkovej('a9EF'))
print(int("a9EF", 16))"""

# vsetko sa to opakuje v inych rokoch stringov - nema zmysel to robit dookola


