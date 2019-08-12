#Ex 1.2
print(3+1) #answer: 4
print(3*3) #answer: 9
print(2 ** 3) #answer: 8
print("Hello, world!") #answer: Hello, world!

#Ex 1.3
print ('py' + 'thon') #answer: python
print ('py' * 3 + 'thon') #answer: pypypython
print ('py' - 'py') #answer: unsupported operand type(s) for -: 'str' and 'str'
print ('3' + 3) #answer: can only concatenate str (not "int") to str
print (3 * '3') #answer: 333
#print (a) #answer: name 'a' is not defined
a=3
print (a) #answer: 3

#Ex 1.4
print(1==1) #answer: True
print(1 == True) #answer: True
print(0 == True) #answer: False
print(0 == False) #answer: True
print(3 == 1 * 3) #answer: True
print((3 == 1) * 3) #answer: 0
print((3 == 3) * 4 + 3 == 1) #answer: False
print(3**5 >= 4**4) #answer: False

#Ex 1.5
print(5/3) #answer: 1.6666666666666667
print(5 % 3) #answer: 2
print(5.0 / 3) #answer: 1.6666666666666667
print(5 / 3.0) #answer: 1.6666666666666667
print(5.2 % 3) #answer: 2.2
print(2001 ** 200) #answer: 1775896810483121914350934797871501063452843428843794422323202530887281536545210629921129898113201749875234297340507804201761453596034016264189501186924066128377025843892373608427790859511135990682732202975330824797118808624727351608183194154557208730494440110429635650057431833674286462463508755276302896154336475782768613964332764108132533925570342220340698973761380541294970139762186212823359128790706292900765512137078550033912252338262922477518858757114840012576514724742388124595061301502222934806074032688691170880996881967426442947828261057852871032366879179996122216385870273020506079240103910728766397733398071775041745854959302025036249707279600400001

#Ex 1.6
print(2000.3 ** 200) #answer: Result too large
print(1.0 + 1.0 - 1.0) #answer: 1.0
print(1.0 + 1.0e20 - 1.0e20) #answer: 0.0

#Ex 1.7
name = "Karin"
print("Hello, "+ name)
 
#Ex 1.8
print(float(123)) #answer: 123.0
print(float('123')) #answer: 123.0
print(float('123.23')) #answer: 123.23
print(int(123.23)) #answer: 123
print(int('123.23')) #answer: invalid literal for int() with base 10: '123.23'
print(int(float('123.23'))) #answer: 123
print(str(12)) #answer: 12
print(str(12.2)) #answer: 12.2
print(bool('a')) #answer: True
print(bool(0)) #answer: False
print(bool(0.1)) #answer: True