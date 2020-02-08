def add(a,b):
    return a + b

def square_it(func):
    def sq(k,j):
        return k * k
    return sq

@square_it
def addition(e,f):
    return add(e,f)

g = addition(2,5)
print(addition(3,5))
print(g)