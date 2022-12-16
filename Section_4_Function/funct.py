def add():
    print(2 + 4)

add()

# Adding parameter
def newadd(para):
    print(para + 9)

newadd(8)

#multiple parameter
first = "Your name is"
def frname(p1, p2, p3):
    print(p1+str(p2)+p3)

frname(first, "shiv", "good")

#parameter with default value
def mul(num1=8, num2=9):
    print(num1 * num2)

mul()

#return
def mult(nm=5, nm1=6):
    return nm * nm1

product = mult(2)
print(product)

def hello_world_printer():
    print("Hello World")

hello_world_printer()

def name_printer(name1):
    print(name1)

name = input("Enter your Name: ")
name_printer("Your name is "+name)

## rectangular prism
length = int(input("Enter a length"))
width = int(input("Enter a width"))
height = int(input("Enter a height"))

def prism_vol(l, w, h):
    return l*w*h

print("The volume of rectangular prism is "+str(prism_vol(length, width, height))+" in cubic metre.")

## celsius to fahrenheit

celcius = int(input("Enter a degree celsius: "))

def fahrenheit(C):
    F = 1.8 * C + 32
    return round(F)

print("The fahrenheit value is"+str(fahrenheit(celcius)))