#Exercise 3
def happy_day(day):
    if day == "monday":
        return ":("
    if day != "monday":
        return ":D"

#Exercise 6
def Ex1(x, y):
    print (x+y)

def Ex5(name): 
    print("%s name has %d letters" % (name, len(name)))

def EX6():
    name = "John Smythe"
    print(name.lower())
    print(name)

if __name__ == "__main__":
    print(happy_day("sunday"))
    print(happy_day("monday"))
    Ex1(5,3)
    Ex5("Karin")
    EX6()