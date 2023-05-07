import numpy as np
import scipy

def calculate_SSA(data):
    treatment_means = np.mean(data, axis=0)
    n = data.shape[0]
    grand_mean = np.mean(data)
    SSA = n * np.sum(np.power(treatment_means - grand_mean, 2))
    return SSA


def calculate_SSE(data):
    treatment_means = np.mean(data, axis=0)
    return np.sum(np.power(np.subtract(data, treatment_means), 2))


def calculate_ESSA(SSA, data):
    k = data.shape[1]
    return SSA/(k-1)

def calculate_ESSE(SSE, data):
    n, k = data.shape
    return SSE/ ((n-1) * k)


def anova(data):
    SSA = calculate_SSA(data)
    SSE = calculate_SSE(data)
    ESSA = calculate_ESSA(SSA, data)
    ESSE = calculate_ESSE(SSE, data)
    return ESSA / ESSE

def is_significant(fval, alpha, dfn, dfd):
    critical_val = scipy.stats.f.ppf(q=1-alpha, dfn=dfn, dfd=dfd)
    print('Critical Val: ', critical_val)
    print("F VALUE: ",  fval)
    if fval > critical_val:
        print("Means are significantly different")
    else: 
        print("No significant difference in means")

if __name__ == "__main__":
    X = np.array([[17.5,16.4,20.3,14.6,17.5,18.3],
              [16.9,19.2,15.7,16.7,19.2,16.2],
              [15.8,17.7,17.8,20.8,16.5,17.5],
              [18.6,15.4,18.9,18.9,20.5,20.1]])

    fval = anova(X)
    critical_val = is_significant(fval, 0.01, X.shape[1]-1, dfd=X.shape[1] * (X.shape[0] - 1))
    