# using a set constructor to creat a set
Beverages = set(["Sting", "Red Bull", "Juice"])
print("Beveragess Set:", Beverages)

# adding elements to the set
Beverages.add("Bushera")
Beverages.add("Ug")
print("Beverages Set:", Beverages)

# checking if an element is present in the set
mySet = {"oven", "kettle", "microwave", "refrigerator"}
if "microwave" in mySet:
    print("Microwave is present in the set")
else:
    print("Microwave is not present in the set")
    
# removing elements from the set
mySet.remove("kettle")
print("Set after removing kettle:", mySet)

# looping through a set
for i in mySet:
    print(i)

# joining sets
fantasticFour = {"Reed Richards", "Sue Storm", "Johnny Storm", "Ben Grimm"}
avengers = {"Iron Man", "Hulk"}
marvel = fantasticFour.union(avengers)
print("Marvel Set:", marvel)

age = {12, 17, 23, 40}
firstNames = {"Nielsen", "Nate","Trevor", "Nanah"}
combination = age.union(firstNames)
print("Combination Set:", combination)