# abstraction
from abc import ABC, abstractmethod #Abstraction

# define abstract class

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass # This method has no implementation
    

class Car(Vehicle):
    def start(self):
        print("Car engine starts")
        
class Bike(Vehicle):
    def start(self):
        print("Bike engine starts")
        
car1 = Car()
bike1 = Bike()

car1.start()
bike1.start()