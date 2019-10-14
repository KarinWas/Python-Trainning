#Ex 1
def Power(a, b):
    if (b == 0):
        return(1)
    elif (b==1):
        return(a)
    else:
      return a * Power (a, b-1)

#Ex 2
def myrecfilter(function, data):
    data = list(data)
    if len(data) == 0:
        return ""
    else:
        if (function(data[0])):
            return str(data[0]) + myrecfilter(function, data[1:])
        return ""+ myrecfilter(function, data[1:])

def filterVowels(alphabet):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if(alphabet in vowels):
        return True
    else:
        return False

def myrecmap(function, data):
    data = tuple(data)
    if(len(data) == 0):
        return ""
    else:
        return str(function(data[0])) + "," + myrecmap(function, data[1:])


def calculateSquare(n):
  return n*n

#Ex 3
def purifyIterate(numbers):
    integers = list(numbers)
    evenNum = []
    for number in integers:
        if (number % 2 == 0):
            evenNum.append(number)

    return evenNum

def purifyRecursion(numbers):
    numbersList = list(numbers)
    if (len(numbersList) == 0):
        return []
    else:
        if (numbersList[0] % 2 == 0):
            return [numbersList[0]] + purifyRecursion(numbersList[1:])
        return purifyRecursion(numbersList[1:])

#Ex 4
def productIteration(numbers):
    product = 1
    for integer in numbers:
        product *= integer
    
    return product

def productRecursion(numbers):
    if (len(numbers) == 0):
        return 1
    else:
        return numbers[0] * productRecursion(numbers[1:])

#Ex 5
def factorial(number):
    if (number == 0 or number == 1):
        return 1
    else:
        return number * factorial(number - 1)

#Ex 9
def palindromes(t):
    if (len(t) == 2  or len(t) == 1):
        return t[0]
    else:
        if (t[0] == t[-1]):
            return t[0] + str(palindromes(t[1:-1])) + t[-1]
        else:
            if (len(palindromes(t[:-1])) > len(palindromes(t[1:]))):
                return palindromes(t[:-1])
            else:
                return palindromes(t[1:])
            
#Ex 10
def quicksort(lst):
    items = list(lst)
    if (len(items) <= 1):
        return items
    pivot = items[int(len(items) / 2)]
    left = [x for x in items if x < pivot]
    middle = [x for x in items if x == pivot]
    right = [x for x in items if x > pivot]
    return quicksort(left) + middle + quicksort(right)

if __name__== "__main__":
    #print (Power(4, 5)) #answer: 1024
    alphabets = ['a', 'b', 'd', 'e', 'i', 'j', 'o']
    print(myrecfilter(filterVowels, alphabets))
    numbers = (1, 2, 3, 4)
    print(myrecmap(calculateSquare, numbers))
    numbersEx3 = (1, 44, 8, 3, 5, 90, 6, 53, 7)
    #print(purifyIterate(numbersEx3))
    print(list(purifyRecursion(numbersEx3)))
    numbersEx4 = (2, 7, 9, 10, 3)
    #print(productIteration(numbersEx4))
    print(productRecursion(numbersEx4))
    print(factorial(6))
    print(palindromes("aaabcbad"))
    lst = [3, 5, 2, 44, 15, 1, 8, 6, 99]
    print(quicksort(lst))