import numpy as np
from scipy.spatial import distance
if __name__== "__main__":
    ROWS = 4
    COLS = 3
    X = np.array(np.random.randint(12, size= ROWS*COLS)).reshape(ROWS,COLS)
    Z = np.zeros((ROWS - 1, 1))
    print(X)
    index = 0
    while index < ROWS - 1:
        Z[index] = distance.pdist(X[[index, index+1], :], 'euclidean')
        index+=1
    
    print(Z)
