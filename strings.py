name="sonia"
print("hello," + name)

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print("lets use for loop ")
for character in name:
    print(character)

#slicing a string
name="sonia"
print(name[2:5])

#length of string
name="sonia"
len1=len(name)
print(len1)
name="sonia"
len1=len(name)
print(name[-1:-3])

#practice
nm="harry"
print(nm[-4:-2])

#string methods -> strings are immutable
"""
string upper()
string lower()
rstrip()
replace()
split()
capitalize()
center()
count()
endswith()
startswith()
find()
isalnum()
isalpha()
islower()
isupper()
isprintable()
isspace()
istitle()
swapcase()
title()


"""
#string upper()
str1="sonia"
print(str1.upper())

#string lower()
a="SONIA"
print(a.lower())

#rstrip()
b="world!!!!"
print(b.rstrip("!"))

#it will not srip the leading character in a string
c="!!!Ali"
print(c.rstrip("!"))

#capitalize
str1="hello"
capstr1=str1.capitalize()
print(capstr1)

#center()
c="hello world!"
print(c.center(40))

#count()
d="hello,hello,hello"
print(d.count("hello"))

#endswith()
e="hello world!"
print(e.endswith("!"))

#startswith()
f="hello"
print(f.startswith("h"))

#find()
g="harry"
print(g.find("a"))

#isalnum()
h="heelo23F"
print(h.isalnum())

#isalpha()
i="soniaaa"
print(i.isalpha())

#islower()
j="HELLO"
print(j.islower())

#isupper()
k="hello"
print(k.isupper())

#isprintable()
l="my name is sonia \n"
print(l.isprintable())

#isspace()
m="hi, sonia"
print(m.isspace())

#istitle()
n="hello"
print(n.istitle())

#swapcase()
p="heelloo"
print(p.swapcase())

#title()
p="heelloo"
print(p.title())