

import numpy as np
import scipy
from p12_01 import calculate_b
from p12_03 import predict
from p12_31 import calculate_SST, calculate_R2, calculate_SSR
from p12_20 import var_covar_matrix
from p12_17 import compute_s

def calculate_R2_adj(SSE, SST, n):
    return 1 - (SSE / (SST/ (n-1)))


if __name__ == "__main__":
    y = np.array([157, -181, -253, 158, 75, 202, -451, 146, 89, -357, 522, 78, 5, -177, 123, 251, -56, 453, 288, -104])

    x1 = ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F']
    x11 = [int(bool(x=='F')) for x in x1]
    x2 = [1, 2, 4, 3, 4, 4, 1, 2, 1, 1, 1, 3, 2, 3, 2, 1, 1, 1, 1, 2]
    x3 = [45000, 55000, 45800, 38000, 75000, 99750, 28000, 39000, 54350, 32500, 36750, 42500, 34250, 36750, 24500, 27500, 18000, 24500, 88750, 19750]
    x0 = [1 for i in range(len(y))]
    X = np.stack((x0, x11, x2, x3), axis=1)
    b = calculate_b(X=X, y=y)

    print(f"The model: {b[0]:.4f} + {b[1]:.4f} Female + {b[2]:.4f} Family Members + {b[3]} Income ")



    # Note that categoralization could be done the other way around: x11 = [int(bool(x=='M')) for x in x1]
    # In which case, the intercept would change. 


    y_hat_full = np.zeros((y.shape[0], 1),  dtype=np.float64)
    for i in range(y.shape[0]):
        y_hat_full[i][0] = predict(X=X[i], b=b)

    SSR_full = calculate_SSR(y=y, y_hat=y_hat_full)
    SST_full = calculate_SST(y=y)
    r2_full = calculate_R2(SSR=SSR_full, SST=SST_full)
    SSE_full = compute_s(b=b, X=X, y=y)


    # Is Income explanatory? 
    X_removed = np.stack((x0, x11, x2), axis=1)
    b_removed = calculate_b(X=X_removed, y=y)
    print(b_removed)

    y_hat = np.zeros((y.shape[0], 1),  dtype=np.float64)
    for i in range(y.shape[0]):
        y_hat[i][0] = predict(X=X_removed[i], b=b_removed)

    SSR = calculate_SSR(y=y, y_hat=y_hat)
    SST = calculate_SST(y=y)
    r2 = calculate_R2(SSR=SSR, SST=SST)

    print(f"R2 Comparison: {r2} vs {r2_full}")


    print("================================= f value for estimations =================================")
    
    f_val_full = (SSR/3)/SST_full
    f_val = (SSR/2)/SST
    p_full = scipy.stats.f.cdf(f_val_full, 3, 16)
    p = scipy.stats.f.cdf(f_val, 2, 17)
    print("Full Model:\n", p_full)
    print("Partial:\n", p)