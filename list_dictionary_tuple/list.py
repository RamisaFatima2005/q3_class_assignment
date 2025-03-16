# List
# Ordered = Items maintain a fixed order.
# Mutable = Can be modified (add, change, remove).
# Duplicates Allowed = Same values can repeat.
# Mixed Data Types = Stores numbers, strings, etc.
# Indexing & Slicing = Access elements by position.
# Dynamic Size = Expands or shrinks as needed.
# Loop Support = Can iterate using loops.
# Built-in Methods = Includes append(), remove(), sort(), etc.

fruit = ['apple', 'banana', 'cherry']
print(fruit) # Output: ['apple', 'banana', 'cherry']
# Accsessing Items by index
print(fruit[1]) # Output: banana
# Negative Indexing
print(fruit[-1]) # Output: cherry
# Modifying List Items
fruit[0] = 'orange'
print(fruit) # Output: ['orange', 'banana', 'cherry']

#List slicing

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[0:5]) # Output: [1, 2, 3, 4, 5]
print(numbers[5:]) # Output: [6, 7, 8, 9]
print(numbers[:5]) # Output: [1, 2, 3, 4, 5]

# Common List Methods

# append() = Add an element at the end of the list
vegetable = ['potato', 'tomato', 'onion']
vegetable.append("carrot")
print(vegetable) # Output: ['potato', 'tomato', 'onion', 'carrot']

# extend() = Add multiple elements to the list
flowers = ['rose', 'lily', 'jasmine']
addflowers = ['sunflower', 'tulip']
flowers.extend(addflowers)
print(flowers) # Output: ['rose', 'lily', 'jasmine', 'sunflower', 'tulip']

# remove() = Removes a specific element by value.	
flowers.remove('tulip')
print(flowers) # Output: ['rose', 'lily', 'jasmine', 'sunflower']

# pop() = Removes an element by index.
stationary = ['pen', 'pencil', 'eraser']
stationary.pop(1)
print(stationary) # Output: ['pen', 'eraser']

# sort() = Sort the list in ascending order
num = [7,5,6,4,3,8]
num.sort()
print(num) # Output: [3, 4, 5, 6, 7, 8]

# sort() = Sort the list in descending order
number = [12,50,7,20]
number.sort(reverse=True)
print(number) # Output: [50, 20, 12, 7]

# sort() = Sorted by string length
colours = ['red', 'green', 'blue', 'yellow']
colours.sort(key=len)
print(colours) # Output: ['red', 'blue', 'green', 'yellow']

#sort() = Sorting a List of Strings by the Last Character
nature = ['tree', 'flower', 'mountain', 'river']
nature.sort(key=lambda nature:nature[-1])
print(nature) # Output: ['tree', 'mountain', 'flower', 'river']

# reverse() = Reverse the order of the list
alphabets = ['a', 'b', 'c', 'd']
alphabets.reverse()
print(alphabets) # Output: ['d', 'c', 'b', 'a']

# index() = Find the index of an element
language = ['English', 'Urdu', 'Chinese', 'Arabic']
print(language.index('Arabic')) # Output: 3

# count() = Count the number of times an element appears in the list
mixnum = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2]
print(mixnum.count(3)) # Output: 2

# copy() – Create a copy of the list
cars = ['toyota', 'honda', 'suzuki']
newcars = cars.copy()
print(cars) # Output: ['toyota', 'honda', 'suzuki']
print(newcars) # Output: ['toyota', 'honda', 'suzuki']

# clear() – Remove all elements from the list
fabric = ['cotton', 'silk', 'wool']
fabric.clear()
print(fabric) # Output: []