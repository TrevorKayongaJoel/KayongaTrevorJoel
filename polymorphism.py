# polymorphism
class Bird:
    def fly(self):
        print("Birds fly in the sky")
        
class Eagle(Bird):
     def fly(self):
        print("Eagles fly at higher altitude")
        
class Sparrow(Bird):
    def fly(self):
        print("Sparrows fly at low altitude")
        
def flight_test(bird):
    bird.fly()
    
eagle1 = Eagle()
sparrow1 = Sparrow()

flight_test(eagle1)
flight_test(sparrow1)