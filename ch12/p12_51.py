

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
    y = np.array([812.52, 822.50, 1211.50, 1348.00, 1301.00, 2567.50, 2526.50, 2755.00, 4390.50 , 5581.50, 5548.00,6086.00, 5764.00, 8903.00])
    x1 = [1, 2, 3, 4, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    x0 = [1 for i in range(len(x1))]
    X = np.stack((x0, x1), axis=1)
    b = calculate_b(X=X, y=y)
    print(f"The model: {b[0]:.4f} + {b[1]:.4f} x1 ")

    x1_q = [1, 2, 3, 4, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    x2_q = [x**2 for x in x1_q]
    x0_q = [1 for i in range(len(x1_q))]
    X_q = np.stack((x0_q, x1_q, x2_q), axis=1)
    b_q = calculate_b(X=X_q, y=y)
    print(f"The model: {b_q[0]:.4f} + {b_q[1]:.4f} x1 + {b_q[2]:.4f} x2 ")

    print("================== Comparison ========================")
    y_hat = np.zeros((y.shape[0], 1),  dtype=np.float64)
    for i in range(y.shape[0]):
        y_hat[i][0] = predict(X=X[i], b=b)
    
    SSE = compute_s(b=b, X=X, y=y)

    y_q = np.zeros((y.shape[0], 1),  dtype=np.float64)
    for i in range(y.shape[0]):
        y_q[i][0] = predict(X=X_q[i], b=b_q)

    SSE_q = compute_s(b=b_q, X=X_q, y=y)

    print(f"s and s_q: {SSE} and {SSE_q}")


    SSR = calculate_SSR(y=y, y_hat=y_hat)
    SST = calculate_SST(y=y)
    r2 = calculate_R2(SSR=SSR, SST=SST)
    SSE = compute_s(b=b, X=X, y=y)


    SSR_q = calculate_SSR(y=y, y_hat=y_q)
    r2_q = calculate_R2(SSR=SSR_q, SST=SST)
    SSE = compute_s(b=b_q, X=X_q, y=y)


    print(f"R2 and R2_q: {r2} and {r2_q}")

    ## PRESS still left to compute. 