#enuumerate function
#enumerate is built in function in python to loop over a sequence such as list,tupple and string
#it will give the output value and value of index
names = ["sonia","nafia","lauhith","ankit"]
for index , names in enumerate(names):
    print(index,names)

#changing the start of index
#by giving start as 1
a = [34,55,66,77,88,22,]
for index,a in enumerate(a, start=1):
    print(index,a)