import numpy as np
from p12_1 import calculate_b

def predict(X, b):
    return np.dot(b, X)

if __name__ == "__main__":
    y = [85, 74, 76, 90, 85, 87, 94, 98, 81, 91, 76, 74]
    x0 = [1 for i in range(len(y))]
    x1 = [65, 50, 55, 65, 55, 70, 65, 70, 55, 70, 50, 55]
    x2 = [1, 7, 5, 2, 6, 3, 2, 5, 4, 3, 1, 4]
    X = np.stack((x0, x1, x2), axis=1)
    b = calculate_b(X=X, y=y)
    # a
    print(f"The model: {b[0]:.4f} + {b[1]:.4f}x1 + {b[2]:.4f}x2")
    # b 
    print(predict(np.array([1, 60, 4]), b))