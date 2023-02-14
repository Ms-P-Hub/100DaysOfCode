"""BANDNAME GENERATOR PROGRAM"""

print("Welcome to the Band Name Generator.")
city = input("What is the name of the city you were born in?\n")
while city.isalpha() == False:
    print("Error please enter a string")
    city = input("What is the name of the city you were born in?\n")

pet_name = input("What is your pet's name?\n")
while pet_name.isalpha() == False:
    print("Error please enter a string")
    pet_name = input("What is your pet's name?\n")
    
print(f"Your Band name could be {city.capitalize()}-{pet_name.capitalize()}")