name = "shiv"

print("Hello" + name)

st = '''Hi shiv
what's up
what are you doing ?
'''
print(st)

print(name[0])
print(name[1])
print(name[2])
print(name[3])
# print(name[4])## This throws an error index out of range

print("let's do for loop\n")

# for character in name:
#     print(character)

for character in st:
    print(character)
