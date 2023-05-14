import numpy as np
from p13_01 import anova, is_significant

if __name__ == "__main__":
    X = np.array([[5.2,9.1,3.2,2.4,7.1],
                    [4.7,7.1,5.8,3.4,6.6],
                    [8.1,8.2,2.2,4.1,9.3],
                    [6.2,6.0,3.1,1.0,4.2],
                    [3.0,9.1,7.2,4.0,7.6]])

    fval = anova(X)
    is_significant(fval=fval, alpha=0.05, dfn=X.shape[1]-1, dfd=X.shape[1] * (X.shape[0] - 1))