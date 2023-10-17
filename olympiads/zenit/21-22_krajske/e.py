"""n = int(input())

karticky = []
karty = input()

karticky = karty.split(" ")
karticky = [int(x) for x in karticky]

h1, h2 = 0, 0

while karticky:
    if karticky[0] >= karticky[-1]:
        h1 += karticky[0]
        karticky.pop(0)
    elif karticky[0] < karticky[-1]:
        h1 += karticky[-1]
        karticky.pop(-1)
    if karticky:
        if karticky[0] >= karticky[-1]:
            h2 += karticky[0]
            karticky.pop(0)
        elif karticky[0] < karticky[-1]:
            h += karticky[-1]
            karticky.pop(-1)

# toto by fungovalo keby nemusia chodit zlava/zprava
while karticky:
    h1 += max(karticky)
    karticky.pop(karticky.index(max(karticky)))
    if karticky:
        h2 += max(karticky)
        karticky.pop(karticky.index(max(karticky)))

print(h1, h2)
"""

def optimalne_body(N, karticky):
    dp = [[0] * N for _ in range(N)]
    
    for i in range(N):
        dp[i][i] = karticky[i]
    
    for length in range(2, N + 1):
        for i in range(N - length + 1):
            j = i + length - 1
            dp[i][j] = max(karticky[i] - dp[i + 1][j], karticky[j] - dp[i][j - 1])
    
    return dp[0][N - 1]

# Načítanie vstupu
N = int(input())
karticky = list(map(int, input().split()))

# Výpočet optimálnych bodov
body = optimalne_body(N, karticky)

# Rozdelenie bodov pre hráča 1 a hráča 2
body_hrac1 = (sum(karticky) + body) // 2
body_hrac2 = (sum(karticky) - body) // 2

# Výstup
print(body_hrac1, body_hrac2)

