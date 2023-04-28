import numpy as np
from p12_01 import calculate_b
from p12_03 import predict

if __name__ == "__main__":
    y = [1,4,5,3,2,3,4]
    x0 = [1 for i in range(len(y))]
    x1 = [0,1,2,3,4,5,6]
    x2 = [x**2 for x in x1]
    x3 = [x**3 for x in x1]
    X = np.stack((x0, x1, x2, x3), axis=1)
    b = calculate_b(X=X, y=y)
    print(f"The model: {b[0]:.4f} + {b[1]:.4f}x1 + {b[2]:.4f}x2 + {b[3]:.4f}x3")
    print(predict([1, 2, 2**2, 2**3], b))
    
