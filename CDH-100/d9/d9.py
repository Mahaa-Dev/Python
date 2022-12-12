a = "1"
b = "2"
print(a+b)

# here a and b is string so it concat instead of adding

# typecasting
print(int(a)+int(b))
# explicit is done by user
string = "15"
number = 7
st_num = int(string)  # throws an error if the string is not a valid integer
sum = number+st_num
print("The sum is", sum)


# implicit is done by python
c = 9.8
d = 4
print(c+d)
