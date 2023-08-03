#local variable 
def demo():
    x= 9 #local variable 
    print(x)
demo()

#local variables are used inside the function and cannot be accessed outside the function

def demo():
    x=10
    print(x)
demo()
#print(x) #it will show x is not defined because it is in local variable it cannot be accessed through globally


#global variable

#These are those which are defined outside any function and which are accessible throughout the program,
#  i.e., inside and outside of every function

# This function uses global variable s
def sa():
    print("i can do it", s)
# Global scope
s = "one day"
sa()
print("outside function", s)
 # This function uses global variable s

