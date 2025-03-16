#For loop

#Print Numbers from 1 to 5

for i in range(1,6):
     print(i)

#Print Each Letter in a Word

word = "Python"
for letter in word:
     print(letter)

#Loop Through a List

stationary = ["Pen", "Pencil", "Eraser", "Ruler"]
for item in stationary:
     print(item)

# Print Even Numbers from 2 to 10

numbers =[1,2,3,4,5,6,7,8,9,10]
for even in numbers:
     if even % 2 == 0:
          print(even)

#Using for Loop with break

for num in range(1, 6):
     if num == 4:
          break
     print(num)

#Using for Loop with continue

for count in range(1,6):
     if count == 3:
          continue
     print(count)
