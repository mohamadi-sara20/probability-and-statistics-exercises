import numpy as np
from p13_1 import anova, is_significant


def calculate_cochran(X):
    varX = np.var(X, ddof=1, axis=0)
    return max(varX) / np.sum(varX)
        

if __name__ == "__main__":
    X = np.array([[11,10,4],
                    [5,7,4],
                    [14,16,6],
                    [7,7,3],
                    [10,7,5],
                    [7,5,6],
                    [23, 10, 8],
                    [4,10,3], 
                    [11, 6, 7],
                    [11, 12, 3]])
    
    c_val = calculate_cochran(X)