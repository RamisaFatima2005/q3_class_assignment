# Built-in Modules (Standard Library)

# math = Mathematics related functions
# random = Random numbers generate karne ke liye
# os = Operating system related kaam ke liye
# sys = System-related information access karne ke liye

import math

print(math.sqrt(16)) # Output = 4.0
print(math.ceil(2.9)) # Output = 3
print(math.floor(2.9)) # Output = 2
print(math.pi) # Output = 3.141592653589793

import random

print(random.randint(1,10)) # Output = Random number between 1 to 10
print(random.random()) # Output = Random float number between 0 to 1
print(random.choice([1,2,3,4,5])) # Output = Random number from list
print(random.choices([1,2,3,4,5], k=3)) # Output = Random 3 numbers from list

import os

print(os.getcwd()) # Output = Current working directory
print(os.listdir()) # Output = List of files and directories
print(os.path.exists(r"C:\Users\hp1\Desktop\coding\Q3\giaic\assignments\q3_class_assignment\modules_functions\main.py")) # Output = True
print(os.path.exists("python.py")) # Output = False 


import sys

print(sys.version) # Output = Python version
print(sys.path) # Output = List of directories in Python path
print(sys.platform) # Output = Operating system platform
print(sys.modules) # Output = List of modules


#importing module from another file

import module

print(module.add(5,5)) # Output = 10
print(module.difference({1,2,3,4}, {3,4,5,6})) # Output = {1, 2}

#External Modules (Third-party Libraries)

import requests

response = requests.get("https://api.github.com")  # GitHub API se data fetch karna
print(response.status_code)  # Output = 200 means request successful