# Python Math Modul

import math
# abs() - Returns the absolute value of a number
print(abs(-7.25)) # Output : 7.25

# pow() - Returns the value of x to the power of y
print(pow(4, 3)) # Output : 64

# round() - Rounds a numbers
print(round(7.25)) # Output : 7
print(round(7.25, 1)) # Output : 7.2

# max() - Returns the largest of the numbers
print(max(7, 9, 10)) # Output : 10

#min() - Returns the smallest of the numbers
print(min(7, 9, 10)) # Output : 7

#math.sin() - Returns the sine of a number
print(math.sin(90)) # Output : 0.8939966636005579

# math.cos() - Returns the cosine of a number
print(math.cos(90)) # Output : -0.4480736161291701

# math.tan() - Returns the tangent of a number
print(math.tan(90)) # Output : -1.995200412208242

# math.sqrt() - Returns the square root of a number
print(math.sqrt(64)) # Output : 8.0

# math.factorial() - Returns the factorial of a number
print(math.factorial(5)) # Output :
# 5 * 4 * 3 * 2 * 1 = 120

# math.log() - Returns the natural logarithm of a number
print(math.log(10)) # Output : 2.302585092994046

# math.log10() - Returns the base-10 logarithm of a number
print(math.log10(10)) # Output : 1.0

# math.exp() - Returns E raised to the power of x
print(math.exp(2)) # Output : 7.3890560989306495

# math.ceil() - Rounds a number upwards to the nearest integer, and returns the result
print(math.ceil(1.4)) # Output : 2

# math.floor() - Rounds a number downwards to the nearest integer, and returns the result
print(math.floor(1.4)) # Output : 1

# math.pi - Returns the value of PI
print(math.pi) # Output : 3.141592653589793

# math.e - Returns the value of e
print(math.e) # Output : 2.718281828459045

# math.inf - Returns a positive infinite number
print(math.inf) # Output : inf

# math.nan - Returns a NAN (Not A Number)
print(math.nan) # Output : nan

# math.tau() - Representing the ratio of the circumference of a circle to its diameter, which is approximately 3.14159
print(math.tau) # Output : 6.283185307179586

positive_infinity = math.inf
print(positive_infinity > 999999999999999999) # Output : True