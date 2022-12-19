# local variables cannot be used by code in the global scope
def lc():
    bt = "hello"
    return bt
lc()
print(bt)