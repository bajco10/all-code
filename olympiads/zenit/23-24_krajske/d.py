n = int(input())
cisla = list(map(int, input().split(" ")))
sucin = 1
for i in range(n):
    sucin = (sucin * cisla[i]) % (10**9 + 7)
vysledok = [str(pow(cisla[i], -1, 10**9 + 7) * sucin % (10**9 + 7)) for i in range(n)]
print(" ".join(vysledok))


