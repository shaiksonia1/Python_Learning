"""
Lists are ordered collection of data items.
They store multiple items in a single variable.
List items are separated by commas and enclosed within square brackets [].
Lists are changeable meaning we can alter them after creation.
"""

list1 = ["red","green","pink","blue"]
print(list1)

# Accessing list items
list1 = ["red","green","pink","blue"]
print(list1[3])

# Negative Indexing:
list1 = ["red","green","pink","blue"]
print(list1[-3])
print(list1[len(list1)-3])
print(list1[1])

# Check whether an item in present in the list?
colors=["red","green","bule","pink","orange"]
if "green" in colors:
    print("yes")
else:
    print("no")

    # Range of Index:

    # listName[start : end : jumpIndex]
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[3:7])	#using positive indexes
print(animals[-7:-2])	#using negative indexes'


# Example: Printing alternate values
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[::2])		#using positive indexes
print(animals[-8:-1:2])	#using negative indexes

# Here, we have not provided start and index, 
# which means all the values will be considered. 
# But as we have provided a jump index of 2 only alternate values will be printed.

animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[1:8:3])
# Here, jump index is 3. Hence it prints every 3rd element within given index.