

import numpy as np
from p12_03 import predict
from p12_08 import compute_SSE, calculate_b_multiple_trials, compute_lof



if __name__ == "__main__":
    y = np.array([[77.4, 76.7, 78.2],[84.1, 84.5, 83.7],[88.9, 89.2, 89.7,],[94.8, 94.7, 95.9]])
    x1 = [150, 200, 250, 300]
    x2 = [x**2 for x in x1]
    x0 = [1 for i in range(len(x1))]
    X = np.stack((x0, x1, x2), axis=1)
    b = calculate_b_multiple_trials(X=X, y=y)
    print(f"The model: {b[0][0]:.4f} + {b[0][1]:.4f}x1 + {b[0][2]}x2")
    yhat = np.zeros((y.shape[0], 1),  dtype=np.float64)
    for i in range(y.shape[0]):
        yhat[i][0] = predict(X=X[i], b=b)
    SSE = compute_SSE(y, yhat)
    print(b[0][0] + b[0][1] * 225 + b[0][2] * (225**2))
    


