
import numpy as np
from p12_01 import calculate_b
from p12_03 import predict
from p12_31 import calculate_R2
from p12_39 import calculate_R2_adj, calculate_SSR, calculate_SST
from p12_17 import compute_s
from p12_25 import confidence_interval
from p12_20 import var_covar_matrix
from random import uniform

def coef_of_var(s, y_bar):
    return (s**0.5 / y_bar) * 100

if __name__ == "__main__":
    y = np.array([193, 172, 33, 230, 91, 125])
    x0 = [1 for i in range(len(y))] 
    x1 = [1.6, 22, 33, 15.5, 43, 40]
    x2 = [851, 1058, 1357, 816, 1201, 1115]
    X_full = np.stack((x0, x1, x2), axis=1)
    b_full = calculate_b(X=X_full, y=y)

    y_hat_full = np.zeros((y.shape[0], 1),  dtype=np.float64)
    for i in range(y.shape[0]):
        y_hat_full[i][0] = predict(X=X_full[i], b=b_full)


    # remove x2 from the model
    X = np.stack((x0, x1), axis=1)
    b = calculate_b(X=X, y=y)

    y_hat = np.zeros((y.shape[0], 1),  dtype=np.float64)
    for i in range(y.shape[0]):
        y_hat[i][0] = predict(X=X[i], b=b)

    SSR = calculate_SSR(y=y, y_hat=y_hat)
    SST = calculate_SST(y=y)
    r2 = calculate_R2(SSR=SSR, SST=SST)
    SSE = compute_s(b=b, X=X, y=y)
    r2 = calculate_R2_adj(SSE=SSE, SST=SST, n=y.shape[0])  
    r2_adj = calculate_R2_adj(SSE=SSE, SST=SST, n=y.shape[0])
    coefv = coef_of_var(s=SSE, y_bar=np.mean(y))
    f_val = SSR / SSE

    cibound = 0
    for i in range(100000):
        x_in = np.random.uniform(low=0.5, high=13.3, size=(2,1))
        x_in[0] = 1
        ta = uniform(1.7, 2.3)
        cibound += confidence_interval(s=SSE, ta=ta, x_in=x_in, A=var_covar_matrix(X=X))




    print("===================== X3 Removed Model =====================")
    print("R2: ", r2)
    print("R2 Adj: ", r2_adj)
    print("S2: ", SSE)
    print("Coeff of Var: ", coefv)
    print("CI Average Length: ", cibound/100000)
    print("F value: ", f_val)




    # remove x2 from the model
    X = np.stack((x0, x2), axis=1)
    b = calculate_b(X=X, y=y)

    y_hat = np.zeros((y.shape[0], 1),  dtype=np.float64)
    for i in range(y.shape[0]):
        y_hat[i][0] = predict(X=X[i], b=b)

    SSR = calculate_SSR(y=y, y_hat=y_hat)
    SST = calculate_SST(y=y)
    r2 = calculate_R2(SSR=SSR, SST=SST)
    SSE = compute_s(b=b, X=X, y=y)
    r2 = calculate_R2_adj(SSE=SSE, SST=SST, n=y.shape[0])  
    r2_adj = calculate_R2_adj(SSE=SSE, SST=SST, n=y.shape[0])
    coefv = coef_of_var(s=SSE, y_bar=np.mean(y))
    f_val = SSR / SSE

    cibound = 0
    for i in range(100000):
        x_in = np.random.uniform(low=0.5, high=13.3, size=(2,1))
        x_in[0] = 1
        ta = uniform(1.7, 2.3)
        cibound += confidence_interval(s=SSE, ta=ta, x_in=x_in, A=var_covar_matrix(X=X))

    

    print("===================== X1 Removed Model =====================")
    print("R2: ", r2)
    print("R2 Adj: ", r2_adj)
    print("S2: ", SSE)
    print("Coeff of Var: ", coefv)
    print("CI Average Length: ", cibound/100000)
    print("F value: ", f_val)



    X_full = np.stack((x0, x1, x2), axis=1)
    b_full = calculate_b(X=X_full, y=y)

    y_hat_full = np.zeros((y.shape[0], 1),  dtype=np.float64)
    for i in range(y.shape[0]):
        y_hat_full[i][0] = predict(X=X_full[i], b=b_full)

    SSR_full = calculate_SSR(y=y, y_hat=y_hat_full)
    SST_full = calculate_SST(y=y)
    r2_full = calculate_R2(SSR=SSR_full, SST=SST_full)
    SSE_full = compute_s(b=b_full, X=X_full, y=y)
    r2_adj_full = calculate_R2_adj(SSE=SSE_full, SST=SST_full, n=y.shape[0])
    coefv_full = coef_of_var(s=SSE_full, y_bar=np.mean(y))
    f_val = SSR_full / SSE_full
    
    cibound_full = 0
    for i in range(100000):
        x_in = np.random.uniform(low=0.5, high=13.3, size=(3,1))
        x_in[0] = 1
        ta = uniform(1.5, 2.5)
        cibound_full += confidence_interval(s=SSE_full, ta=ta, x_in=x_in, A=var_covar_matrix(X=X_full))


    print("===================== Full Model =====================")
    print("R2: ", r2_full)
    print("R2 Adj: ", r2_adj_full)
    print("S2: ", SSE_full)
    print("Coeff of Var: ", coefv_full)
    print("CI Average Length: ", cibound_full/100000)
    print("F value: ", f_val)
