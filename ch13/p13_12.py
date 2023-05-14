import numpy as np
from p13_05 import *

def compare(X, W):
    nom = calculate_SSW(X, W)
    den = calculate_S(X)
    return nom / den


def calculate_SSW(X, W):
    Yi = np.sum(X, axis=1)
    nom = np.power(np.dot(W, Yi), 2)
    den = X.shape[1] * np.sum(np.power(W, 2))
    return nom/den


def calculate_S(X):
    means = np.mean(X, axis=1).reshape((X.shape[0], 1))
    n = X.shape[1]
    k = X.shape[0]
    return np.sum(np.power(X - means, 2)) / (k *(n-1))


if __name__ == "__main__":
    # # Book Example for sanity check
    # A = np.array([551, 457, 450, 731, 499, 632])
    # B = np.array([595, 580, 508, 583, 633, 517])
    # C = np.array([639, 615, 511, 573, 648, 677])
    # D = np.array([417, 449, 517, 438, 415, 555])
    # E = np.array([563, 631, 522, 613, 656, 679])
    # X = np.array([A, B, C, D, E], dtype=object)
    # W = np.array([1, 1, -1, 0, -1])
    # first_comp = compare(X, W)
    # print(first_comp)

    A = np.array([58.7, 61.4, 60.9, 59.1, 58.2])
    B = np.array([62.7, 64.5, 63.1, 59.2, 60.3])
    C = np.array([55.9, 56.1, 57.3, 55.2, 58.1])
    D = np.array([60.7, 60.3, 60.9, 61.4, 62.3])
    X = np.array([A, B, C, D], dtype=object)
    W1 = np.array([1, -3, 1, 1])
    first_comp = compare(X, W1)
    print(f"B vs A, C, D : {first_comp}")
    W2 = np.array([-1, 0, 2, -1])
    scond_comp = compare(X, W2)
    print(f"C vs A and D: {scond_comp}")
    W3 = np.array([1, 0, 0, -1])
    third_comp = compare(X, W3)
    print(f"A vs D: {third_comp}")

    # To see if f-value (hence the contrast) is significant, look up the critical value 
    # for f(1, N-k) dfs, that is, f(1, 20-4)
