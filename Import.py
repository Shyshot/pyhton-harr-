"""This Used to Import a Method"""

import math
print(math.pi)
print(math.sqrt(97589) * math.pi)

"""This Imports Specific methods of the imported module"""

from math import sqrt, pi
print(pi)
print(sqrt(97589) * pi)

"""* is used to import all the methods of the imported Module. It is similar to import math but does not require mention of the module to call the method"""

from math import *
result = sqrt(9)
print(result)  # Output: 3.0

print(pi)  # Output: 3.141592653589793

"""dir(*) returns all the Available methods of the imported Module"""

import math

print(dir(math))              
