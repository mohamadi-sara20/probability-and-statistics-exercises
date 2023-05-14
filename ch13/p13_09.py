import numpy as np
from p13_01 import is_significant
from p13_08 import anova_unequqal


def calculate_bartlett_unequal(X):
    varX = np.ones(X.shape)
    nis = np.ones(X.shape)
    for i in range(len(X)):
        varX[i] = np.var(X[i], ddof=1)
        nis[i] = len(X[i]) - 1
    sp = np.sum(np.dot(nis.T, varX)) / np.sum(nis)
    bval_n = 1
    for i in range(len(varX)):
        bval_n *= varX[i] ** nis[i]
    power = 1/(np.sum(nis))
    bval_n = bval_n**power
    return bval_n / sp

    
if __name__ == "__main__":
    zero = np.array([11.01, 12.09, 10.55, 11.26])
    eighty = np.array([11.38, 10.67, 12.33, 10.08])
    hundred_sixty  = np.array([11.02, 10.67, 11.50, 10.31])
    three_hundred_sixty = np.array([6.04, 10.31, 8.65, 8.30, 7.76, 9.48, 10.13, 8.89, 9.36])
    X = np.array([zero, eighty, hundred_sixty, three_hundred_sixty], dtype=object)
    fval, dfd, dfn = anova_unequqal(X)
    bval = calculate_bartlett_unequal(X)
    print("B Val: ", bval)