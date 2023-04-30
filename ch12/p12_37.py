import numpy as np
from p12_01 import calculate_b
from p12_17 import compute_s
from p12_03 import predict
from p12_31 import calculate_SST, calculate_R2, calculate_SSR
import scipy


if __name__ == "__main__":
    # 
    y = np.array([240, 236, 290, 274, 301, 316, 300, 296, 267, 276, 288, 261])
    x0 = [1 for i in range(len(y))]
    x1 = [25, 31, 45, 60, 65, 72, 80, 84, 75, 60, 50, 38]
    x2 = [24, 21, 24, 25, 25, 26, 25, 25, 24, 25, 25, 23]
    x3 = [91, 90, 88, 87, 91, 94, 87, 86, 88, 91, 90, 89]
    x4 = [100, 95, 110, 88, 94, 99, 97, 96, 110, 105, 100, 98]
    X = np.stack((x0, x1, x2, x3, x4), axis=1)
    b = calculate_b(X=X, y=y)
    
    SST = calculate_SST(y)
    y_hat = np.zeros((y.shape[0], 1),  dtype=np.float64)
    for i in range(y.shape[0]):
        y_hat[i][0] = predict(X=X[i], b=b)
    SSR_total = calculate_SSR(y_hat=y_hat, y=y)
    
    X_removed = np.stack((x0, x3, x4), axis=1)
    b_removed = calculate_b(X=X_removed, y=y)
    y_hat_removed = np.zeros((y.shape[0], 1),  dtype=np.float64)
    for i in range(y.shape[0]):
        y_hat_removed[i][0] = predict(X=X_removed[i], b=b_removed)
    SSR_removed = calculate_SSR(y_hat=y_hat_removed, y=y)
    s = compute_s(X=X, y=y, b=b)
    f_val = ((SSR_total - SSR_removed)/2) / s
    print(f_val)
    # H0: B1 = B2 = 0 and H1: Neither of B1 and B2 zero
    # f-stat = R(B1 and B2 | B0, B3, B4) / s = (SSR - R(B0, B3, B4)) / s




   
 