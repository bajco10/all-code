import random
with open("/home/tomas/Desktop/all-code/SCHOOL/testy/prvocisla.txt", "w") as subor:
    prvo = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 
            47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for i in range(5): # 5 riadkov v subore
        v_riadku = random.randrange(3, 8)
        cisla = []
        for j in range(v_riadku):
            cisla.append(str(random.choice(prvo)))
        print(" ".join(cisla))
        print(" ".join(cisla), file = subor)
