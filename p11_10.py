
from p11_1 import *
import numpy as np
import matplotlib.pyplot as plt
import math

if __name__ == "__main__":
    x = [1,2,2,3,5,5]
    y = [6350,5695,5750,5395,4985,4895]
    y = np.log(y) / np.log(100)
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    b1 = estimate_slope(x=x, mean_x=mean_x, y=y, mean_y=mean_y)
    b0 = estimate_intercept(b1=b1, mean_x=mean_x, mean_y=mean_y)
    # (a)
    print(f"B1: {b1} and B0: {b0}")
    c = math.exp(b0)
    d = math.exp(b1)
    pred = c * (d**10)
    print(f"μY|10: {pred}") 