'''
A set is a data type that consists of a collection of items, much like a list.

However, sets differ from lists in two important ways.

The first is that they cannot have duplicate values in them, and the second is that the items they

contain are unordered, like the key value pairs of a dictionary.
'''
set_1 = {1, 2, 3, 4, 5, 6}
set_2 = set({"apple","ball","cat","dog"})
print(set_1)
print(set_2)
set_3 = set(range(1, 12, 2))
print(set_3)

print(4 in set_1)

'''
Sets are useful in situations where you want to use a collection of items, but you don't want duplicate

items in the collection, and you also don't care about the order of the items that make up the collection.
'''
scifif = {"apple","banana","cagger","donkey","eye"}
scifif.add("aanda")
print(scifif)

## set comprehensions
comp1 = {even+2 for even in range(2, 11, 2)}
print(comp1)

comp2 = {char.lower() for char in "ALLCAPS"}
print(comp2)