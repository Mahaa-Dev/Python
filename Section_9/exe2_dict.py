dict2 = {"Queen": "Bohemian Rhapsody",
         "Bee Gees": "Stayin' Alive",
         "U2": "One",
         "Michael Jackson": "Billie Jean",
         "The Beatles": "Hey Jude",
         "Bob Dylan": "Like A Rolling Stone"}

print(len(dict2))

for key in dict2.keys():
    print(key)

print(dict2.values())

for key, value in dict2.items():
    print(key, value)

print(dict2.get("Promise of the Real", "not found"))