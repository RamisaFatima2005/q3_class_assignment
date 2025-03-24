# Example no. 1

# try = The try block is used to test a block of code for errors.

try:
    num1 = int(input("Enter firts number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2

# except = The except block is used to handle the error.

except ZeroDivisionError:
    print("Can't divide by zero")
except ValueError:
    print("Please enter a valid number")

# else = The else block will execute if the try block does not raise an exception.

else:
    print(result)

# finally = The finally block is used to execute code, regardless of the result of the try- and except blocks.
finally:
    print("This will always execute")


# Example no. 2
# raise = The raise keyword is used to raise an exception.
age = int(input("Enter your age: "))

if age < 18:
    raise ValueError("You must be 18 or older to enter") 
else:
    print("You are allowed.")