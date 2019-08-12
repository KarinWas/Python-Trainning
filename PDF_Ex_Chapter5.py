import math
if __name__== "__main__":
    #Ex 5.1
    a = 2
    b = 3
    a, b = b, a
    print ("a: " + str(a) +" b: " + str(b)) # answer: a: 3 b: 2

    #Ex 5.2
    #Zip-
    y = [1, 4, 7, 9, 3]
    x = [2, 5, 8, 9, 6]
    resultList = list(zip(x, y))
    print(list(zip([(1,2), (3,4)])))
    print (resultList) # answer: [(2, 1), (5, 4), (8, 7), (9, 9), (6, 3)]

    #Unzip-
    unzipX, unzipY = zip(*resultList)
    print('x = ', unzipX) # answer: x =  (2, 5, 8, 9, 6)
    print ('y = ', unzipY) # answer: y =  (1, 4, 7, 9, 3)
    
    #Ex 5.3
    a = [1, 4, 7, 9, 3]
    b = [2, 5, 8, 9, 6]

    distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(a, b)]))
    print ("The distance: ", distance) # answer: The distance:  3.4641016151377544