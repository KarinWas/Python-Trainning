import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class OLS:
    def __init__(self):
        self.coefficient = None
        self.bias = None

    def fit(self, x , y):
        A = np.vstack([x, np.ones(len(x))]).T
        self.coefficient, self.bias = np.linalg.lstsq(A, y, rcond=None)[0]

    def predict(self, x):
        return self.coefficient * x + self.bias

    def __str__(self):
        return "The coefficient is: " + str(self.coefficient) + " and the bias is: " + str(self.bias)

class Main:
     if __name__ == "__main__":
        ols = OLS()
        x = np.array([0, 1, 2, 3])
        y = np.array([-1, 0.2, 0.9, 2.1])
        ols.fit(x, y)
        print(ols)
        df = pd.DataFrame({'X axis':x, 'Y axis':ols.predict(x)})
        df.plot(kind='scatter',x='X axis',y='Y axis', color='red')
        plt.show()
        #plt.plot(x, y, 'o', label='Original data', markersize=10)
        #plt.plot(x, ols.predict(x), 'r', label='Fitted line')
        #plt.legend()
        #plt.show()
        
        