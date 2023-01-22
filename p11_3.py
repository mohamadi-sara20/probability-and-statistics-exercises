from p11_1 import *
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    x = [0,0,0,15,15,15,30,30,30,45,45,45,60,60,60,75,75,75]
    y = [8,6,8,12,10,14,25,21,24,31,33,28,44,39,42,48,51,44]
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    b1 = estimate_slope(x=x, mean_x=mean_x, y=y, mean_y=mean_y)
    b0 = estimate_intercept(b1=b1, mean_x=mean_x, mean_y=mean_y)
    # (a)
    print(f"B1: {b1} and B0: {b0}")
    # (b)
    plt.scatter(x, y)
    y_pred = [b1*x+b0 for x in x]
    plt.plot(x, y_pred, color="r", linestyle='-')
    plt.show()
    # (c)
    pred = b1 * 50 + b0
    print(f"μY|50: {pred}")
