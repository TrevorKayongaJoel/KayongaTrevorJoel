add = lambda a, b: a + b

print(add(10, 5))

 
 # lambda fun to get square of list map [1,2,3,4,5]
 

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x * x, numbers)) 
print(squared)
