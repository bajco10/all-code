'''
bicycles = ["trek", "canondale", "redline", "specialized"]
print(bicycles[-1].title())
print(bicycles[2].title())

message = f"my first bicycle was a {bicycles[0].title()}"
print(message)
'''
'''
# 3.1 exercise
names = ["medo", "samo", "pato", "andrej", "stano"]
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[3].title())
print(names[4].title())
# 3.2 exercise
# using the list names
print("Greetings "+names[0].title()+", how are you?")
print("Greetings "+names[1].title()+", how are you?")
print("Greetings "+names[2].title()+", how are you?")
print("Greetings "+names[3].title()+", how are you?")
print("Greetings "+names[4].title()+", how are you?")
# 3.3 exercise
mode_of_transportation = ["car", "motorcycle"]
brand_of_transportation = ["Honda", "Yamaha", "Toyota"]
print("I would like to own a "+brand_of_transportation[0].title()+" "+mode_of_transportation[0]+".")
'''
'''
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
motorcycles.insert(0, "ducati")
print(motorcycles)
del motorcycles[-1]
print(motorcycles)
'''
'''
motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)
too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
'''
'''
# 3.4 - 3.6 exercise
people_for_dinner = ["einstein", "schopenhauer", "plato", "nietzsche"]
for person in people_for_dinner:
    print(person+" come to dinner")
print(people_for_dinner[-1])
people_for_dinner[-1] = "fico"
print(people_for_dinner)
for person in people_for_dinner:
    print(person+" come to the fucking dinner")
print("We found a new bigger table!")
people_for_dinner.insert(0, "kalinak")
people_for_dinner.insert(-1, "tiso")
people_for_dinner.insert(3, "raz")
print(people_for_dinner)
for person in people_for_dinner:
    print(person + " like come to the fucking dinner already!")
print("We can only invite 2 people for dinner!")
while len(people_for_dinner) > 2:
    person_leaving = people_for_dinner.pop()
    print(person_leaving+" sorry, you can't go.")
    
print(people_for_dinner)
del people_for_dinner[1]
del people_for_dinner[0]
print(people_for_dinner)
'''
'''
cars = ["bmw", "audi", "toyota", "subaru"]
# cars.sort(reverse=True)
# print(cars)
# print("Here is the original list: "+str(cars))
# print("\nHere is the sorted list: "+str(sorted(cars, reverse=True)))
# print("\nHere is the original list again: "+str(cars))
# cars.reverse()
# print(cars)
print(len(cars))
'''
'''
# 3.8 exercise
locations = ["moscow", "california", "tokyo", "amsterdam", "london"]
print(locations)
print(sorted(locations))
print(locations)
print(sorted(locations, reverse=True))
print(locations)
locations.reverse()
print(locations)
locations.sort()
print(locations)
locations.sort(reverse=True)
print(locations)
'''
