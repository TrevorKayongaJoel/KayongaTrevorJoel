# Turples
x = ("samsung", "iphone", "tecno", "redmi")
print("My favorite phone brands:", x[1])

# using negative indexing to print the second item
print("This my turple:", x)
print("2nd item:", x[-3])

# updating iphone to itel in the turple
x_list = list(x)
x_list[1] = "itel"
x = tuple(x_list)
print("My new Turple:", x)

# Adding "Huawei" to the turple
x += ("Huawei",)
print("Updated Turple:", x)

# Looping through the Turple
for i in x:
    print(i)

# Removing/deleting first item in the turple
x = x[1:]
print(x)

# using turple constructor "turple()"
cities = tuple(["K'la", "Mbara","Gulu", "Masaka"])
print("Cities:",cities)

# unpacking the turple
a, b, c, d = cities
print("Cities:", a, b, c, d)

# printing items from the turple in the range 2:4
print("2nd, 3rd, and 4th Cities", cities[1:4])

# joining turples
firstNames = ("Rita", "Ruth")
lastNames = ("Lumala", "Luyimbazi")
fullName = firstNames + lastNames
print("Names:", fullName)

# Multiplying a turple by 3
colors = ("Blue", "Green", "Red")
multiple = colors * 3
print("Colors:", colors)
print("Multiplied Colors:", multiple)

# Count in the turple
thisturple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count_8 = thisturple.count(8)
print("Turple:", thisturple)
print(f"8 appears {count_8} times")