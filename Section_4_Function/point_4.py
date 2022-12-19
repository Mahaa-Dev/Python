# you can use thesame name for different variables as long as they are in different scopes.
def fr1():
    fruits = "orange"
    print(fruits)

def fr2():
    fruits = "banana"
    print(fruits)

fruits = "Apple"
fr1()
fr2()
print(fruits)