# Base dictionary
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

# 1. Print the value of the shoe size
print("Shoe size:", Shoes["size"])

# 2. Change the value “Nick” to “Adidas”
Shoes["brand"] = "Adidas"
print("Updated brand:", Shoes["brand"])

# 3. Add a key/value pair "type”: "sneakers"
Shoes["type"] = "sneakers"
print("Dictionary after adding type:", Shoes)

# 4. Return a list of all the keys
print("Keys:", list(Shoes.keys()))

# 5. Return a list of all the values
print("Values:", list(Shoes.values()))

# 6. Check if the key “size” exists
print("Does 'size' exist in Shoes?", "size" in Shoes)

# 7. Loop through the dictionary
print("Dictionary contents:")
for key, value in Shoes.items():
    print(f"{key}: {value}")

# 8. Remove “color” from the dictionary
Shoes.pop("color", None)
print("After removing color:", Shoes)

# 9. Empty the dictionary
Shoes.clear()
print("Emptied dictionary:", Shoes)

# 10. Write a dictionary and make a copy
person = {
    "name": "Trevor",
    "age": 22,
    "country": "Uganda"
}
person_copy = person.copy()
print("Copied dictionary:", person_copy)

# 11. Show nested dictionaries
family = {
    "child1": {
        "name": "Liana",
        "age": 10
    },
    "child2": {
        "name": "Abraham",
        "age": 8
    }
}
print("Nested dictionary:")
print(family)
