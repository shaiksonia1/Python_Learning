# sonia={"hello","my","name","is"}
# print(sonia)

s1={'name':'Ankit','Rollno':29,'marks':78}
s2={'name1':'sonia','Rollno2':30,}
print(s1)# will print all the values
print(s1['name'])#will print the value of name in the dictionary
print(s1.get('marks'))#will print the value of marks
print(s1.items()) #will print the items of dictionary
print(s1.keys())#will print the keys of dictionary like name, rollno,marks


#dictionary methods
s1.update(s2)
print(s1) # will update with s1+s2
s1.pop('Rollno')
print(s1) #will remove the rollno
s2.popitem()
print(s2) #will remove the last item of dictionary
s1.clear() # will clear s1 dictionary
del s1["name"]
print(s1) # will delete the name in the dictionary

# to create empty dictionary
empt={}
print(empt)