import numpy as np
from p12_01 import calculate_b
from p12_17 import compute_sigma
from p12_03 import predict
from p12_31 import calculate_SST, calculate_R2, calculate_SSR
import scipy


if __name__ == "__main__":
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
    SSR = calculate_SSR(y_hat=y_hat, y=y)
    r2 = calculate_R2(SSR=SSR, SST=SST)
    s = compute_sigma(X=X, y=y, b=b)
    f_val = (SSR/4)/s
    critical_val = scipy.stats.f.ppf(q=0.01, dfn=4, dfd= len(y)-4-1)
    print("b2 p-val" + "is significant at 0.01" if f_val > critical_val else "is not significant at 0.01")

   
 