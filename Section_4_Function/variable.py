example = "Hello world" # variable created outside a function is global scope i.e, global variable
def loc():
    example="This is aexample" # variable created within afunction is local scope :ie, local variable
    return example

print(example)
print(loc())

# WHY is understanding variable scope important ?
# local variables cannot be used by code in the global scope
# global variables can be accessed by code in a local scope
# the local scope of one function can't be use variables from another function's local scope
# you can use thesame name for different variables as long as they are in different scopes.