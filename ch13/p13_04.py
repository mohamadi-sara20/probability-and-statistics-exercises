import numpy as np
from p13_01 import anova, is_significant

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

    fval = anova(X)
    is_significant(fval=fval, alpha=0.01, dfn=X.shape[1]-1, dfd=X.shape[1] * (X.shape[0] - 1))