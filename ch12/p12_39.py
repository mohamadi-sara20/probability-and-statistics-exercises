
import numpy as np
from p12_01 import calculate_b
from p12_17 import compute_sigma
from p12_03 import predict
from p12_31 import calculate_SST, calculate_R2, calculate_SSR


def calculate_R2_adj(SSE, SST, n):
    return 1 - (SSE / (SST/ (n-1)))


if __name__ == "__main__":
    y = np.array([16.9,15.5,19.2,18.5,30.0,27.5,27.2,30.9,20.3,17.0,21.6,16.2,20.6,20.8,18.6,18.1,17.0,17.6,16.5,18.2,26.5,21.9,34.1,35.1,27.4,31.5,29.5,28.4,28.8,26.8,33.5,34.2,31.8,37.3,30.5,22.0,21.5,31.9])
    x0 = [1 for i in range(len(y))]
    x1 = [4.360,4.054,3.605,3.940,2.155,2.560,2.300,2.230,2.830,3.140,2.795,3.410,3.380,3.070,3.620,3.410,3.840,3.725,3.955,3.830,2.585,2.910,1.975,1.915,2.670,1.990,2.135,2.570,2.595,2.700,2.556,2.200,2.020,2.130,2.190,2.815,2.600,1.925]
    x2 = [2.73,  2.26,  2.56,  2.45,  3.70,  3.05,  3.54,  3.37,  3.90,  3.50,  3.77,  3.58,  2.73,  3.08,  2.71,  2.73,  2.41,  2.26,  2.26,  2.45,  3.08,  3.08,  3.73,  2.97,  3.08,  3.78,  3.05,  2.53,  2.69,  2.84,  2.69,  3.37,  3.70,  3.10,  3.70,  3.70,  3.64,  3.78]
    X = np.stack((x0, x1, x2), axis=1)
    b = calculate_b(X=X, y=y)
    
    y_hat = np.zeros((y.shape[0], 1),  dtype=np.float64)
    for i in range(y.shape[0]):
        y_hat[i][0] = predict(X=X[i], b=b)
    
    SSR = calculate_SSR(y=y, y_hat=y_hat)
    SST = calculate_SST(y=y)
    r2 = calculate_R2(SSR=SSR, SST=SST)

    print("R2", r2)

    SSE = compute_sigma(b=b, X=X, y=y)

    r2_adj = calculate_R2_adj(SSE=SSE, SST=SST, n=y.shape[0])
    print("R2 adjusted: ", r2_adj)


    f_val = (SSR/2) / SSE
    print("f val:", f_val)


    # adding x2 has improved both R2 and R2adj and decreased s2 