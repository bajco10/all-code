x = input().split(" ")
y = input().split(" ")
y = [int(k) for k in y]
x = [int(k) for k in x]
y.sort(reverse=True)
A=int(x[0])
B=int(x[1])
fin=[0, 0, 0]
for l, i in enumerate(y):
    if A<B:
        if int(i)<=A:
            A -= int(i)
            fin[l] = 1
        elif int(i)<=B:
            B -= int(i)
            fin[l] = 1
    else:
        if int(i)<=B:
            B-=int(i)
            fin[l]=1
        elif int(i)<=A:
            A-=int(i)
            fin[l]=1
if fin.count(0) == 0:
    print("Ano")
else:
    print("Nie")