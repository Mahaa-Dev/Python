# while loop
i = 0
while (i < 3):
    print(i)
    i = i + 1

j = 5
while (j > 0):
    print(j)
    j = j - 1
else:
    print("I am in else condition")

while True:
    number = int(input("Enter a positive number: "))
    print(number)
    if not number > 0:
        break
