# add implementation
def add(x,y) :
    return x+y    # on Bug123
# subtract implementation
def subtract(x,y):
    return x-y      # on master
# multiply implementation
def multiply(x,y) :
    return x*y    #on Bug456
# divide implementation
def divide(x,y) :
    if y==0:
        return DIVIDE_BY_0_ERROR   # on Bug789
    else:
        return x/y
