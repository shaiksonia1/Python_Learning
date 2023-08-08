#tuple count
tuple1=("red","green","pink","white")
res=tuple1.count("red")
print(res)

#tuple index

tuple2=(1,2,3,4,5,6,7,7)
res=tuple2.index(4)
print(res)

#manipulating tuple 
countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)

#same like lists other functions