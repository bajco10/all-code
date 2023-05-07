n = int(input())
y = 0
for i in range(n):
    x = input()
    y = y + x.count("<") + x.count(">")
if y%2:
    print("had")
else:
    print("dazdovka")
