ex2 = {}.fromkeys(["address"],"lahan")
print(ex2)
#takes two argument
#The first argument needs to be an iterable value, such as a list or string.
#The second arguments will be used as a value by the dictionary that from returns.

ex3 = {"name:":"bidhan","age":20,"subject":"IPPS"}
ex3.pop("age")#remove key value
print(ex3)

for key, value in {}.fromkeys("bcdfghjklmnpqrstvwxyz", "consonant").items():
    print(key, value)

fast_food_items = {"McDonald's": "Big Mac", "Burger King": "Whopper", "Chick-fil-A": "Original Chicken Sandwich"}
print(fast_food_items.pop("McDonald's"))

fast_food_items.popitem()
print(fast_food_items)