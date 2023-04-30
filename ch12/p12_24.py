import numpy as np
from p12_01 import calculate_b
from p12_19 import compute_sigma
from p12_20 import var_covar_matrix
import scipy

if __name__ == "__main__":
    y = [6.40, 15.05, 18.75, 30.25, 44.85, 48.94, 51.55, 61.50, 100.44, 111.42]
    x0 = [1 for i in range(len(y))]
    x1 = [1.32, 2.69, 3.56, 4.41, 5.35, 6.20, 7.12, 8.87, 9.80, 10.65]
    x2 = [1.15, 3.40, 4.10, 8.75, 14.82, 15.15, 15.32, 18.18, 35.19, 40.40]
    X = np.stack((x0, x1, x2), axis=1)
    b = calculate_b(X=X, y=y)
    s = compute_sigma(X=X, y=y, b=b)
    A = var_covar_matrix(X=X)
    t_val = (b[1]-2)/(s**0.5 * (A[1][1])**0.5)
    print(f"t-value for B2==0: {t_val}")
    print("p-val for B2==0", scipy.stats.t.sf(abs(t_val), df=len(y) - 3)*2)
    