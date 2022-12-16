# import random
#
# print(random.randint(1, 10))

# from random import randint
# print(randint(2, 10))

# universal

# from random import *
# print(random())
import random
ran1 = random.randint(10, 25)
ran2 = random.randint(200, 400)

car_mph = round((ran2 / ran1), 2)

print("Car miles is ", car_mph)

from random import randint
# generates random integer between and inclusive of 10 and 25 to represent gas in the car's fuel tank
fuel = randint(10, 25)
# generates random integer between and inclusive of 200 and 400 to represent miles the car can go without refueling
miles = randint(200, 400)
# calculates and displays the MPG of the car assuming car manufacturers overestimates in their claims
print("The car can travel " + str(miles // fuel) + " miles per gallon.")
# displays the number of gallons of fuel that the car's fuel tank can hold
print("The car's fuel tank can hold " + str(fuel) + " gallons.")
# displays the number of miles that the car can travel on a full tank
print("The car can travel " + str(miles) + " miles on a full tank.")