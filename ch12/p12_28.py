import numpy as np
from p12_01 import calculate_b
from p12_03 import predict
from p12_17 import compute_sigma
from p12_25 import confidence_interval, prediction_interval
from p12_20 import var_covar_matrix

if __name__ == "__main__":
    y = [193,230,172,91,113,125]
    x0 = [1 for i in range(len(y))]
    x1 = [1.6 ,15.5,22.0,43.0,33.0, 40.0]
    x2 = [851, 816, 1058, 1201, 1357, 1115]
    X = np.stack((x0, x1, x2), axis=1)
    b = calculate_b(X=X, y=y)
    s = compute_sigma(X=X, y=y, b=b)
    A = var_covar_matrix(X=X)

    print("Sample Variance: ", s)
    y_hat = predict(b=b, X=np.array([1, 20, 1000]))
    cibound = confidence_interval(s=s, x_in=np.array([1, 20, 1000]), A=A, ta=3.182446)
    pibound = prediction_interval(s=s, ta=3.182446, x_in=np.array([1, 20, 1000]), A=A)
    print(f"CI:\nlb: {y_hat-cibound}, ub: {y_hat+cibound}")
    print(f"PI:\nlb: {y_hat-pibound}, ub: {y_hat+pibound}")


