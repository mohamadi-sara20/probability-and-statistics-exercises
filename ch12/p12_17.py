import numpy as np
from p12_01 import calculate_b
from p12_03 import predict


def compute_s(X, b, y):
    yhat = []
    for i in range(len(X)):
        yhat.append(predict(X[i], b))
    s = np.sum(np.power((np.array(y) - np.array(yhat)), 2)) / (len(y) - X.shape[1])
    return s

if __name__ == "__main__":
    y = [0.231, 0.107, 0.053, 0.129, 0.069, 0.030, 1.005, 0.559, 0.321, 2.948, 1.633, 0.934]
    x0 = [1 for i in range(len(y))]
    x1 = [740, 740, 740, 805, 805, 805, 980, 980, 980, 1235, 1235, 1235]
    x2 = [1.10, 0.62, 0.31, 1.10, 0.62, 0.31, 1.10, 0.62, 0.31, 1.10, 0.62, 0.31]
    X = np.stack((x0, x1, x2), axis=1)
    
    b = calculate_b(X=X, y=y)
    print(compute_s(X, b, y))
    