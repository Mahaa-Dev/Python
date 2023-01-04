myList = [4, 2, 3, 2, 10]
myStringList = ["a", "b", "c", "d"]
myString = "The weather is really good today!"

for num in myList:
    if num == 4:
        print("Number found")  # True

for c in myStringList:
    if c == 'c':
        print("c is found", c)
# 0 in myList  # False
# 0 in myStringList  # False
# "c" in myStringList  # True
# "e" in myStringList  # False
# "weather" in myString  # True
# "really" in myString  # True
# "rain?" in myString  # False
