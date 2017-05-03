import math

a = (1,2,3)
b = (3,4,5)

rel = tuple(map(lambda a, b: a + b, a, b))

print(' a:',a)
print(' b:',b)
print('rel',rel)


square = lambda x: x * x
print(square(3))
print(list(map(square, a)))
print(tuple(map(square, a)))


def tripple(x):
    return x*3

def iseven(x):
    return x % 2 == 0

e = range(1,20)
print( list(map(tripple,e)) )
print( list(filter(iseven, e)) )


e = range(1,20)
print( [x*3 for x in e] )
print( [ x for x in e if x % 2 == 0])