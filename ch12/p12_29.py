import numpy as np
from p12_01 import calculate_b
from p12_03 import predict
from p12_17 import compute_sigma
from p12_25 import confidence_interval, prediction_interval
from p12_20 import var_covar_matrix
import scipy.stats

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
    t_val_b1 = b[1]/(s**0.5 * (A[1][1])**0.5)
    t_val_b2 = b[2]/(s**0.5 * (A[2][2])**0.5)

    print("b1 p-val", scipy.stats.t.sf(abs(t_val_b1), df=len(y) - 3)*2)
    print("b2 p-val", scipy.stats.t.sf(abs(t_val_b2), df=len(y) - 3)*2)
