m = int(input())

p1 = list(map(int, input().split(" ")))
p2 = list(map(int, input().split(" ")))

p2.sort()
p1.sort()


def kukni(m, p1, p2):
    t = True
    for i in range(m):
        if p1[i]!=p2[i]:
            if (p1[i]+1)!=p2[i]:
                t = False

    if t:
        print("Jednoduche")
    else:
        print("Neda sa")
    

kukni(m, p1, p2)
        

