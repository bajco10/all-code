#1
# vstup: *lek-kal+lotoK
# vystup: Kotol lak kel

def premen(retazec):
    retazec = retazec.replace("*", " ")
    retazec = retazec.replace("-", " ")
    retazec = retazec.replace("+", " ")
    retazec = retazec.strip()
    return retazec[::-1]
print(premen("*lek-kal+lotoK"))

#2

def card_check(card_number):
    card_number = card_number.replace("-", "")
    if not card_number.isdigit() or len(card_number)!=16:
        return False
    digits = card_number[::-1] # otocil som si to uz tu
    total = 0
    for i in range(len(digits)):
        digit = int(digits[i])
        if i % 2 == 1:
            digit = digit * 2
            if digit > 9:
                digit = digit - 9
        total += digit
    return total % 10 == 0

print(card_check("1234-5467-3216-2324"))

#2.5 looks for an x value that makes the card_n valid
# strasne leniva cesta ale funguje to lmao
def card_creator(card_number):
    card_number = card_number.replace("-", "")
    if len(card_number)!=16:
        return False
    for i in range(10):
        total = 0
        new_number = card_number.replace("x", f"{i}")
        digits = new_number[::-1]
        for i in range(len(digits)):
            digit = int(digits[i])
            if i % 2 == 1:
                digit = digit * 2
            if digit > 9:
                digit = digit - 9
            total += digit
            if total%10==0:
                print(new_number)
                return True
    return False
print(card_creator("1234-5467-3216-x324"))

    