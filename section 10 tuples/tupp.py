tuples1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tuples2 = ("apple","ball","cat","dog")
tuples3 = (2.5, False, [2, 4, 5])
print(tuples3)
print(tuples2)
print(tuples1)
print(tuples3.__sizeof__())
#looping
for fr in tuples2:
    print(fr)

#step
print(tuples1[::2])#stride length of 2
print(tuples1[1::2])#even only

##tuple methods
nested = ((1, 2, 3),(4, 5, 6),(7, 8, 9),(10, 11, 12))
print(nested[2])
print(nested[3][1])
#count
ness = (3, 5, 6, 3, 5, 2, 6, 3, 7,4,2)
print(ness.count(3))
#index
print(tuples1.index(3))