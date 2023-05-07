import numpy as np
from p13_1 import anova, is_significant

if __name__ == "__main__":
    X = np.array([[77,88,85],
                    [82,94,85],
                    [86,93,87],
                    [78,90,81],
                    [81,91,80],
                    [86,94,79],
                    [77,90,87],
                    [81,87,93]])

    fval = anova(X)
    is_significant(fval=fval, alpha=0.01, dfn=X.shape[1]-1, dfd=X.shape[1] * (X.shape[0] - 1))