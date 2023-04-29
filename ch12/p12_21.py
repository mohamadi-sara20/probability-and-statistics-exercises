import numpy as np
from p12_01 import calculate_b
from p12_03 import predict
from p12_17 import compute_sigma
from p12_20 import var_covar_matrix

if __name__ == "__main__":
    y = [240, 236, 290, 274, 301, 316, 300, 296, 267, 276, 288, 261]
    x0 = [1 for i in range(len(y))]
    x1 = [25, 31, 45, 60, 65, 72, 80, 84, 75, 60, 50, 38]
    x2 = [24, 21, 24, 25, 25, 26, 25, 25, 24, 25, 25, 23]
    x3 = [91, 90, 88, 87, 91, 94, 87, 86, 88, 91, 90, 89]
    x4 = [100, 95, 110, 88, 94, 99, 97, 96, 110, 105, 100, 98]
    X = np.stack((x0, x1, x2, x3, x4), axis=1)
    b = calculate_b(X=X, y=y)
    s = compute_sigma(X=X, y=y, b=b)
    A_inv = var_covar_matrix(X)    
    b2 = A_inv[2][2] * s
    print(f"B2 --> {b2}")
    print(f"Cov B1:B4 --> {A_inv[1][4]}")
    print(f"Cov B1:B4 --> {A_inv[4][1] * s}")
    
