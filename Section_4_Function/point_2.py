# global variables can be accessed by code in a local scope
glob = "this is globsl var"
def pg():
    print(glob)

pg()