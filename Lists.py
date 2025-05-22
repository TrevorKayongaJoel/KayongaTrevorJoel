names = ["Abel", "Cain", "Adam", "Eve", "Noah"]
print("Initial list:", names)
print("2nd Name: " + names[1])

# Changing value of the first item
names[0] = "John"
print("1st name: " + names[0])

# adding 6th name to the list
names.append("Mary")
print("6th name: " + names[5])

# add a name as the third element
names.insert(2, "Bathel")
print("3rd name: " + names[2])

# removing 4th element from list
names.pop(3)
print("After removing forth element", names)

# using negative indexing to print the last name in the list
print("Last name: " + names[-1])

# creating new list having 7 elements
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
print(colors[2:5])

# Making a copy of a list
countries = ["Uganda", "Kenya", "SouthAfrica", "China"]
copy = countries.copy()
print("Copy of Countries: ", copy)

# looping through the list of countries
k = 1
for i in countries:   
    print(f"Country {k} is {i}")
    k += 1
    
# sorting a list of animals in Descending order
animals = ["Pigs", "Cows", "Goats", "Sheep", "Chickens"]
animals.sort()
print("Animals in Ascending order: ", animals)
animals.sort(reverse=True)
print("Animals in Descending order: ", animals)

# outputting only animals with letter 'a' in them
animals_A = [animals for animals in animals if "a" in animals]
print("Animals with letter 'a' in them: ", animals_A)

# joining 2 lists
firstNames = ["John", "Mary"]
lastNames = ["Mukibi", "Lule"]
fullNames = firstNames + lastNames
print("Full names: ", fullNames)