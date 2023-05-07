# smiley-face problem
"""
def count_smileys(arr):
    n = 0
    eyes = False
    nose = False
    mouth = False
    for i in arr:
        if ":" or ";" in i:
            eyes = True
        if "-" or "~" in i:
            nose = True
        if ")" or "D" in i:
            mouth = True
    if eyes and nose and mouth:
        n += 1
    elif eyes and mouth:
        n += 1
    return n

print(count_smileys([':)', ';(', ';}', ':-D']))
"""
# The hashtag generator
"""
def generate_hashtag(s):
    s = str(s)
    s = s.strip()
    s = s.title()
    s = s.replace(" ", "")
    if len(s) > 140 or len(s) <=0:
        return False
    else:
        return(f"#{s}")

print(generate_hashtag("   Hello        World"))
"""
# ROT 13 encryption code
"""
import codecs
def rot13(message):
     return codecs.decode(message, "rot_13")


print(rot13("Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf."))    
"""
# RGB - HEX converter
"""
Formátovací parameter 02x na tomto mieste znamená, že dané číslo sa 
prevedie do 16-ovej sústavy s dvoma ciframi, 
pričom sa toto číslo doplní zľava 0, ak bolo iba jednociferné. 
Vďaka tomuto zápisu vieme v našich programoch veľmi elegantne
 vygenerovať ľubovoľné RGB.
"""
"""
def rgb(r, g, b):
    if r > 255:
        r = 255
    if g > 255:
        g = 255
    if b > 255:
        b = 255
    if r < 0:
        r = 0
    if g < 0:
        g = 0
    if b < 0:
        b = 0
    return (f'{r:02x}{g:02x}{b:02x}').upper()

print(rgb(-2, 255, 300))
"""
# IP validation (not finished :( )
"""
from string import ascii_letters


def is_valid_IP1(strng):
     
    is_valid = True
    pos_list = []
    split_list = strng.split(".")
    int_list = [int(i) for i in split_list]
    # print(split_list)
    if len(split_list) != 4:
        is_valid = False
    for i in split_list:
        if "-" in i:
            is_valid = False
        for n in ascii_letters:
            if n in i:
                is_valid = False
        for n in i:
            pos_list.append(n)
    
    if pos_list[0] == "0":
        if len(pos_list) > 1:        
            is_valid = False        
          
    if len(pos_list) > 10:
        is_valid = False
    

    for j in int_list:
        if j > 255:
            is_valid = False
    return is_valid





from string import ascii_letters


def is_valid_IP(strng):
     
    is_valid = True
    pos_list = []
    split_list = strng.split(".")
    int_list = [int(i) for i in split_list]
    # print(split_list)
    if len(split_list) != 4:
        is_valid = False
    for i in split_list:
        # pos_list.append(i)
        # if "0" in i:
        #     is_valid = False
        if "-" in i:
            is_valid = False
        for n in ascii_letters:
            if n in i:
                is_valid = False
        for n in i:
            pos_list.append(n)
    
    if pos_list[0] == "0":
        if len(i) > 1:        
            is_valid = False        

    
    for j in int_list:
        if j > 255:
            is_valid = False

    return is_valid


print(is_valid_IP("123.45.67.89"))
print(is_valid_IP("123.456.789.0"))
print(is_valid_IP("0.0.0.0"))
"""
# direction reducter (not finished :/ )
"""
def dirReduc(arr):
    arr = list(arr)
    for i in range(len(arr)):
        if i > 1:
            if arr[i] == "North" and arr[i-1] == "South":
                arr.pop(i)
        if i < len(arr):
            if arr[i] == "North" and arr[i+1] == "South":
                arr.pop(i)
        
    print(arr)



dirReduc(["North", "South", "South", "South", "North"])
"""
# vowel remover
"""
def disemvowel(string_):
    # string_ = str(string_)
    remove_characters = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    # remove_characters = "aeiouAEIOU"
    for character in remove_characters:
        string_ = string_.replace(character, "")
    return string_

print(disemvowel("kokot pica u holica"))
"""
# square every digit
"""
def square_digits(num):
    stringa_cisla = str(num)
    list_cisiel = []
    hotovo = ""
    for i in stringa_cisla:
        i = int(i)
        squared = i**2
        list_cisiel.append(squared)
    for n in list_cisiel:
        n = str(n)
        hotovo += n
    
    return int(hotovo)


print(square_digits(2412))
"""
# good vs evil (did it!)
"""
def good_vs_evil1(good, evil):
    good, evil = str(good), str(evil)
    good = good.replace(" ", "")
    evil = evil.replace(" ", "")
    # print(f"good: {good}    evil: {evil}")
    good_VALUE = ( 
    (int(good[0])*1) + (int(good[1])*2) + (int(good[2])*3) + 
    (int(good[3])*3) + (int(good[4])*4) + (int(good[5])*10)
    )
    evil_VALUE = (
        (int(evil[0])*1) + (int(evil[1])*2) + (int(evil[2])*2) +
        (int(evil[3])*2) + (int(evil[4])*3) + (int(evil[5])*5) + (int(evil[6])*10)
    )
    
    print(good_VALUE)
    print(evil_VALUE)
    if good_VALUE > evil_VALUE:
        return("Battle Result: Good triumphs over Evil")
    elif good_VALUE == evil_VALUE:
        return("Battle Result: No victor on this battle field")
    else:
        return("Battle Result: Evil eradicates all trace of Good")

print(good_vs_evil1('1 1 1 1 1 1', '1 1 1 1 1 1 1'))
print(good_vs_evil1('100000', '1000000'))
"""
"""
def good_vs_evil(good, evil):
    # good, evil = str(good), str(evil)
    good = good.split(" ")
    evil = evil.split(" ")
    # print(good)
    # print(evil)
    # print(f"good: {good}    evil: {evil}")
    good_VALUE = ( 
    (int(good[0])*1) + (int(good[1])*2) + (int(good[2])*3) + 
    (int(good[3])*3) + (int(good[4])*4) + (int(good[5])*10)
    )
    evil_VALUE = (
        (int(evil[0])*1) + (int(evil[1])*2) + (int(evil[2])*2) +
        (int(evil[3])*2) + (int(evil[4])*3) + (int(evil[5])*5) + (int(evil[6])*10)
    )
    
    # print(good_VALUE)
    # print(evil_VALUE)
    if good_VALUE > evil_VALUE:
        return("Battle Result: Good triumphs over Evil")
    elif good_VALUE == evil_VALUE:
        return("Battle Result: No victor on this battle field")
    else:
        return("Battle Result: Evil eradicates all trace of Good")

print(good_vs_evil('1 1 1 1 1 1', '1 1 1 1 1 1 1'))
print(good_vs_evil('1 0 0 0 0 0', '1 0 0 0 0 0 0'))
"""
# find the odd int
"""
def find_it(seq):
    count = 0
    for n in range(-1000, 1000):
        for i in seq:
            if i == n:
                count += 1
        if count%2 > 0:
            return n

print(find_it([1, 2, 2, 2, 2, 3, 3, 3, -1, 1, 3]))
"""
"""
# better solution!
def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i
print(find_it([1, 2, 2, 2, 2, 3, 3, 3, -1, 1, 3]))
"""
"""
def find_smallest_int(arr):
    return min(arr)

     
print(find_smallest_int([78, 56, 232, 12, 11, 43])) 
"""
# multiples of 3 or 5
"""
def solution(number):
    divisibles = []
    for i in range(number):
        if not i % 3:
            divisibles.append(i)
        if not i % 5:
            if i not in divisibles:
                divisibles.append(i)
    
    return(sum(divisibles))

print(solution(553))
"""
"""
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
def increment_string(strng):
    strng = str(strng)
    cislo = ""
    for i in strng:
        print(i)
        if i in numbers:
            print("lol")
            cislo +=i
    cislo_actual = int(cislo)
    nove_cislo = cislo_actual + 1
    new_strng = strng.replace(cislo, str(nove_cislo))
    return new_strng

    

print(increment_string("kokot129"))
print(increment_string("fo99obar99"))
"""
"""
def domain_name(url):
    url = str(url)
    if "http://" in url:
        if "http://www." in url:
            url = url.replace("http://www.", "")
            url = url.split(".")
            return(url[0])
        else: 
            url = url.replace("http://", "")
            url = url.split(".")
            return(url[0])
    if "https://" in url:
        if "https://www."in url:
            url = url.replace("https://www.", "")
            url = url.split(".")
            return(url[0])
        else:
            url = url.replace("https://", "")
            url = url.split(".")
            return(url[0])
    if "www." in url:
        url = url.replace("www.", "")
        url = url.split(".")
        return(url[0])
    

domain_name("http://google.co.jp")
domain_name("https://youtube.com")
domain_name("www.xakep.ru")
domain_name("http://github.com/carbonfive/raygun")
print(domain_name("http://www.zombie-bites.com"))
print(domain_name("https://www.zombie-bites.com"))
print(domain_name("https://www.w3schools.com/tags/ref_urlencode.ASP"))
"""
"""
def likes(names):
    if len(names) == 0:
        return("no one likes this")
    elif len(names) == 1:
        return(f"{names[0]} likes this")
    elif len(names) == 2:
        return(f"{names[0]} and {names[1]} like this")
    elif len(names) == 3:
        return(f"{names[0]}, {names[1]} and {names[2]} like this")
    else:
        return(f"{names[0]}, {names[1]} and {len(names)-2} others like this")
"""

"""
def number(bus_stops):
    nastup = 0
    vystup = 0
    for i in bus_stops:
        nastup += i[0]
        vystup += i[1]
    return nastup-vystup
print(number([[10, 3], [2, 5]]))
"""

"""
def spin_words(sentence):
    new_str = ""
    lst = []
    for i in sentence:
        print(i)
        if len(i) >= 5:
            lst.append(i)
            for j in i:
                # lst.append(j)
                pass
        else:
            new_str += i
    return lst
"""
#word spinner
"""
def spin_words(sentence):
    L = sentence.split()
    new = []
    for word in L:
        if len(word) >= 5:
            new.append(word[::-1])
        else:
            new.append(word)
    string = " ".join(new)
    return string

print(spin_words("Hey fellow warriors"))

lst = [1, 2, 3, 4, 5]
print(lst[::-1])
print(lst[::-1])
"""
"""
def is_valid_walk(walk):
    boky = 0
    vrchy = 0
    if len(walk) != 10:
        return False
    for i in walk:
        if i == "n":
            vrchy += 1
        elif i == "s":
            vrchy -= 1
        if i == "e":
            boky += 1
        elif i == "w":
            boky -=1
    if boky != 0:
        return False
    if vrchy != 0:
        return False
    return True
"""
def xo(s):
    if s.count("x") in s == s.count("o") in s:
        return True
    else:
        return False