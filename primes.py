def check_prime(n):
    for divider in range (2, n):
        if (n % divider == 0):
            return False
    else:
        return True

def check_a_smaller_b(a,b):
    return a < b

if __name__ == '__main__':
    a = int(input("please insert a number:"))
    b = int(input("please insert a number bigger than the first:"))
    while (not check_a_smaller_b(a, b)):
        print("you entered a number smaller/equal to the first")
        b = int(input("please insert a number bigger than the first:"))

    for number in range(a,b + 1):
        if (check_prime(number)):
            print (number)