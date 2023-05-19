def zisti(retazec):
    abc = "abcdefghijklmnopqrstuvwxyz"
    hodnoty = []
    retazec = retazec.lower()
    retazec = retazec.replace(",", "")
    slova = retazec.split(" ")
    hodnota = 0

    for i in slova:
        for j in range(len(i)-1):
            """The reason for subtracting 1 is because
            the loop variable j is incremented within the loop. 
            By subtracting 1, we ensure that the correct number 
            of characters (excluding the first character) is 
            considered in the calculation."""
            hodnota += abs((abc.find(i[j])+1) - (abc.find(i[j+1])+1)) - 1
        hodnoty.append(hodnota)
        hodnota = 0
    min_index = hodnoty.index(min(hodnoty))
    return f"{slova[min_index]} - {min(hodnoty)}"

x = zisti("Adolf, Gregor, Filip, Natalia")
y = zisti("jednotka, Prepadnem, string, GBAS, abeceda")

print(x)
print(y)

