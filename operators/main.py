# 1. Unary operators
# Negative (-), Logical Not (not)

a = 6
b = -a
print(a) # Output = 6
print(b) # Output = -6

c = True
d = not c
print("c =", c) # Output = True
print("d =", d) # Output = False

# 2. Bitwise not (~)
e = 6
f = ~e
print("e = ", e) # Output = 6
print("f = ", f) # Output = -7

g = -2
h = ~g
print("g = ", g) # Output = -2
print("h = ", h) # Output = 1

# Binary Operators
# 3. Arithmetic Operators
# +, -, *, /, //, %, **

i = 7
j = 5
# Add (+)
print(i + j) #Output = 12
# Subtract (-)
print(i - j) #Output = 2
# Multiply (*)
print(i * j) #Output = 35
# Divide (/)
print(i / j) #Output = 1.4
# Floor Division (//) -Remove the decimal part
print(i // j) #Output = 1
# Modulus (%)
print(7 % 5) #Output = 2
# Exponentiation (**)
k = 2
l = 2
m = 3
print(k ** l) # 2 * 2 = 4 -Output = 4
print(k ** m) # 2 * 2 * 2 = 8 -Output = 8

# 4. Comparision Operators
# ==, !=, >, <, >=, <=
n: int = 6
o: int = 8

print("== ", n == o)  # False
print("!= ", n != o)  # True
print("> ", n > o)   # False
print("< ", n < o)   # True
print(">= ", n >= o)  # False
print("<= ", n <= o)  # True

# 5. Logical Operators
# and, or, not

p = 5
q = 4
print(p > q and p < q) # Output = False
print(p > q or p < q) # Output = True
print(not(p < q)) # Output = True

# 6. Assignment Operators

r = 9
print(r) # Output = 9
r += 2
print(r) # 9 + 2 = 11
r -= 2
print(r) # 11 - 2 = 9
r *= 2
print(r) # 9 * 2 = 18
r /= 2
print(r) # 18 / 2 = 9
r //= 2
print(r) # 9 // 2 = 4

# 7. Identity Operators
# is, is not

s = 1
t = 3
print(s is t) #Output = False
print(s is not t) #Output = True

# 8. Membership Operators
# in, in not

u = ["apple", "mango", "banana", "strawberry"]
print("mango" in u) # Output = True
print("banana" not in u) # Output = False