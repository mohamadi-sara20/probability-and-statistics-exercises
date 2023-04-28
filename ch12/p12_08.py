import numpy as np
from p12_03 import predict


def calculate_b_multiple_trials(X, y):
    y_bar = np.mean(y, axis=1)
    A = np.dot(X.T, X)
    g = np.dot(X.T, y_bar).reshape(X.shape[1], 1)
    b = np.squeeze(np.dot(np.linalg.inv(A), g))
    return b.reshape(1, b.shape[0])


def compute_SSE(y, yhat): 
    sse = np.sum(np.power(np.subtract(y, yhat),2))
    return sse

def compute_lof(y, SSE):
    y_bar = np.mean(y, axis=1)
    y_bar = np.reshape(y_bar, [y_bar.shape[0], 1])
    ESS = np.sum(np.power(np.subtract(y, y_bar), 2))

    # SSE df : n - #p --> 15 - 3 (12)
    # LoF df : 5 - #p --> 5 - 3 (2)
    # 12 = 2 + ? (SSE Pure df) --> SSE pure df = 10
    # See p. 420 of the book for a one parameter case
    return ((ESS - SSE) / 2) / (SSE / 10)


if __name__ == "__main__":
    y = np.array([[25.2,27.3,28.7],[29.8,31.1,27.8],[31.2,32.6,29.7],[31.7,30.1,32.3],[29.4,30.8,32.8]])
    x0 = [1 for i in range(len(y))]
    x1 = [10.0, 15.0, 20.0, 25.0, 30.0]
    x2 = [x**2 for x in x1]
    X = np.stack((x0, x1, x2), axis=1)
    b = calculate_b_multiple_trials(X=X, y=y)
    print(f"The model: {b[0][1]:.4f} + {b[0][1]:.4f}x1 + {b[0][2]:.4f}x2")
    yhat = np.zeros((y.shape[0], 1),  dtype=np.float64)
    for i in range(y.shape[0]):
        yhat[i][0] = predict(X=X[i], b=b)
    SSE = compute_SSE(y, yhat)
    print(compute_lof(y, SSE))
    
