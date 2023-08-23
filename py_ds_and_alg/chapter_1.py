#R-1.1
"""def is_multiple(n, m):
    return n%m==0
print(is_multiple(6, 4))"""
#R-1.2
"""def is_even(k):
    return (k[-1] in "02468")
print(is_even("1233131"))"""
#R-1.3
# - without the use of in-built functions
"""def minmax(data):
    minim = 0
    maxim = 0
    for i in data:
        if i > maxim:
            maxim = i
        if i < minim:
            minim = i
    return minim, maxim
print(minmax([9,3,2,2,34,-4,2]))"""
#R-1.4
"""def square_sum(n):
    sum = 0
    for i in range(1, n+1):
        sum+=i*i
    return sum
print(square_sum(3))"""
#R-1.5
"""print(sum(i*i for i in range(4)))"""
#R-1.6
"""def odd_square_sum(n):
    sum=0
    for i in range(1, n+1):
        if i%2!=0:
            sum+=i*i
    return sum"""
#R-1.7
"""print(sum(i*i for i in range(10) if i%2!=0))"""
#R-1.8
"""s[j], j=n-abs(k)
    n being the length of the string"""
#R-1.9
"""range(50, 80, 10)"""
"""for i in range(50,90, 10):
    print(i)"""
#R-1.10
"""for i in range(8, -10, -2):
    print(i)"""
#R-1.11
"""newlist = [2**x for x in range(9)]
print(newlist)"""
#R-1.12
"""import random
n being the length of the non-empty sequence
def random_choice(n):
    i = random.randrange(0, n+1)
    return n[i]"""

#C-1.13
"""we take the list into our function and create 
a copy using list[::-1] which reverses our list"""
"""k = [1,2,3]
l = k[::-1]"""
#C-1.14 - probably suboptimal
"""def odd_product(numbers):
    nums = []
    for i in numbers:
        for j in numbers:
            if i!=j and (i*j)%2!=0 and (i, j) not in nums:
                t = (i, j)
                nums.append(t)
    return nums
print(odd_product([1,1,1,2,34,4,4,8,9,90,322]))"""
#C-1.15
"""def are_unique(numbers):
    for i in numbers:
        if numbers.count(i)!=1:
            return False
    return True
print(are_unique([1,24,5,6]))"""
#C-1.16
"""because it changes it inside of the function body??"""
#C-1.17
"""does not work because of no return statement and no
    variable to return the data as"""
"""def scale(data, factor):
    for val in data:
        val *= factor"""
#C-1.18
"""l = [x*(x + 1) for x in range(10)]
print(l)"""
#C-1.19
"""l = [chr(i) for i in range(97, 123)]
print(l)"""
#C-1.20 - funny "solution"
"""import random
def wish_shuffle(data):
    n = len(data)
    l = [0]*n
    used = []
    for i in data:
        idx = random.randrange(0,n)
        while idx in used:
            idx=random.randrange(0,n)
        used.append(idx)
        l[idx] = i
    return l
print(wish_shuffle([1,2,3, 4, 5, 6, 7, 8, 9]))"""
#C-1.21
"""def main():
    lines = []
    try:
        while True:
            line = input()
            lines.append(line)
    except EOFError:
        pass
    print("\n".join(reversed(lines)))
main()"""
#C-1.22
"""def dot_product(a, b):
    n = len(a)
    c = []
    for i in range(n):
        c.append(a[i]*b[i])
    return c
print(dot_product([2,2,2,4], [1,2,1,3]))"""
#C-1.23
"""def overflow(idx):
    cars=["audi", "bmw", "toyota", "nissan", "mitsubishi"]
    try:
        return cars[idx]
    except IndexError:
        return "Don't try buffer overflow attacks in Python!"
print(overflow(12))"""
#C-1.24
"""def vowel_count(s):
    c = 0
    for i in s:
        if i in "aeiouy":
            c+=1
    return c
print(vowel_count("mama"))"""
#C-1.25 - garbage solution -> should have done with ord() values
"""def de_punctuator(s):
    res = ""
    for i in s:
        if i in " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
            res+=i
    return res
print(de_punctuator("Let's try, Mike."))"""
#C-1.26 - faster to type out 
"""def formulator(a, b, c):
    if a+b==c or a+c==b or b+c==a:
        return True
    elif a-b==c or a-c==b or b-c==a:
        return True
    elif a*b==c or b*c==a or a*c==b:
        return True
    return False
print(formulator(2,2,4))
print(formulator(11, 3, 7))"""
#C-1.27
"""def factors(n):
    k = 1
    while k*k<n:
        if n%k==0:
            yield k
            yield n//k
        k += 1
    if k*k==n:
        yield k
x = list(factors(8))
x.sort()
print(x)"""
#C-1.28
"""import math
def norm(v, p):
    vv = 0
    for i in v:
        vv += i**p
    vv = vv**(1/p) #math.sqrt(vv) 
    return vv
print(norm([1, 2, 2], 2))"""
#P-1.29
"""def permutator(chars, current="", results=[]):
    if len(current) == len(chars):
        results.append(current)
        return
    
    for char in chars:
        if char not in current:
            permutator(chars, current + char, results)
def main():
    characters = "catdog"
    permutations = []
    permutator(characters, results=permutations)
    return permutations
print(main())"""
#P-1.30
"""def divider(n):
    c = 0
    while n/2 >= 2:
        c+=1
        n/=2
    return c
print(divider(2224728947289472))"""
#P-1.31 - made in €
"""def change(charged, given):
    change = given - charged
    print(change)
    bills_and_coins=[]
    returned = {}
    while change !=0:
        for i in 500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01:
            if change-i >= 0:
                bills_and_coins.append(i)
                change-=i
                change = round(change, 2)
                break
    for k in bills_and_coins:
        j = bills_and_coins.count(k)
        returned[k]=j
    return returned
print(change(54.70, 100))
print(change(122234.23, 2200000.50))"""
#P-1.32 + P-1.33 - don't want to waste too much time on this
"""def simple_calculator():
    while True:
        n = int(input())
        operand = input()
        m = int(input())
        if operand == "+":
            print(m+n)
        elif operand == "-":
            print(n-m)
        elif operand == "*":
            print(n*m)
        elif operand == "/":
            print(n/m)
simple_calculator()"""
#P-1.34 - understood as making the mistakes in each one
"""import random
def printer():
    s = "I will never spam my friends again."
    for i in range(101):
        s = "I will never spam my friends again."
        for j in range(9):
            idx = random.randrange(0, len(s)+1)
            ch = chr(random.randrange(97, 123))
            s = s[:idx] + ch + s[idx+1:]
        print(f"{i}.{s}")
printer()"""
#P-1.35 #dd-mm-yyyy - not 100% accurate with month days
"""import random
def birthday_generator(n):
    b_day = ""
    b_days = []
    for i in range(n+1):
        b_day=f"{random.randrange(0, 32):02}-{random.randrange(0, 13):02}-{random.randrange(1950,2024)}"
        b_days.append(b_day)
    return b_days
def bd_check(bds):
    common_bds = []
    for i in bds:
        if bds.count(i)>1:
            common_bds.append(i)
    return common_bds
# print(birthday_generator(23))
print(bd_check(birthday_generator(230)))"""
#P-1.36
"""def word_counter(s):
    l = s.split(" ")
    res = {}
    for i in l:
        j = l.count(i)
        res[i] = j
    return res
print(word_counter("mama dog dog dog cat cat split split cat dog dad try go on on for long on"))"""





        










