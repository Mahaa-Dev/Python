num = int(input("Enter a number: "))
if num < 0:
    print("Number is less than zero.")
elif num == 0:
    print("Number is equal to zero")
elif 0<num<=100:
    print("Number is between 0 and 100")
else:
    print("Number is greater than 100")
