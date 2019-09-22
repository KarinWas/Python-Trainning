import numpy as np
from scipy.spatial import distance
if __name__== "__main__":
    ROWS = 4
    COLS = 3
    X = np.array(np.random.randint(12, size= ROWS*COLS)).reshape(ROWS,COLS)
    Z = np.zeros((ROWS + ROWS - 2, 1))
    print(X)
    indexZ = 0
    index = 0
    while index < ROWS - 1:
        innerIndex = index + 1
        while innerIndex < ROWS:
            Z[indexZ] = distance.pdist(X[[index, innerIndex], :], 'euclidean')
            innerIndex += 1
            indexZ += 1
        index+=1
    
    print(Z)
