# error 
# 1. Syntax errors
# 2. Runtime errors 
# 3. Logical errors
try:
    result = 5 / 0
    
except ZeroDivisionError:
    print("Cannot divide by zero.")
    
else:
    print("Division successful", result)
    
finally:
    print("run complete")
    
# custom exception

def set_age(x):
   if x < 0:
       raise ValueError("Age cannot be negative")
   else:
       print(f"You are {x} years old")

try:
    set_age(5)
    
except ValueError as e:
    print(e)
    