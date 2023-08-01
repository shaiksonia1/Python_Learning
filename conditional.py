"""
conditional operators:
<,>,<=,>=,==,!=
"""
#if
a=int(input("enter your age:"))
print("your age is:",a)
if(a<18):
    print("you cannot drive.")
    print("oops!")
else:
    print("you can drive.")
    print("yay!")
print("hey") #this is outside the ELSE BLOCK.

#if-else
appleprice=120
budget=20
if(appleprice<=budget):
    print("add to the cart")
else:
    print("do not add to the cart")
#elif
#ex:1
appleprice=10
budget=200
if(budget-appleprice>200):
    print("add to the cart")
elif(budget-appleprice>70):
    print("you can buy the apple")
else:
    print("do not add to the cart")

#ex2:
num=int(input("enter a number:"))
if(num<0):
    print("number is negative")
elif(num==0):
    print("number is zero")
elif(num==999):
    print("number is special")
else:
    print("number is positive")
print("yay!")

#nested if-else-if
num=3
if(num<0):
    print("number is negative")
elif(num>0):
    if(num<=10):
        print("number is between 1-10")
    elif(num>10 and num<=20):
        print("number is btwn 11-20")
    else:
        print("no is greater than 20")
else:
    print("no is zero")

    #matchcase statements

#  x = 4
# # x is the variable to match
# match x:
#     # if x is 0
#     case 0:
#         print("x is zero")
#     # case with if-condition
#     case 4 if x % 2 == 0:
#         print("x % 2 == 0 and case is 4")
#     # Empty case with if-condition
#     case _ if x < 10:
#         print("x is < 10")
#     # default case(will only be matched if the above cases were not matched)
#     # so it is basically just an else:
#     case _:
