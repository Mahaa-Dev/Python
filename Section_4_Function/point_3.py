# the local scope of one function can't be use variables from another function's local scope
def fst():
    loc = 2
    return loc
def scnd():
    return loc

fst()
scnd()