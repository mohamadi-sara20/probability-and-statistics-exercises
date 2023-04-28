import numpy as np
from p12_1 import calculate_b
from p12_3 import predict

if __name__ == "__main__":
    y = [240, 236, 290, 274, 301, 316, 300, 296, 267, 276, 288, 261]
    x0 = [1 for i in range(len(y))]
    x1 = [25, 31, 45, 60, 65, 72, 80, 84, 75, 60, 50, 38]
    x2 = [24, 21, 24, 25, 25, 26, 25, 25, 24, 25, 25, 23]
    x3 = [91, 90, 88, 87, 91, 94, 87, 86, 88, 91, 90, 89]
    x4 = [100, 95, 110, 88, 94, 99, 97, 96, 110, 105, 100, 98]
    X = np.stack((x0, x1, x2, x3, x4), axis=1)
    b = calculate_b(X=X, y=y)
    print(f"The model: {b[0]:.4f} + {b[1]:.4f}x1 + {b[2]:.4f}x2 + {b[3]}x3 + {b[4]}x4")
    print(predict([1, 75, 24, 90, 98], b))
