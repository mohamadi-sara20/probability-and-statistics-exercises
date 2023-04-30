
import numpy as np
from p12_01 import calculate_b
from p12_17 import compute_s
from p12_03 import predict
from p12_31 import calculate_SST, calculate_R2, calculate_SSR
from p12_20 import var_covar_matrix
from p12_17 import compute_s

def calculate_R2_adj(SSE, SST, n):
    return 1 - (SSE / (SST/ (n-1)))


if __name__ == "__main__":
    y = np.array([34.5,33.3,30.4,32.8,35.0,29.0,32.5,29.6,16.8,19.2,22.6,24.4,20.7,25.1,18.8,15.8,17.4,15.6,17.3,20.8,22.2,16.5,21.3,20.7,24.1])
    x1 = ["sedan","sedan","sedan","sedan","sedan","sedan","sedan","sedan","van","van","van","van","van","van","van","van","van","SUV","SUV","SUV","SUV","SUV","SUV","SUV","SUV"]
    x11 = [int(bool(x=='van')) for x in x1]
    x12 = [int(bool(x=='SUV')) for x in x1]


    x2 = [75000,60000,88000,15000,25000,35000,102000,98000,56000,72000,14500,22000,66500,35000,97500,42000,65500,65000,55500,26500,11500,38000,77500,19500,87000]
    x3 = [87.5,87.5,78.0,78.0,90.0,78.0,90.0,87.5,87.5,90.0,87.5,90.0,78.0,90.0,87.5,78.0,78.0,78.0,87.5,87.5,90.0,78.0,90.0,78.0,90.0]
    x0 = [1 for i in range(len(y))]
    X = np.stack((x0, x11, x12, x2, x3), axis=1)
    b = calculate_b(X=X, y=y)


    print(f"The model: {b[0]:.4f} + {b[1]:.4f} van + {b[2]:.4f} SUV + {b[3]} Odometer + {b[4]} Octane")

    
    y_hat = np.zeros((y.shape[0], 1),  dtype=np.float64)
    for i in range(y.shape[0]):
        y_hat[i][0] = predict(X=X[i], b=b)
    
    SSR = calculate_SSR(y=y, y_hat=y_hat)
    SST = calculate_SST(y=y)
    r2 = calculate_R2(SSR=SSR, SST=SST)

    
    # which vehicle has better mileage? estimates are close. One way to look at it
    # is to find a CI for each parameter first. 
    # So let's get those. 
    A = var_covar_matrix(X=X)
    s = compute_s(X=X, y=y, b=b)
    for i in range(b.shape[0]):
        print(f"B{i} variance:  {(A[i][i] * s)**0.5}")