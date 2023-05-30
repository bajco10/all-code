# overkill riesenie
def kodovanie(retazec):
    l = [[" "], ["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"], ["m", "n", "o"], ["p", "q", "r"], ["s", "t", "u"], ["v", "w","x"], ["y", "z"]]
    res = ""
    retazec = retazec.lower()
    for i in retazec:
        for j in l:
            if i in j:
                x = l.index(j)
                n = j.index(i)
                res+=str(x)*(n+1)
    return res

print(kodovanie("janko hrasko"))

# riesenie cez ordinalne hodnoty

def kodovanie(textik):
    textik = textik.upper()
    v = ""
    for i in textik:
        if i == " ":
            v+= "0"
            continue
        poc = (ord(i)-65)%3 +1
        cislo = str(((ord(i)-65)//3)+1)
        v += poc*cislo
    print(v)

kodovanie("Janko Hrasko")
