import numpy as np
from p12_01 import calculate_b
from p12_03 import predict
from p12_17 import compute_sigma


if __name__ == "__main__":
    y = [6.40, 15.05, 18.75, 30.25, 44.85, 48.94, 51.55, 61.50, 100.44, 111.42]
    x0 = [1 for i in range(len(y))]
    x1 = [1.32, 2.69, 3.56, 4.41, 5.35, 6.20, 7.12, 8.87, 9.80, 10.65]
    x2 = [1.15, 3.40, 4.10, 8.75, 14.82, 15.15, 15.32, 18.18, 35.19, 40.40]
    X = np.stack((x0, x1, x2), axis=1)
    b = calculate_b(X=X, y=y)    
    print(compute_sigma(X, b, y))
    