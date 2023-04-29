import numpy as np
from p12_01 import calculate_b
from p12_03 import predict
from p12_17 import compute_sigma

def var_covar_matrix(X):
    A = np.dot(X.T, X)
    return np.linalg.inv(A)

if __name__ == "__main__":
    # TODO: sth seems off with cov 
    y = [0.231, 0.107, 0.053, 0.129, 0.069, 0.030, 1.005, 0.559, 0.321, 2.948, 1.633, 0.934]
    x0 = [1 for i in range(len(y))]
    x1 = [740, 740, 740, 805, 805, 805, 980, 980, 980, 1235, 1235, 1235]
    x2 = [1.10, 0.62, 0.31, 1.10, 0.62, 0.31, 1.10, 0.62, 0.31, 1.10, 0.62, 0.31]
    X = np.stack((x0, x1, x2), axis=1)
    b = calculate_b(X=X, y=y)
    s = compute_sigma(X=X, y=y, b=b)
    A_inv = var_covar_matrix(X)
    b1 = A_inv[1][1] * s
    b2 = A_inv[2][2] * s
    print(f"B1 --> {b1}")
    print(f"B2 --> {b2}")
    
