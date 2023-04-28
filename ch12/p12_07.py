import numpy as np
from p12_01 import calculate_b
from p12_03 import predict

if __name__ == "__main__":
    y = [84.33,87.80,82.20,78.21,78.44,80.01,83.53,79.46,75.22,76.58,77.90,78.80,80.67,86.60,78.20]
    x0 = [1 for i in range(len(y))]
    x1 = [603.40,582.50,556.20,594.60,558.90,575.20,580.10,451.20,404.00,484.00,452.40,448.40,334.80,320.30,350.30]
    x2 = [x**2 for x in x1]
    X = np.stack((x0, x1, x2), axis=1)
    b = calculate_b(X=X, y=y)
    print(f"The model: {b[0]:.4f} + {b[1]:.4f}x1 + {b[2]:.4f}x2")
    
    
