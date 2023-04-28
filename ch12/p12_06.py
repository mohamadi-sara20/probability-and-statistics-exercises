import numpy as np
from p12_01 import calculate_b
from p12_03 import predict

if __name__ == "__main__":
    y = [16, 26, 41, 62, 88, 119]
    x0 = [1 for i in range(len(y))]
    x1 = [35, 50, 65, 80, 95, 110]
    x2 = [x**2 for x in x1]
    X = np.stack((x0, x1, x2), axis=1)
    b = calculate_b(X=X, y=y)
    print(f"The model: {b[0]:.4f} + {b[1]:.4f}x1 + {b[2]:.4f}x2")
    print(predict([1, 70, 70**2], b))
    
