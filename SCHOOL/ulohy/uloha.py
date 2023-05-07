# akvarium
# hustota skla = 2500kg / m**3
# hustota vody = 998 kg**m3
dlzka = 1
sirka = 0.45
vyska = 0.6

objem_vody = (dlzka-0.02) * (sirka-0.02) * (vyska-0.01)
objem = dlzka * sirka * vyska
blok_skla_vaha = 2500 * (dlzka * sirka * vyska)
vyrez_zo_skla_vaha = 2500 * ((dlzka-0.02) * (sirka-0.02) * (vyska-0.01))
akvarium_vaha = (blok_skla_vaha - vyrez_zo_skla_vaha) + (998 * ((dlzka-0.02) * (sirka-0.02) * (vyska-0.01)))
print(f"Vaha plne naplneneho akvaria je {akvarium_vaha}kg.")