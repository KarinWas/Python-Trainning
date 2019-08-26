class Rational:
    def __init__(self, p, q):
        self.p = p
        self.q = q
    
    def __str__(self):
        return (str(self.p) + "/" + str(self.q))

    def greatest_common_divisor(self):
        x = self.p
        y = self.q
        while y != 0:
            (x, y) = (y, x % y)
        return (int(x))
    
    def __add__(self, other):
       firstNum = Rational(self.p * other.q , self.q * other. q)
       secondNum = Rational(other.p * self.q , self.q * other. q)
       newNum = Rational(firstNum.p + secondNum.p , self.q * other. q)
       gcd = newNum.greatest_common_divisor()
       newNum.p = int(newNum.p / gcd)
       newNum.q = int(newNum.q / gcd)
       return(newNum)
    
    def __sub__(self, other):
       firstNum = Rational(self.p * other.q , self.q * other. q)
       secondNum = Rational(other.p * self.q , self.q * other. q)
       newNum = Rational(firstNum.p - secondNum.p , self.q * other. q)
       gcd = newNum.greatest_common_divisor()
       newNum.p = int(newNum.p / gcd)
       newNum.q = int(newNum.q / gcd)
       return(newNum) 
    
    def __mul__(self, other):
        newNum = Rational(self.p * other.p , self.q * other.q)
        gcd = newNum.greatest_common_divisor()
        newNum.p = int(newNum.p / gcd)
        newNum.q = int(newNum.q / gcd)

        return(newNum)

    def __div__(self, other):
        newOtherNum = Rational(other.q, other.p)
        newNum = self.__mul__(newOtherNum)
        gcd = newNum.greatest_common_divisor()
        newNum.p = int(newNum.p / gcd)
        newNum.q = int(newNum.q / gcd)

        return(newNum)

    def __eq__(self, other):
        gcdSelf = self.greatest_common_divisor()
        gcdOther = other.greatest_common_divisor()
        return((self.p / gcdSelf == other.p / gcdOther) and (self.q / gcdSelf == other.q / gcdOther))

    def __float__(self):
        return (self.p / self.q)
    
if __name__== "__main__":
    number = Rational(4, 20)
    number2 = Rational(1, 3)
    print(number)
    print(number.greatest_common_divisor())
    print(number.__add__(number2))
    number3 = Rational(8,20)
    print(number3.__sub__(number2))
    print(number3.__mul__(number2))
    print(number3.__div__(number))
    number4 = Rational(2,6)
    print(number == number4)
    print(number2.__float__())