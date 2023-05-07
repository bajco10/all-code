def porovnaj(s1, s2):
    if s1< s2:
        return (f"{s1} < {s2}")
    if s1 > s2:
        return f"{s1} > {s2}"
    return f"{s1} == {s2}"

print(porovnaj("2", "11"))
print(porovnaj("32", "9"))

def sucet(slovo):
    for i in range(len(slovo)):
        if slovo[i] == " ":
            return int(slovo[:i]) + int(slovo[i:])

print(sucet("12 9"))