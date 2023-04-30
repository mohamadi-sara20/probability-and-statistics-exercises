import numpy as np
from p12_01 import calculate_b
from p12_03 import predict
from p12_17 import compute_s


if __name__ == "__main__":
    y = [240, 236, 290, 274, 301, 316, 300, 296, 267, 276, 288, 261]
    x0 = [1 for i in range(len(y))]
    x1 = [25, 31, 45, 60, 65, 72, 80, 84, 75, 60, 50, 38]
    x2 = [24, 21, 24, 25, 25, 26, 25, 25, 24, 25, 25, 23]
    x3 = [91, 90, 88, 87, 91, 94, 87, 86, 88, 91, 90, 89]
    x4 = [100, 95, 110, 88, 94, 99, 97, 96, 110, 105, 100, 98]
    X = np.stack((x0, x1, x2, x3, x4), axis=1)
    b = calculate_b(X=X, y=y)
    print(compute_s(X, b, y))
    