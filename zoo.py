zoo = ("monkey", "tiger", "bear", "lion", "seal", "zebra", "hedgehog", "king cobra", "spider", "dolphin")

zoo.index("dolphin")

animal_to_find = "kangaroo"
if animal_to_find in zoo:
    print(f"A {animal_to_find} is in your zoo")
else:
    print(f"A {animal_to_find} is not in your zoo")

(first_animal, second_animal, third_animal, fourth_animal, fifth_animal, sixth_animal, seventh_animal, eighth_animal, ninth_animal, tenth_animal) = zoo
print(first_animal) 
print(second_animal) 
print(third_animal) 
print(fourth_animal) 
print(fifth_animal) 
print(sixth_animal) 
print(seventh_animal) 
print(eighth_animal) 
print(ninth_animal) 
print(tenth_animal) 

zoo = list(zoo)
zoo.extend(["panda", "fox", "kangaroo"])
zoo = tuple(zoo)