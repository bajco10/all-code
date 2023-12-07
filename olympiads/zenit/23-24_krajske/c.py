n = int(input())
montes = list(map(int, input().split()))
distinctus_elementa = set(montes)
maximus_numerus = 0
for iterum in distinctus_elementa:
    for alter_iterum in distinctus_elementa:
        if iterum == alter_iterum:
            continue
        numerus = 0
        dp = [0] * len(montes)
        for index, valor in enumerate(montes):
            if valor == iterum or valor == alter_iterum:
                numerus += 1
            else:
                numerus = 0
            dp[index] = numerus
        maximus_numerus = max(maximus_numerus, max(dp))
print(maximus_numerus)
