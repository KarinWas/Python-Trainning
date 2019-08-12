#Ex 2.1
print (range(5)) #answer: range(0,5)

for i in range(5):
    print(i)
    #answer: 0, 1, 2, 3, 4

print(type(range(5))) #answer: <class 'range'>

#Ex 2.2
#a
for i in range(101):
    print (i)

#b
for i in range (101):
    if(i % 7 == 0):
        print (i)

#c
for i in range (1,101):
    if ((i%5 == 0) and (i%3 !=0)):
        print (i)
        
#d
for i in range(2,21):
    print("The numbers that divid "+ str(i) +" are: ")
    for j in range (2,i):
        if (i%j == 0):
            print (j)
            
#Ex 2.3
MAXIMUM_RANGE_23 = 100
#a
countA = 0
while(countA <= MAXIMUM_RANGE_23):
    print(countA)
    countA += 1

#b
countB = 0
while(countB <= MAXIMUM_RANGE_23):
    if (countB % 7 == 0):
        print(countB)
    countB += 1
    
#Ex 2.5
MAXIMUM_RANGE_25 = 20
number_found = 0
x = 11
while (number_found <= MAXIMUM_RANGE_25):
    if ((x%5 == 0 ) and (x%7 == 0) and (x%11 ==0)):
        print(x)
        number_found +=1
    x += 1
    
#Ex 2.6
smallest_div = 12
counter = 1
while(counter <= 10):
    if (smallest_div % counter == 0):
        counter += 1
    else:
        smallest_div += 1

print ("The smallest number that is divisible by all integers in range 1-10 is: " + str(smallest_div))

#Ex 2.7
FLAG = 1
x = 103
print(x)
while(x != FLAG):
    if (x%2 == 0):
        x = x//2
    else:
        x = 3*x +1
    print(x)
