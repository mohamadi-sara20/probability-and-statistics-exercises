import numpy as np
from p12_01 import calculate_b
from p12_03 import predict
from p12_17 import compute_sigma
from p12_20 import var_covar_matrix

def confidence_interval(s, ta, x_in, A):
    return ta * s**0.5 * np.dot(np.dot(x_in.T, A), x_in)**0.5

def prediction_interval(s, ta, x_in, A):
    return ta * s**0.5 * (1+np.dot(np.dot(x_in.T, A), x_in))**0.5


if __name__ == "__main__":
    y = [0.231, 0.107, 0.053, 0.129, 0.069, 0.030, 1.005, 0.559, 0.321, 2.948, 1.633, 0.934]
    x0 = [1 for i in range(len(y))]
    x1 = [740, 740, 740, 805, 805, 805, 980, 980, 980, 1235, 1235, 1235]
    x2 = [1.10, 0.62, 0.31, 1.10, 0.62, 0.31, 1.10, 0.62, 0.31, 1.10, 0.62, 0.31]
    X = np.stack((x0, x1, x2), axis=1)
    b = calculate_b(X=X, y=y)
    s = compute_sigma(X=X, y=y, b=b)
    # t-value = 2.262156 (two-tailed, df=9)
    cibound = confidence_interval(s=s, ta=2.262156, x_in=np.array([1, 900, 1.00]),A=var_covar_matrix(X=X))
    pibound = prediction_interval(s=s, ta=2.262156, x_in=np.array([1, 900, 1.00]),A=var_covar_matrix(X=X))
    y_hat = predict(X=np.array([1, 900, 1.00]), b=b)
    print(f"CI:\nlb: {y_hat-cibound}, ub: {y_hat+cibound}")
    print(f"PI:\nlb: {y_hat-pibound}, ub: {y_hat+pibound}")