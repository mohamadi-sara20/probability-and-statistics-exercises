from p11_1 import *
from p11_15 import * 
import numpy as np
from scipy import stats

def calculate_b1_cint(theta, s, tvalue, Sxx):
    lb = theta - s * tvalue / math.sqrt(Sxx)
    up = theta + s * tvalue / math.sqrt(Sxx)
    return lb, up

def calculate_b0_cint(theta, s, tvalue, Sxx, x):
    lb = theta - s * tvalue * math.sqrt(np.sum(np.power(x,2))) / math.sqrt(len(x) * Sxx)
    up = theta + s * tvalue * math.sqrt(np.sum(np.power(x,2))) / math.sqrt(len(x) * Sxx)
    return lb, up

if __name__ == "__main__":
    x = [77,50,71,72,81,94,96,99,67]
    y = [82,66,78,34,47,85,99,99,68]
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    b1 = estimate_slope(x=x, mean_x=mean_x, y=y, mean_y=mean_y)
    b0 = estimate_intercept(b1=b1, mean_x=mean_x, mean_y=mean_y)
    y_pred = []
    for i in range(len(x)):
        y_pred.append(b1 * x[i] + b0)
    s = calculate_s(y,y_pred)
    b1_cint = []
    b0_cint = []
    df = len(x) - 2
    Sxx = calculate_Sxx(x=x, mean_x=mean_x)
    
    tsig = stats.t.isf(0.025, df)
    b1_lb, b1_up = calculate_b1_cint(theta=b1, s=s, tvalue=tsig, Sxx=Sxx)
    b0_lb, b0_up = calculate_b0_cint(theta=b0, s=s, tvalue=tsig, Sxx=Sxx, x=x)
    s2 = s**2
    print(f"S^2: {s2}")
    print(f"B1 Confidence Interval: ({b1_lb}, {b1_up})")
    print(f"B0 Confidence Interval: ({b0_lb}, {b0_up})")