import random
class SparseVector:
    def __init__(self, lst):
        self.originalVec = lst
        self.vector = {}
        index = 0

        for value in lst:
            if (value != 0):
                self.vector[index] = value
            index +=1
    
    def __str__(self):
        return ("The sparse vector is: " + str(self.originalVec))

    def __add__(self, other):
        sum = other.vector
        if (isinstance(other, DenseVector)):
            for key in self.vector:
               sum[key] += self.vector[key]
        else:
            for key in self.vector:
                if (key not in other.vector.keys()):
                    sum[key] = self.vector[key]
                else:
                    sum[key] += self.vector[key]
            sum = dict(sorted(sum.items()))    
            sum = list(sum.values())
        return sum
    
    def __mul__(self, other):
        multiple = other.vector.copy()
        if (isinstance(other, DenseVector)):
            index = 0
            for index in range(len(other.vector)):
                if index not in self.vector.keys():
                    multiple[index] = 0
                else:
                    multiple[index] *= self.vector[index]
        else:
            for key in other.vector:
                if key in self.vector.keys():
                    multiple[key] *= self.vector[key]
                else:
                    del multiple[key]
            multiple = dict(sorted(multiple.items()))
            multiple = list(multiple.values())
        
        return multiple

class DenseVector:
    def __init__(self, lst):
        self.vector = lst

    def __str__(self):
        return ("The dense vector is: " + str(self.vector))
    
    def __add__(self, other):
        sumVectors = self.vector
        if (isinstance(other, SparseVector)):
            for key in other.vector:
                sumVectors[key] += other.vector[key]
            return sumVectors
        else:
            zipList = list(zip(self.vector, other.vector))
            for index in range(len(zipList)):
                sumVectors[index] = sum(zipList[index])
            return sumVectors
    
    def __mul__(self, other):
        multiple = self.vector.copy()
        if (isinstance(other, SparseVector)):
            index = 0
            for index in range(len(self.vector)):
                if index not in other.vector.keys():
                    multiple[index] = 0
                else:
                    multiple[index] *= other.vector[index]
        else:
            multiple = [a*b for a,b in zip(self.vector, other.vector)]
        
        return multiple

class Main:
    if __name__== "__main__":
        lstSparse = [0, 0, 3, 50, 21, 0, 8, 66]
        lstSparse2 = [1, 94, 47, 6, 0, 0, 10, 0]
        lstSparse3 = [0, 0, 22, 5, 11, 42, 0, 89]
        lstSparse4 = [20, 0, 0, 0, 13, 94, 0, 1]
        lstDense = [11, 49, 67, 33, 2, 25, 99, 14]
        lstDense2 = [25, 12, 95, 26, 10, 63, 4, 10]
        lstDense3 = [14, 13, 19, 9, 29, 8, 55, 1]
        lstDense4 = [44, 55, 66, 77, 88, 1, 22, 35]
        sparseVec = SparseVector(lstSparse)
        sparseVec2 = SparseVector(lstSparse2)
        sparseVec3 = SparseVector(lstSparse3)
        sparseVec4 = SparseVector(lstSparse4)
        denseVec = DenseVector(lstDense)
        denseVec2 = DenseVector(lstDense2)
        denseVec3 = DenseVector(lstDense3)
        denseVec4 = DenseVector(lstDense4)
        
        print(sparseVec)
        print(denseVec)

        #print(sparseVec + denseVec) # answer: [11, 49, 70, 83, 23, 25, 107, 80]
        #print(sparseVec * denseVec) # answer: [0, 0, 201, 1650, 42, 0, 792, 924]
        #print(sparseVec * sparseVec2) #answer: [141, 300, 80]
        #print(denseVec * sparseVec) #answer: [0, 0, 201, 1650, 42, 0, 792, 924]
        #print (denseVec * denseVec2) #answer: [275, 588, 6365, 858, 20, 1575, 396, 140]
        #print(sparseVec2 + sparseVec3) #answer: [1, 94, 69, 11, 11, 42, 10, 89]
        #print (denseVec4 + sparseVec4) # answer: [64, 55, 66, 77, 101, 95, 22, 36]
        #print (denseVec2 + denseVec3) # answer: [39, 25, 114, 35, 39, 71, 59, 11]
