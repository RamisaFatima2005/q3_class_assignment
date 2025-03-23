# Basic import
import math
print(math.pi) # Output = 3.141592653589793

#Import with Alias (as)
import random as r
print(r.randint(1,20)) # Output = Random number between 1 to 20

import numpy as np
print(np.array([1,2,3,4])) # Output = [1 2 3 4]

#Import Specific Functions or Variables (from ... import ...)

from math import sqrt, floor
print(sqrt(25)) # Output = 5.0
print(floor(2.9)) # Output = 2

from math import sqrt as s, pi as p
print(s(4)) # Output = 2.0
print(p) # Output = 3.141592653589793

#Import Everything (from module import *) (Not recommended for large modules)
from math import *
print(sqrt(16)) # Output = 4.0
print(pi) # Output = 3.141592653589793
