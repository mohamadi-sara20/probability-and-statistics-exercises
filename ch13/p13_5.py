import numpy as np
from p13_1 import is_significant

def calculate_SSA_unequal(data):
    treatment_means = np.zeros((data.shape[0], 1))
    nis = np.zeros((data.shape[0], 1))
    total = 0
    for i in range(len(data)):
        treatment_means[i] = np.mean(data[i])
        total += np.sum(data[i])
        nis[i][0] = len(data[i])
    grand_mean = total / np.sum(nis)
    SSA = np.sum(np.dot(nis.T, np.power(treatment_means - grand_mean, 2)))
    return SSA, nis, treatment_means

def calculate_ESSA_unequal(SSA, data):
    k = data.shape[0]
    return SSA/(k-1)
    
def calculate_SSE(data, treatment_means):
    SSE = 0
    for i in range(len(data)):
        treatment_means[i] = np.mean(data[i])
    for i in range(len(treatment_means)):
        SSE += np.sum(np.power(data[i] - treatment_means[i], 2))  
    return SSE


def calculate_ESSE(SSE, k, nis):
    df = np.sum(nis) - k
    return SSE/df, df


def anova_unequqal(data):
    SSA, nis, treatment_means = calculate_SSA_unequal(data)
    SSE = calculate_SSE(data, treatment_means)
    ESSA = calculate_ESSA_unequal(SSA, data)
    ESSE, dfd = calculate_ESSE(SSE, len(data), nis)
    return ESSA/ESSE, dfd, len(nis) -1


if __name__ == "__main__":
    zero = np.array([11.01, 12.09, 10.55, 11.26])
    eighty = np.array([11.38, 10.67, 12.33, 10.08])
    hundred_sixty  = np.array([11.02, 10.67, 11.50, 10.31])
    three_hundred_sixty = np.array([6.04, 10.31, 8.65, 8.30, 7.76, 9.48, 10.13, 8.89, 9.36])
    X = np.array([zero, eighty, hundred_sixty, three_hundred_sixty], dtype=object)
    fval, dfd, dfn = anova_unequqal(X)
    is_significant(fval=fval, alpha=0.01, dfd=dfd, dfn=dfn)
    