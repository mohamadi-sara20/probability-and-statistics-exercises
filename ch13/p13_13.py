import numpy as np
from p13_05 import *
from p13_12 import compare


if __name__ == "__main__":
   

    A = np.array([13.7, 23.0, 15.7, 25.5, 15.8, 14.8, 14.0, 29.4, 9.7, 14.0, 12.3, 12.3])
    B = np.array([6.2, 5.4, 5.0, 4.4, 5.0, 3.3, 16.0, 2.5, 1.6, 3.9, 2.5, 7.1])
    C = np.array([27.2, 16.8, 12.9, 14.9, 17.1, 13.0,  10.8, 13.5, 25.5, 14.2, 27.4, 11.5])
    D = np.array([18.2, 8.8, 14.5, 14.7, 17.1, 13.9, 10.6, 5.8, 7.3, 17.7, 18.3, 9.9])
    X = np.array([A, B, C, D], dtype=object)
    f_val = anova_unequqal(data=X)
    print(f"F_val of anova: {f_val}")
    W1 = np.array([1, -1, 0, 0])
    first_comp = compare(X, W1)
    print(f"1 vs 2: {first_comp}")
    W2 = np.array([0, 0, 1, -1])
    scond_comp = compare(X, W2)
    print(f"3 vs 4: {scond_comp}")

    # # To see if f-value (hence the contrast) is significant, look up the critical value 
    # # for f(1, N-k) dfs, that is, f(1, 36-4)
