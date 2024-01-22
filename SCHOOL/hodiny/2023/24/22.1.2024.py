# ked nahodne ulkadam 8 figurok na sachovnicu, aka je sanca
# ze aspon 3 z tychto figurok budu na ciernych polickach?
# opakuj = 10000000
'''import random, time
priaznive, vsetky = 0, 0
start = time.time()
for i in range(10000000):
    figurky = []
    for j in range(8):
        figurky.append(random.randrange(64))
    p = 0
    for i in figurky:
        if i < 33:
            p+=1
    if p>=3:
        priaznive+=1
        vsetky +=1
    else:
        vsetky+=1
koniec = time.time()
print((priaznive/vsetky)*100)
print(f"{(koniec-start):.2f}sec")'''
"""
import multiprocessing
if __name__== "__main__":
    start = time.time()
    cpu = 4
    with multiprocessing.Pool(precesses=cpu) as pool:
        nums = [opakuj//cpu]*cpu
    # results = pool.map(pocitaj, nums)
    """

# stvorsten, ktory sa da tahat (jeho body)

