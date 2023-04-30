import numpy as np
from p12_01 import calculate_b
from p12_17 import compute_sigma
from p12_03 import predict
from p12_31 import calculate_SST, calculate_R2, calculate_SSR
import scipy


def calculate_b_orthogonal(X, y):
    b = np.zeros((1, X.shape[0]))
    b[0][0] = np.sum(y) / y.shape[0]
    for i in range(1, X.shape[0]):
        b[0][i] = np.dot(X[i], y)/ np.sum(np.power(X[i], 2))
    return b

def calculate_SSR_orthogonal(X, b):
    SSR = np.zeros((1, X.shape[0]-1))
    for i in range(1, X.shape[0]):
        SSR[0][i-1] = b[0][i]**2 * np.sum(np.power(X[i],2))
    return SSR

def calculate_SSE_orthogonal(y, y_hat):
    return np.sum(np.power(y-y_hat, 2)) 

def predict_orthogonal(X, b):
    return np.dot(b, X)

if __name__ == "__main__":
    # Is the intercept correct?
    y = np.array([7.6, 8.4, 9.2,10.3, 9.8, 11.1, 10.2, 12.6])
    x0 = [1 for i in range(len(y))]
    x1 = [-1,1,-1,-1,1,1,-1,1]
    x2 = [-1,-1,1, -1, 1, -1, 1,1,]
    x3 = [-1,-1,-1,1,-1,1,1,1]
    X = np.vstack((x0, x1, x2, x3))
    b = calculate_b_orthogonal(X=X, y=y)
    
    SST = calculate_SST(y)
    y_hat = np.zeros((y.shape[0], 1),  dtype=np.float64)
    SSR = calculate_SSR_orthogonal(X=X, b=b)
    total_SSR = np.sum(SSR)
    
    y_hat = predict_orthogonal(X=X, b=b)
    SSE = calculate_SSE_orthogonal(y=y, y_hat=y_hat)
    
    f_vals = []
    for i in range(SSR.shape[1]):
        f_vals.append(SSR[0][i] / (SSE/(y.shape[0] - X.shape[0])))
    
    print(f_vals)