# While loop

# Print Numbers from 1 to 7

count = 1
while count <= 7:
     print(count)
     count +=1

# Print Even Numbers from 2 to 10

num = 2
while num <= 10:
     print(num)
     num += 2

# Ask for Password Until Correct

password = ""
while password != "1234":
     password = input("Enter your password: ")

print("Password Correct")

# Countdown from 5 to 1

number = 5

while number > 0:
     print(number)
     number -= 1

# Using break to Stop Loop Early

num = 1
while num <= 10:
     if num == 5:
          break
     print(num)
     num += 1

