import numpy as np
from p13_05 import *
from p13_12 import compare, calculate_S


def calculate_Tukey_val(ybari, ybarj):
    return abs(ybari-ybarj)

def Tukey_critical_value(s, tuk_val, n1, n2):
    return tuk_val * (s/2 * 1/n1 * 1/n2)**0.5

if __name__ == "__main__":
    A = np.array([190, 266, 270])
    B = np.array([318,295, 271, 438, 402])
    C = np.array([390, 321, 396, 399])
    X = np.array([A, B, C], dtype=object)
    Diff = np.zeros(X.shape)
    N = A.shape[0] + B.shape[0] + C.shape[0]
    f_val = anova_unequqal(data=X)
    print(f"F_val of anova: {f_val}")
    AB = calculate_Tukey_val(np.mean(A), np.mean(B))
    AC = calculate_Tukey_val(np.mean(A), np.mean(C))
    BC = calculate_Tukey_val(np.mean(B), np.mean(C))

    SSA, nis, treatment_means = calculate_SSA_unequal(X)
    SSE = calculate_SSE(X, treatment_means)
    s = SSE/(N - X.shape[0])



    print("Tukey Critical Val 0.05: ", Tukey_critical_value(s=SSE, tuk_val=3.95, n1=A.shape[0], n2=B.shape[0]))
    print("Tukey Critical Val 0.01: ", Tukey_critical_value(s=SSE, tuk_val=5.43, n1=A.shape[0], n2=B.shape[0]))
    print("Comparison Value: ", AB)

    print("Tukey Critical Val 0.05: ", Tukey_critical_value(s=SSE, tuk_val=3.95, n1=A.shape[0], n2=C.shape[0]))
    print("Tukey Critical Val 0.01: ", Tukey_critical_value(s=SSE, tuk_val=5.43, n1=A.shape[0], n2=C.shape[0]))
    print("Comparison Value: ", AC)
    
    print("Tukey Critical Val 0.05: ", Tukey_critical_value(s=SSE, tuk_val=3.95, n1=B.shape[0], n2=B.shape[0]))
    print("Tukey Critical Val 0.01: ", Tukey_critical_value(s=SSE, tuk_val=5.43, n1=B.shape[0], n2=B.shape[0]))
    print("Comparison Value: ", BC)
     