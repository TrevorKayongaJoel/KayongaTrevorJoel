# Eg 1: Inheritance
# Superclass / Parent Class / Base class
class Animal:
    def speak(self):
        print("Animal makes sound")
        

# subclass / child class / derived class
class Cat(Animal):
    def sound(self):
        print("Cat makes sound meow")
        
        
# Create an object of cat
cat1 = Cat()

cat1.speak()
cat1.sound()

class A:
    def method(self):
        print("Method from A")
        
class B(A):
    def method(self):
        print("Method from B")
        
class C(A):
    def method(self):
        print("Method from C")
        
class D(B, C):
    pass

d = D()
d.method()