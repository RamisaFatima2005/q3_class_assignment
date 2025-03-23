#built-in functions in python

# print() = print the output
print("Hello World") # Output: Hello World

# len() = returns the length of an object

text = "python"
print(len(text)) # Output: 6

#type() = return the data type of an object
num = 6
print(type(num)) # Output: <class 'int'>

# input() = takes input from the user
hobby = input("Enter your hobby: ")
print(hobby) # Output will be the input given by the user

# sum() = returns the sum of all items in an iterable
numbers = [1, 2, 3, 4, 5]
print(sum(numbers)) # Output: 15

# round() = returns the rounded value of a number
round_num = 7.453
print(round(round_num)) # Output: 7
print(round(round_num, 1)) # Output: 7.5
print(round(round_num, 2)) # Output: 7.45

#max() = returns the largest item 
max_num = [7,5,8,9,2]
print(max(max_num)) # Output: 9

#min() = returns the smallest item
min_num = [7,5,8,9,2]
print(min(min_num)) # Output: 2

# abs() = returns the positive value of a number
num = -7
print(abs(num)) # Output: 7

# sorted() = returns a sorted list
num = [7,5,8,9,2]
print(sorted(num)) # Output: [2, 5, 7, 8, 9]

# range() = returns a sequence of numbers
for i in range(5):
    print(i) # Output: 0 1 2 3 4

for num in range(6, 9):
    print(num) # Output: 6 7 8  (start from 6 and end at 9-1=8)


# User-defined functions
# A function is a block of code that only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.

def name():
    print ("My name is Ramisa")

name() # Output: My name is Ramisa

def info(hobby):
    print(hobby)

info("Reading") 

# function with parameters
def add(a, b):
    return a + b

print(add(2, 3)) # Output: 5

# function with default parameters
def greet(name="Guest"):
    print("Hello, " + name)

greet()  # Default value  Output : Hello, Guest
greet("Sara")  # Custom value  Output : Hello, Sara

# return function
def square(num):
    return num * num

result = square(4)
print(result) # Output: 16

# Lambda Function
# A lambda function is a small anonymous function. A lambda function can take any number of arguments, but can only have one expression.

x = lambda a : a + 10
print(x(5)) # Output: 15

square = lambda x : x* x
print(square(5)) # Output: 25

# Recursive Function
# A recursive function is a function that calls itself during its execution.

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5)) # Output: 120 (5*4*3*2*1)

# Function with multiple arguments
def total(*numbers):  #*args= This accept multiple numbers and it is also handle multiple arguments
    return sum (numbers)
print(total(2,4,6,8)) # Output: 20

# Function with keyword arguments
def person(name, age):
    print("Name:", name)
    print("Age:", age)
person(name="Ramisa", age=19) # Output: Name: Ramisa Age: 19

def hobby(**hobbies):  #**kwargs= accept data in dictionary format and it is also handle multiple arguments
    print("Hobby no.1: ", hobbies["hobby1"])
    print("Hobby no.2: ", hobbies["hobby2"])
hobby(hobby1 = "Coding", hobby2 = "Reading") # Output: Hobby no.1:  Coding Hobby no.2:  Reading

# Nested function
def outer():
    print("Outer function")

    def inner():
        print("Inner function")
    inner()
outer() # Output: Outer function Inner function

# Global and Local Variables

count = 5 # Global variable

def update_count(value):
    count = value # Local variable
    print("Inside function, local count:", count)

update_count(10)
print("Outside function, global count:", count) # Output: Inside function, local count: 10 Outside function, global count: 5