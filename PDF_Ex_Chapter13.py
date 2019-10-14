import numpy as np
#Ex 1
def collatz_sequence(n):
    while (n != 1):
        yield n
        if (n%2 == 0):
            n = int(n/2)
        else:
            n = int(3*n + 1)
    yield 1
        
#Ex 2
def collatz_numpy():
    iterable = collatz_sequence(61)
    return np.fromiter(iterable, int)

#Ex 3
def prime_num(n):
    counter = 0
    number = 2
    while (counter != n):
        if check_prime(number):
            yield number
            counter+=1
        number += 1
        

def check_prime(n):
    for divider in range (2, n):
        if (n % divider == 0):
            return False
    else:
        return True

if __name__== "__main__":
    print(list(collatz_sequence(103)))
    print(collatz_numpy())
    print(list(prime_num(10000)))