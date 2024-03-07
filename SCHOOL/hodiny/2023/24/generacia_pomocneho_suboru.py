import random
with open("spokojnost.txt", "w") as subor:
    for i in range(20000):
        cas = f"{random.randrange(0, 24)}:{random.randrange(0,60):02}"
        spokojny = random.choice(("ano", "nie"))
        print(f"{cas} {spokojny}", file=subor)
