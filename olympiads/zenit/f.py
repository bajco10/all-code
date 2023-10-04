mince, kola, pravdepodobnost = input().split()
mince, kola, pravdepodobnost = int(mince), int(kola), float(pravdepodobnost)

def stavkomat(m, k, p):
    if p <= 0.5:
        return m
    elif p > 0.5:
        return m*(2*p)**k

# geometricka postupnosť??, podobne ako pri prikladoch s uverami
# kde musime ratat s tym ze suma je ina ako povodna
# preto nemozme dat m*(2*p)*k, pretoze by sme nestavkovali
# s najvacsou moznou sumou v kazdom danom kole

print(stavkomat(mince, kola, pravdepodobnost))
