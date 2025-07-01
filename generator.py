def even_generator():
    x = 0
    while(True):
        x+=2
        yield x

import types
if type(even_generator()) == types.GeneratorType:
    print("The type is generator")

    even = even_generator()
    for _ in range(10):
        print(next(even))


def square_generator(n):
    i = 1
    while (i<=n):
        yield i**2
        i+=1
import types

x = int(input("how many terms do you want the series till: "))
if type(square_generator(x)) == types.GeneratorType:
    print("This is generator type")
    print("The series of squares from 1 to %d term are given below" %(x))
    square = square_generator(x)
    for _ in range(x):
        print(next(square))