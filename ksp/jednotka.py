n = int(input())
l = []
for i in range(n):
    l.append(int(input()))

l.sort()
#l.remove(max(l))
rebrik = l[-2]
kolko = rebrik - 2 + 1
pocet_policok = len(l)-2
if len(l)<3:
    print(0)
elif kolko<pocet_policok:
    print(kolko)
else:
    print(pocet_policok)
# print(x)

