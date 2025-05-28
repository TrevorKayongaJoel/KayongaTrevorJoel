class Robot:
    pass
 

x = Robot()
y = Robot()
y2 = y
print(x == y)
print(y == y2)
x.name = "Marvin"
x.build_year = "1945"

print(x.name)
print(x.__dict__)


#We have seen that a method differs from a function only in two aspects:
#It belongs to a class, and it is defined within a class
#The first parameter in the definition of a method has to be a reference to the instance, which called the method. This parameter is usually called "self".

