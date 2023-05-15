import random
def allUnique(x):
    seen = set()
    return not any(i in seen or seen.add(i) for i in x)

n = int(input())
jedla = input().split(" ")
jedla = [int(k) for k in jedla]
# print(n, len(jedla))
if n == 1:
    print("Janka bude frflat")
elif allUnique(jedla) == False:
    print("Janka bude frflat")
else:
    # random.shuffle(jedla)
    jedla = jedla[::-1]
    for i in jedla:
        print(i, end=" ")



    




    

    