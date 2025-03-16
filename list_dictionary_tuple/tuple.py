# Tuple is a collection of ordered, immutable, and indexed elements.
# Tuple is defined using parentheses (). It is similar to a list but cannot be modified.
# Tuple is faster than a list because of its fixed size.
# Tuple is used to store multiple items in a single variable.
# Tuple is used when the data should not be changed or modified.
# Tuple is used when the data should be accessed by position or index.

fruits = ('apple', 'banana', 'cherry')
print(fruits) # Output = ('apple', 'banana', 'cherry')
# Accessing Tuple Items
print(fruits[1]) # Output = banana
# Negative Indexing
print(fruits[-1]) # Output = cherry

# Tuple with different data types
mixed = ('apple', 1, 2.5, True)
print(mixed) # Output = ('apple', 1, 2.5, True)

# Tuple slicing
colors = ('red', 'blue', 'green', 'yellow', 'black')
print(colors[1:4]) # Output = ('blue', 'green', 'yellow')

# Loop through a tuple
companies = ('Google', 'Microsoft', 'Apple', 'Amazon')
for company in companies:
    print(company) # Output = Google, Microsoft, Apple, Amazon

# Length of a tuple
flowers = ('rose', 'lily', 'jasmine', 'lotus')
print(len(flowers)) # Output = 4

# Count the number of items in a tuple
numbers = (1, 2, 3, 4, 5, 2, 3, 2)
print(numbers.count(5)) # Output = 1

# Find the index of an item in a tuple
animals = ('dog', 'cat', 'elephant', 'lion', 'tiger')
print(animals.index('elephant')) # Output = 2   

# Tuple unpacking
biodata = ('Ramisa', 19, 'Karachi')
name, age, city = biodata
print(name) # Output = Ramisa
print(age) # Output = 19    
print(city) # Output = Karachi