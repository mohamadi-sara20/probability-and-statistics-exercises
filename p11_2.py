from p11_1 import *
import numpy as np

if __name__ == "__main__":
    x = [77,50,71,72,81,94,96,99,67]
    y = [82,66,78,34,47,85,99,99,68]
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    b1 = estimate_slope(x=x, mean_x=mean_x, y=y, mean_y=mean_y)
    b0 = estimate_intercept(b1=b1, mean_x=mean_x, mean_y=mean_y)
    # (a)
    print(f"B1: {b1} and B0: {b0}")
    # (b)
    pred = b1 * 85 + b0
    print(f"μY|85: {pred}")