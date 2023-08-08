l=[1,2,3,4,522,0,78]
l.sort() #it will sort in ascending order
l.sort(reverse=True) #it will sort in descending order
l.append(70) #it will add 70 element in the end
l.reverse() #it will print the elements in reverse order
print(l.index(3)) #it will print the element of the index
print(l.count(3)) #it will count the number of times the element present in the list
l.insert(1,34) #it will insert the new element in the list 
m=[233,55]
l.extend(m)
print(l+m)

print(l)
#copy
colors = ["voilet", "green", "indigo", "blue"]
newlist = colors.copy()
print(colors)
print(newlist)