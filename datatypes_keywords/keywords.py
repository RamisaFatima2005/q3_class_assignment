# if, elif, else
age = 18
if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You just became an adult!")
else:
    print("You are an adult.")  # Output: You just became an adult!

# for loop
for i in range(3):
    print("Hello")  #Output: prints Hello 3 times

# while loop
x = 0
while x < 3:
    print(x)
    x += 1  #Output: 0,1,2

# break (stops loop)
for i in range(5):
    if i == 3:
        break
    print(i)    #Output: 0,1,2

# continue (skips an iteration)
for i in range(5):
    if i == 3:
        continue
    print(i)    #Output: 0,1,2,4

# pass (does nothing, used as a placeholder)
def my_function():
    pass

# def and return
def add(a, b):
    return a + b
print(add(3, 5)) #Output: 8

# lambda (one-line function)
square = lambda x: x * x
print(square(4)) #Otput: 16

# class (blueprint for objects)
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}") #Output: Hello, my name is Ali

p1 = Person("Ali")
p1.greet()

# try, except, finally
try:
    num = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("This always runs.") #Output: Cannot divide by zero. This always runs.

# raise (custom error)
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")

try:
    check_age(-1)
except ValueError as e:
    print("Error:", e)  # Output: Error: Age cannot be negative!


# assert (stops if condition is False)
x = 10
assert x > 5, "x should be greater than 5"  #Output:No output (The program runs normally because the condition x > 5 is True).

# import a full module
import math
print(math.sqrt(16)) #Output: 4.0

# from (import only specific parts)
from math import pi
print(pi) #Output: 3.141592653589793

# as (rename a module)
import numpy as np
print(np.array([1, 2, 3])) #Output: [1 2 3]

# Boolean values
is_student = True
print(is_student) #Output: True

# None (empty value)
x = None
print(x)    #Output:None

# del (delete a variable)
name = "John"
del name  # Now, name no longer exists

# global (modify global variable)
x = 5
def change():
    global x
    x = 10
change()
print(x) #Output: 10

# nonlocal (modify outer function variable)
def outer():
    y = 10
    def inner():
        nonlocal y
        y = 20
    inner()
    print(y) #Output: 20
outer()

# and, or, not
a= True
b =False
print(a and b)  # False
print(a or b)   # True
print(not a)    # False

# in, not in
fruits = ["apple", "banana"]
print("apple" in fruits)  # True
print("mango" not in fruits)  # True

# is, is not
x = [1, 2, 3]
y = x
print(x is y)  # True (same object)
print(x is not y)  # False (they are the same)

import asyncio

# async and await (asynchronous function)
async def hello():
    print("Hello")          #Output: Hello
    await asyncio.sleep(1) # Pause for 1 second (asynchronously)
    print("World")          #World appears after 1 second

asyncio.run(hello())


