def add(a,b):
    def inner(c,d):
        return c + d
    return inner(a,b)

a = add(2,3)
print(a)