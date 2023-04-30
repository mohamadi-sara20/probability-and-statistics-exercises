import numpy as np
from p12_01 import calculate_b
from p12_17 import compute_sigma
from p12_03 import predict


def calculate_R2_b(SSE, SST):
    return 1 - (SSE/SST)

def calculate_R2(SSR, SST):
    return SSR/SST

def calculate_SSR(y_hat, y):
    y_bar = np.mean(y)
    return np.sum(np.power(y_hat - y_bar, 2))

def calculate_SST(y):
    y_bar = np.mean(y)
    return np.sum(np.power(np.subtract(y, y_bar), 2))



if __name__ == "__main__":
    y = np.array([6.40, 15.05, 18.75, 30.25, 44.85, 48.94, 51.55, 61.50, 100.44, 111.42])
    x0 = [1 for i in range(len(y))]
    x1 = [1.32, 2.69, 3.56, 4.41, 5.35, 6.20, 7.12, 8.87, 9.80, 10.65]
    x2 = [1.15, 3.40, 4.10, 8.75, 14.82, 15.15, 15.32, 18.18, 35.19, 40.40]
    X = np.stack((x0, x1, x2), axis=1)
    b = calculate_b(X=X, y=y)
    SSE = compute_sigma(b=b, X=X, y=y)
    SST = calculate_SST(y)
    

    y_hat = np.zeros((y.shape[0], 1),  dtype=np.float64)
    for i in range(y.shape[0]):
        y_hat[i][0] = predict(X=X[i], b=b)

    SSR = calculate_SSR(y_hat=y_hat, y=y)
    r2 = calculate_R2(SSR=SSR, SST=SST)
    r2_b = calculate_R2_b(SSE=SSE, SST=SST)

    print("SST: ", SST)
    print("SSE: ", SSE)
    print("SSR: ", SSR)
    print(f"R2: {r2}")
    print(f"R2 method b: {r2_b}")
    
    