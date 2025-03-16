# In Python, a dictionary is a collection of key-value pairs. It is used to store data in an organized way, where each key has a corresponding value.

# Key Points:
# Created using {} (curly brackets)
# Keys must be unique and immutable (like strings, numbers, or tuples)
# Values can be of any data type

info:dict = {
    "name": "Ramisa",
    "age":19,
    "slot":"Monday 2-5"
}

print(info) #Output = {'name': 'Ramisa', 'age': 19, 'slot': 'Monday 2-5'}

# Using dict() Constructor:
# Instead of using curly braces {}, you can use dict() to create a dictionary.

dictionary:dict = dict(Country="Pakistan", Language="Urdu", Capital="Islamabad")

# Accessing Value
student = {
    "name":"Hadi",
    "age": 10
}
print(student["name"]) # Output = Hadi
print(student.get("age", 15)) # Output = 10 (if key is missing, it returns 15)
print(student.get("Progress", "Brilliant Student")) # Output = Brilliant Student

stdinfo = {
    "name": "Hooriya",
    "age": "12",
    "class": 3
}

# Updating an Existing Value
stdinfo["class"] = 4
print(stdinfo) # Output = {'name': 'Hooriya', 'age': '12', 'class': 4}

# Adding a New Key-Value Pair
stdinfo["section"] = "S.F" # Output = {'name': 'Hooriya', 'age': '12', 'class': 4, 'section': 'S.F'}

#  Using update() to Modify Multiple Values
stdinfo.update({"name":"Kiswa", "age":14, "class": 5})
print(stdinfo) # Output = {'name': 'Kiswa', 'age': 14, 'class': 5, 'section': 'S.F'}

# Removing a Key Using del
del stdinfo["section"]
print(stdinfo) # Output = {'name': 'Kiswa', 'age': 14, 'class': 5}

# Using pop() to Remove a Key and Get Its Value
grade = stdinfo.pop("class")
print(grade) # Output = 5
print(stdinfo) # Output = {'name': 'Kiswa', 'age': 14}

# Removing the Last Inserted Item Using popitem()
stdinfo.popitem()
print(stdinfo) # Output = {'name': 'Kiswa'}


# Methods
teacher = {
    "name": "Miss Fatima",
    "role": "Class Teacher",
    "class": 6
}

# keys() = Returns a list of all keys in the dictionary.
print(teacher.keys()) # Output = dict_keys(['name', 'role', 'class'])

# values() = Returns a list of all values in the dictionary.
print(teacher.values()) # Output = dict_values(['Miss Fatima', 'Class Teacher', 6])

# items() = Returns a list of key-value pairs as tuples.
print(teacher.items()) # Output = dict_items([('name', 'Miss Fatima'), ('role', 'Class Teacher'), ('class', 6)])

# clear() = Removes all items from the dictionary.
print(teacher.clear()) # Output = None

# Duplicate Key Not Allowed
bio = {
    "name": "Ali",
    "age": 25,
    "city": "Karachi",
    "age": 30  # This will overwrite the previous "age": 25
}

print(bio) #Output = {'name': 'Ali', 'age': 30, 'city': 'Karachi'}

# Iterating Over a Dictionary
flower = {
    "name": "Rose",
    "class": "Rosaceae",
}

for info in flower:
    print(info) # Output = name, class

for key, value in flower.items():
    print(key, "=", value) # output = name = Rose, class = Rosaceae

print(len(flower)) # Output = 2

# copy() = Copying a dictionary
alto = {
    "brand": "Suzuki",
    "model": "Alto",
    "year": 2023,
    "seating_capacity": 4
}
print(alto) # Output = {'brand': 'Suzuki', 'model': 'Alto', 'year': 2023, 'seating_capacity': 4}
print(alto.copy()) # Output = {'brand': 'Suzuki', 'model': 'Alto', 'year': 2023, 'seating_capacity': 4}
