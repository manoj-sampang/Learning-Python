def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_generator(n):
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            yield num
            count += 1
        num += 1

# Test code
import types

x = int(input("Enter how many prime numbers you want: "))
if isinstance(prime_generator(x), types.GeneratorType):
    print("Yes, it's a generator")

    for prime in prime_generator(x):
        print(prime)
