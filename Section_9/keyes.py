dictionary = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
print(dictionary.keys())

for key in dictionary.keys():
    print(key)

print(dictionary.values())

print(dictionary.items())

for key, value in dictionary.items():
    print(key, value)

if "a" in dictionary:
    print(dictionary["a"])
else:
    print("Not in dictionary")

print(dictionary.get("f", "try again"))