def kodovanie(retazec):
    l = [[" "], ["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"], ["m", "n", "o"], ["p", "q", "r"], ["s", "t", "u"], ["v", "w","x"], ["y", "z"]]
    res = ""
    retazec = retazec.lower()
    for i in retazec:
        for j in l:
            if i in j:
                x = l.index(j)
                n = j.index(i)
                print(i, x+1, n+1)
                res+=str(x)*(n+1)
    return res

print(kodovanie("janko hrasko"))
