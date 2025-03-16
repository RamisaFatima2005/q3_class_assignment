# A set in Python is an unordered, unindexed collection of unique elements. It is mutable (can be modified) but does not allow duplicates.

# Creating Sets
# Use {} or set(), but an empty set must be created with set().
# Key Properties
# Unordered = No fixed order.
# Unique = Duplicates are removed automatically.
# Mutable = Can add/remove elements.
# Unindexed = No direct access via index.

# In Python, sets are unordered, so their elements don’t follow a fixed sequence.

# Key Points:
# The order of elements in a set can change each time you print it.
# {apple, mango, banana} may appear as {banana, apple, mango} or {mango, banana, apple}.
# Sets don’t support indexing, so elements have no fixed position.

set1: set = {1,2,3,4}
set2: set = {1,2,3,4}
print('set1 = ',set1) # Output = set1 =  {1, 2, 3, 4}
print('set2 = ',set2) # Output = set2 =  {1, 2, 3, 4}
print('set1 = ',type(set1)) # Output = set1 =  <class 'set'>
print('set2 = ',type(set2)) # Output = set2 =  <class 'set'>
print(set1 == set2) # Output = True


# Adding Elements

colors={'blue', 'yellow', 'green'}
print(colors) # Output = {'yellow', 'blue', 'green'}

# add(x) = Adds a single element.
colors.add('white')
print(colors) # Output = {'yellow', 'white', 'blue', 'green'}

# update([x, y]) = Adds multiple elements.
colors.update(['brown', 'purple', 'pink'])
print(colors) # Output = {'purple', 'green', 'white', 'pink', 'blue', 'yellow', 'brown'}



# Removing Elements

flower = {"Rose", "Sunflower", "Tulip", "Jasmine", "Daffodil"}
print(flower) # Output = {'Tulip', 'Jasmine', 'Daffodil', 'Rose', 'Sunflower'}

# remove(x) = Removes x, error if not found.
flower.remove("Tulip")
print(flower) # Output = {'Jasmine', 'Daffodil', 'Rose', 'Sunflower'}

# discard(x) = Removes x, no error if not found.
flower.discard("Sunflower")
print(flower) # Output = {'Jasmine', 'Daffodil', 'Rose'}

# pop() = Removes a random element.
flower.pop()
print(flower) # Remove random flower

# clear() = Removes all elements.
flower.clear()
print(flower) # Output = set()



# Set Operations
num1 = {1,2,3,4}
num2 = {3,4,5,6}
print(num1) # Output = {1,2,3,4}
print(num2) # Output = {3,4,5,6}

# Union (|) = Combines sets.
num3 = num1.union(num2)
print(num3) # Output = {1, 2, 3, 4, 5, 6}
print(num1 | num2) # Output = {1, 2, 3, 4, 5, 6}

# Intersection (&) = Common elements.
num4 = num1.intersection(num2)
print(num4) # Output = {3, 4}
print(num1 & num2) # Output = {3, 4}

# Difference (-) = Elements in A, not in B.
num5 = num1.difference(num2)
print(num5) # Output = {1, 2}
print(num1 - num2) # Output = {1, 2}

# Symmetric Difference (^) = Elements in either, not both.
num6 = num1.symmetric_difference(num2)
print(num6) # Output = {1, 2, 5, 6}
print(num1 ^ num2) # Output = {1, 2, 5, 6}

# Checking Membership
print(2 in num1)
print(2 in num2)

# difference_update()
fruits = {"apple", "banana", "mango", "grapes", "orange"}
print("Before:", fruits) #Output =  Before: {'orange', 'mango', 'apple', 'banana', 'grapes'}
fruits.difference_update({"banana", "orange", "mango"})
print("After:", fruits) #Output = After: {'apple', 'grapes'}

# issuperset / issubset
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}

# Subset check (A is a subset of B)
print(A.issubset(B))  # True
print(A <= B)         # True 

# Superset check (B is a superset of A)
print(B.issuperset(A))  # True
print(B >= A)           # True 



# Frozen Set
# A frozenset is an immutable set (cannot be modified).

frozen = frozenset([1, 2, 3])
# frozen.add(4)  # Error: frozenset is immutable
print(frozen) # Output = frozenset({1, 2, 3})