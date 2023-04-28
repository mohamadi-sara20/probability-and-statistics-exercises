import numpy as np
from p12_1 import calculate_b
from p12_3 import predict

if __name__ == "__main__":
    y = [95, 77, 80, 100, 97, 70, 50, 80, 92, 84]
    x0 = [1 for i in range(len(y))]
    x1 = [42, 33, 33, 45, 39, 36, 32, 41, 40, 38]
    x2 = [272, 226, 259, 292, 311, 183, 173, 236, 230, 235]
    X = np.stack((x0, x1, x2), axis=1)
    b = calculate_b(X=X, y=y)
    # a
    print(f"The model: {b[0]:.4f} + {b[1]:.4f}x1 + {b[2]:.4f}x2")
    # b 
    print(predict(np.array([1, 35, 250]), b))