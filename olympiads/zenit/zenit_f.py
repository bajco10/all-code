pole = [[1, 1], [3, 2], [2, 3], [4, 9], [5, 6], [7, 8], [6, 7], [8, 5], [9, 4]]
uspor = sorted(pole)

n = len(pole)
moznosti = []
def generuj(i):
    for j, prvok in enumerate(uspor[i:]):
        pole[i] = prvok
        prve = [x[0] for x in pole]
        druhe = [x[1] for x in pole]
        if prve == sorted(prve) and druhe == sorted(druhe):
            print(*pole)
            # moznosti.append([*pole])
            
        else:
            generuj(i+1)

generuj(0)