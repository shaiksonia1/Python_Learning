import math
result=math.sqrt(9)
print(result)

#from keyword
#You can also import specific functions or variables from a module using the from keyword.
from math import sqrt,pi
result=math.sqrt(10)*pi
print(result)

#importing everything
#It's also possible to import all functions and variables from a module using the * wildcard
from math import *
result=sqrt(8)
print(result)
print(pi)

#The "as" keyword
#Python also allows you to rename imported modules using the as keyword.
import math as m
result=m.sqrt(5)
print(result)
print(m.pi)

#The dir function
#Python has a built-in function called dir that you can use to view the names of all the functions and variables defined in a module. 
import math
print(dir(math))