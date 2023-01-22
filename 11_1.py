import matplotlib.pyplot as plt
import numpy as np


x = [17.3, 19.3, 19.5, 19.7, 22.9, 23.1, 26.4, 26.8, 27.6, 28.1, 28.2, 28.7, 29.0, 29.6, 29.9, 29.9, 30.3, 31.3, 36.0, 39.5, 40.4, 44.3, 44.6, 50.4, 55.9]
y = [71.7, 48.3, 88.3, 75.0, 91.7, 100.0, 73.3, 65.0, 75.0, 88.3, 68.3, 96.7, 76.7, 78.3, 60.0, 71.7, 85.0, 85.0, 88.3, 100.0, 100.0, 100.0, 91.7, 100.0, 71.7]

#(a)

def estimate_slope(x, mean_x, y, mean_y):
    b1 = 0
    den = 0
    for i in range(len(x)):
        b1 += (x[i] - mean_x) * (y[i] - mean_y)
        den += (x[i] - mean_x) ** 2
    
    return b1 / den

def estimate_intercept(mean_y, b1, mean_x):
    return mean_y - (b1 * mean_x)

mean_x = np.mean(x)
mean_y = np.mean(y)
b1 = estimate_slope(x=x,y=y,mean_x=mean_x, mean_y=mean_y)
b0 = estimate_intercept(mean_y=mean_y, b1=b1, mean_x=mean_x)

print(f"B1: {b1} and B0: {b0}")

#(b)
pred = b1 * 30 + b0
print(f"μY|30: {pred}")

#(c)

def calculate_residuals(y, y_pred):
    return np.subtract(y, y_pred)
    
y_pred = []
for i in range(len(x)):
    y_pred.append(b1 * x[i] + b0)

residuals = calculate_residuals(y=y, y_pred=y_pred)
plt.scatter(x, residuals)
plt.axhline(y=0, color='r', linestyle='-')
plt.show()
