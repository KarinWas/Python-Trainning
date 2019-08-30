class MySet:
    def __init__(self, items):
        self.set = {}
        index = 0
        for value in items:
            if (value not in self.set.values()):
                self.set[index] = value
                index += 1
    
    def __sub__(self, other):
        result = []
        for value in self.set.values():
            if (value not in other.set.values()):
                result.append(value)
        
        return result
    
    def union(self, other):
        result = (list(self.set.values())).copy()

        for value in other.set.values():
            if (value not in result):
                result.append(value)
        
        return result

    def intersection(self, other):
        result = []

        for value in self.set.values():
            if (value in other.set.values()):
                result.append(value)
        
        return result

    def __str__(self):
        return ("The set is: " + str(list(self.set.values())))

class Main:
    if __name__== "__main__":
        animals1 = ['cat', 'dog', 'goldfish', 'canary', 'cat']
        animals2 = ['cow', 'goldfish', 'cat', 'bird', 'fish']
        my = MySet(animals1)
        my2 = MySet(animals2)
        print(my) # answer: The set is: ['cat', 'dog', 'goldfish', 'canary']
        print(my - my2) # answer: ['dog', 'canary']
        print (my.union(my2)) #answer: ['cat', 'dog', 'goldfish', 'canary', 'cow', 'bird', 'fish']
        print (my.intersection(my2))
