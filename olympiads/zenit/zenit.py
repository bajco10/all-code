n = int(input())
x = 0
for i in range(n):
    x += int(input())

if x < 0:
    print(0)
else:
    print(x)