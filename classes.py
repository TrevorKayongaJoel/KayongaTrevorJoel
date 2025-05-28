class Student:
    def __init__(self, name = None, regno = None):
        self.name = name
        self.regno = regno
        
        
    def say_Hi(self):
        if self.name and self.regno:
            print(f"My name is {self.name} and my Registion Number is {self.regno}")
        else:
            print("I am a student with no Name and Registration Number")
            
x = Student("Trevor", "001")
x.say_Hi()

y = Student()
y.say_Hi()
