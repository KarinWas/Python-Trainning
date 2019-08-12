#Ex 3.1
#a
def hello_world():
    print ("Hello, world!")

#b
def hello_world(name):
    print("Hello, " + name + "!")

#Ex 3.2
def polynomial(x):
    calc = 3*(x**2) - x + 2
    print (calc)

#Ex 3.3
def my_max(x,y):
    if (x<y):
        return y
    return x

#Ex 3.4
#a
def is_primeA(n):
    for i in range (2, n):
            if (n % i == 0):
                return False
    return True

#b
def is_primeB(n):
    if ((n != 2) and (n!= 3)):
        for i in range(1, n):
            if (((6*i + 1) == n) or (6*i - 1) == n):
                return True
    return False

#c
def all_primes(n):
    primes = []
    for i in range(2,n):
        for j in range (2,i):
            if (i % j == 0):
                break
        else:
            primes.append(i)
    return primes

#d
def first_n_primes(n):
    counter = 1
    number = 2
    primes = []
    while (counter <= n):
        if (is_primeA(number)):
            counter += 1
            primes.append(number)
        number += 1
    return primes

#Ex 3.5
#a

if __name__== "__main__":
    hello_world("Karin")
    polynomial(3)
    print(my_max(3,5))
    print(is_primeA(7))
    print(is_primeB(8))
    print(all_primes(13))
    print(first_n_primes(7))