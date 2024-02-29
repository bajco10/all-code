# 7x6 hracia plocha (7 sirka, 6 vyska)
# postupne striadnie hráča 1 a 2
# hrac vyhrava ak ma suvisle 4 gulicky svojej farby: 1. verikalne 2. horizontalne 3. diagonalne
# spravit 2_rozmerné pole, keď hráč klikne na stlpec, zistiť ktory "najnizsi" riadok je prazdny
# na tom indexe a tam dat jeho kruh

import tkinter
c = tkinter.Canvas(width=600, height=550, bg="light grey")
c.pack()

# hracia plocha
c.create_rectangle(50, 80, 550, 510, fill="black", outline="")
# diery v ploche
kruh_x, kruh_y = 60 + 30, 90 + 30
for i in range(6):
    for i in range(7):
        c.create_oval(kruh_x - 30, kruh_y - 30, kruh_x + 30, kruh_y + 30, fill="white", outline="")
        kruh_x += 70
    print("max_x", kruh_x)
    kruh_x = 90
    kruh_y += 70
print("max_y", kruh_y)

c.mainloop()