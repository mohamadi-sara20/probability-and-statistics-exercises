import numpy as np
from p13_14 import calculate_Tukey_val
from p13_05 import *

def Tukey_critical_value(s, tuk_val, n):
    return tuk_val * (s/n)**0.5

if __name__ == "__main__":
    A = np.array([5.2, 4.7, 8.1, 6.2, 3 ])
    B = np.array([9.1, 7.1, 8.2, 6, 9.1])
    C = np.array([3.2, 5.8, 2.2, 3.1, 7.2])
    D = np.array([2.4, 3.4, 4.1, 1, 4 ])
    E =np.array([7.1, 6.6, 9.3, 4.2, 7.6])
    X = np.array([A, B, C, D, E], dtype=object)
                   
    SSA, nis, treatment_means = calculate_SSA_unequal(X)
    SSE = calculate_SSE(X, treatment_means)
    s = SSE/ (X.shape[0] * (A.shape[0]-1))
    
    AB = calculate_Tukey_val(np.mean(A), np.mean(B))
    AC = calculate_Tukey_val(np.mean(C), np.mean(A))
    AD = calculate_Tukey_val(np.mean(D), np.mean(A))
    AE = calculate_Tukey_val(np.mean(E), np.mean(A))

    print("AB: ", AB)
    print("AC: ", AC)
    print("AD: ", AD)
    print("AE: ", AE)

    BC = calculate_Tukey_val(np.mean(C), np.mean(B))
    BD = calculate_Tukey_val(np.mean(D), np.mean(B))
    BE = calculate_Tukey_val(np.mean(E), np.mean(B))
    print("BC: ", BC)
    print("BD: ", BD)
    print("BE: ", BE)


    CD = calculate_Tukey_val(np.mean(C), np.mean(D))
    CE = calculate_Tukey_val(np.mean(C), np.mean(E))
    print("CD: ", CD)
    print("CE: ", CE)

    DE = calculate_Tukey_val(np.mean(E), np.mean(D))
    print("DE: ", DE)
    
    tuk_val=Tukey_critical_value(s=s, tuk_val=4.24, n=A.shape[0])

    #TODO: Tukey needs an ordered list of means. This should be corrected. 

    

