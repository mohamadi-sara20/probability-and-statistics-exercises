import numpy as np
from p13_14 import calculate_Tukey_val
from p13_05 import *

def Tukey_critical_value(s, tuk_val, n):
    return tuk_val * (s/n)**0.5

if __name__ == "__main__":
    A = np.array([25.6,24.3,27.9])
    B = np.array([25.2,28.6,24.7])
    C = np.array([20.8,26.7,22.2])
    D = np.array([31.6,29.8,34.3])
    X = np.array([A, B, C, D], dtype=object)

    f_val = anova_unequqal(data=X)
    print(f"F_val of anova: {f_val[0]}")

    # p = 5
    # df = 12 - 4 = 8
    rp = [3.261, 3.398, 3.475]
    SSA, nis, treatment_means = calculate_SSA_unequal(X)
    SSE = calculate_SSE(X, treatment_means)
    s = SSE/ (X.shape[0] * (A.shape[0]-1))
    Rp = []
    for i in rp:
        Rp.append(i * (s/3)**0.5)
    

    A_m = np.mean(A)
    B_m = np.mean(B)
    C_m = np.mean(C)
    D_m = np.mean(D)
    ms = [A_m, B_m, C_m, D_m]
    ms = sorted(ms)
    
    
    fc1 = ms[-1] - ms[0]
    if not fc1 > Rp[2]:
        # print(fc1 > Rp[2]) 
        print("first with smallest")
        fc2 = ms[-1] - ms[1]
        if not fc2 > Rp[1]: 
            # print(fc2 > Rp[1])
            print("first with second smallest")
            fc3 = ms[-1] - ms[1]
            if not fc3 > Rp[0]: 
                # print(fc3 > Rp[0])
                print("first with third smallest")


    sc1 = ms[-2] - ms[0]
    if not sc1 > Rp[1]:
        # print(sc1 > Rp[1])
        print("second with smallest")
        sc2 = ms[-2] - ms[1]
        if not sc2 > Rp[0]:
            # print(sc2 > Rp[0])
            print("second with second smallest")


    tc1 = ms[-3] - ms[0]
    if not tc1 > Rp[0]:    
        print("third with smallest")
    


    # AB = calculate_Tukey_val(np.mean(A), np.mean(B))
    # AC = calculate_Tukey_val(np.mean(C), np.mean(A))
    # AD = calculate_Tukey_val(np.mean(D), np.mean(A))

    # print("AB: ", AB)
    # print("AC: ", AC)
    # print("AD: ", AD)
    # print("AE: ", AE)

    # BC = calculate_Tukey_val(np.mean(C), np.mean(B))
    # BD = calculate_Tukey_val(np.mean(D), np.mean(B))
    # BE = calculate_Tukey_val(np.mean(E), np.mean(B))
    # print("BC: ", BC)
    # print("BD: ", BD)
    # print("BE: ", BE)


    # CD = calculate_Tukey_val(np.mean(C), np.mean(D))
    # CE = calculate_Tukey_val(np.mean(C), np.mean(E))
    # print("CD: ", CD)
    # print("CE: ", CE)

    # DE = calculate_Tukey_val(np.mean(E), np.mean(D))
    # print("DE: ", DE)
    
    # tuk_val=Tukey_critical_value(s=s, tuk_val=4.24, n=A.shape[0])

    

