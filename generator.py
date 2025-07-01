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

    
