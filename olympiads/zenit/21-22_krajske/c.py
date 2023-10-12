n = int(input())

stromceky = []
for i in range(n):
    stromceky+=input()

stromceky = stromceky[::-1]
abc = "abcdefghijklmnopqrstuvwxyz"
for i in stromceky[::-1]:
    if i=="o":
        stromceky[stromceky.index(i)] = abc[0]
        abc = abc[1:]

stromceky = stromceky[::-1]
for i in range(1, n+1):
    st = stromceky[:i]
    x = "".join(str(j) for j in st)
    print(x)
    stromceky=stromceky[i:]
