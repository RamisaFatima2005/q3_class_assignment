#if statement

age = float(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote")

# else statement

age = float(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

#elif statement

age = float(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote")
elif age == 17:
    print("You will be eligible to vote next year")
else:
    print("You are not eligible to vote")

#nested if else statement

username = str(input("Enter your username(admin): "))
password = str(input("Enter your password(1234): "))

if username == "admin":
    if password == "1234":
        print("Login Successfully")
    else:
        print("Invalid Password")
else:
 print("User not found")