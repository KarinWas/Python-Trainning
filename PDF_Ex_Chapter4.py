#Ex 4.1
#a
def print_list(elements):
    print(elements)

#b
def print_reverse(elements):
    print(list(reversed(elements)))

#c
def len_function(elements):
    count = 0
    for index in elements:
        count += 1
    return count

#Ex 4.2
def set_first_elem_to_zero(l):
    l[0] = 0
    return l

#Ex 4.4
def set_index_value_to_zero(l, index):
    l[index] = 0

#Ex 4.7
def myfilter(age):
    if (age < 18):
        return False
    return True

#Ex 4.9
def longest_word_in_text(text):
    punctuation = [',', '?', '!', '.']
    words = text.split()
    word_length = 0
    longest_word = None
    
    for word in words:
        # remove punctuation
        word =  [x for x in word if x not in punctuation]
        # check if longest
        if (word_length < len(word)):
            longest_word = word
            word_length = len(word)

    return ''.join(longest_word)

#Ex 4.10
def collatz_as_list(n):
    FLAG = 1
    collatz = []
    x = n
    collatz.append(x)
    while(x != FLAG):
        if (x%2 == 0):
            x = x//2
        else:
            x = 3*x +1
        collatz.append(x)

    return collatz

def longest_collatz(n):
    maximumValue = 0
    maxNum = 0
    for x in range (1, n):
        if (len(collatz_as_list(x))> maximumValue):
            maximumValue = len(collatz_as_list(x))
            maxNum = x
    return maxNum

#Ex 4.11
def pivots (x, y):
    output_list =[]
    for value in y:
        if (value < x):
            output_list.append(value)
            y.remove(value)
    output_list.append(x)
    for value in y:
        output_list.append(value)

    return output_list

#Ex 4.12
def primes(n):
    primelist = lambda n : [x for x in range(2, n) if not 0 in map(lambda z : x % z, range(2,x))]

    return (primelist(n))

if __name__== "__main__":
    animals = ['cat', 'dog', 'fish', 'bison']
    names = ['Eli', 'Karin', 'Dana', 'Eden']
    print_list(animals)
    print_reverse(animals)
    print(len_function(animals))

    #Ex 4.2
    b = animals
    b[1] = 'cow'
    print (animals) #dog changed to cow because both b and animals point to the same place
    print(b)

    c= animals[:]
    c[2] = 'donkey'
    print (animals) #didn't changed because c is a copy of animals = new variable
    print (c)

    print(set_first_elem_to_zero(animals))
    print(animals) # the original list also changed

    #Ex 4.3
    a = [[]] * 3
    b = [[] for _ in range(3)]

    print (a)
    print (b)

    #Ex 4.4
    print(names)
    set_index_value_to_zero(names, 1)
    print(names)

    #Ex 4.7
    print ("With my filter: ")
    ages = [5, 12, 17, 18, 24, 32]
    adults = filter(myfilter, ages)
    for x in adults:
        print(x)
    print ("Now without filter: ")
    adults_noFilter = [x for x in ages if x >= 18]
    print (adults_noFilter)
    
    #Ex 4.8
    double_list = [[1,3], [5], [3,6]]
    no_sub_list = []
    for element in double_list:
        if len(element) >= 1:
            for sub_element in element:
                no_sub_list.append(sub_element)
        
    print (no_sub_list)

    #Ex 4.9
    print(longest_word_in_text("Hello, how was the football match earlier today???"))
    
    #Ex 4.10
    print(collatz_as_list(5)) # answer: [5, 16, 8, 4, 2, 1]
    print(longest_collatz(5)) # answer: 3

    #Ex 4.11
    print(pivots(3, [6, 4, 1, 7]))
    

    #Ex 4.12
    print(primes(12))