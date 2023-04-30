import numpy as np
from p12_03 import predict
from p12_02 import calculate_b
from p12_08 import calculate_b_multiple_trials
from p12_25 import confidence_interval
from p12_17 import compute_s
from p12_20 import var_covar_matrix

if __name__ == "__main__":
    # multiple observations example. I treated it as a simple n observation case. 
    # df(s) would be 12 this way, n=15 and df= n - 2 - 1
    
    y_mo = np.array([[25.2,27.3,28.7],[29.8,31.1,27.8],[31.2,32.6,29.7],[31.7,30.1,32.3],[29.4,30.8,32.8]])
    x0_mo = [1 for i in range(len(y_mo))]
    x1_mo = [10.0, 15.0, 20.0, 25.0, 30.0]
    x2_mo = [x**2 for x in x1_mo]

    y = np.array([25.2,27.3,28.7, 29.8,31.1,27.8, 31.2,32.6,29.7, 31.7,30.1,32.3, 29.4,30.8,32.8])
    x0 = [1 for i in range(len(y))]
    x1 = [10.0,10,10,15,15, 15.0,20,20, 20.0,25,25, 25.0,30,30, 30.0]
    x2 = [x**2 for x in x1]
    
    X = np.stack((x0, x1, x2), axis=1)
    X_mo = np.stack((x0_mo, x1_mo, x2_mo), axis=1)

    b = calculate_b(X=X, y=y)
    b_mo = calculate_b_multiple_trials(X=X_mo, y=y_mo)
    s = compute_s(X=X, y=y, b=b)
    A = var_covar_matrix(X=X)
    print(f"The model: {b[0]:.4f} + {b[1]:.4f}x1 + {b[2]:.4f}x2")
    y_hat = predict(X=np.array([1, 19.5, 19.5**2]), b=b)
    y_hat_mo = predict(X=np.array([1, 19.5, 19.5**2]), b=b_mo)

    assert y_hat == y_hat_mo

    cibound = confidence_interval(s=s, x_in=np.array([1, 19.5, 19.5**2]), A=A, ta=1.782)
    print(f"CI:\nlb: {y_hat-cibound}, ub: {y_hat+cibound}")