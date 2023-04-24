from p11_1 import *
import math

def calculate_s(y, y_pred):
    s = 0
    for i in range(len(y)):
        s += (y[i] - y_pred[i]) ** 2
    return math.sqrt(s / (len(y) - 2))

def calculate_Sxx(x, mean_x):
    Sxx = 0
    for i in x:
        Sxx += (i - mean_x) ** 2
    return Sxx

def linearity_ttest(b1, s, Sxx):
    return b1 * math.sqrt(Sxx) / s

if __name__ == "__main__":
    x = [17.3, 19.3, 19.5, 19.7, 22.9, 23.1, 26.4, 26.8, 27.6, 28.1, 28.2, 28.7, 29.0, 29.6, 29.9, 29.9, 30.3, 31.3, 36.0, 39.5, 40.4, 44.3, 44.6, 50.4, 55.9]
    y = [71.7, 48.3, 88.3, 75.0, 91.7, 100.0, 73.3, 65.0, 75.0, 88.3, 68.3, 96.7, 76.7, 78.3, 60.0, 71.7, 85.0, 85.0, 88.3, 100.0, 100.0, 100.0, 91.7, 100.0, 71.7]

    mean_x = np.mean(x)
    mean_y = np.mean(y)
    b1 = estimate_slope(x=x,y=y,mean_x=mean_x, mean_y=mean_y)
    b0 = estimate_intercept(mean_y=mean_y, b1=b1, mean_x=mean_x)
    y_pred = []
    for i in range(len(x)):
        y_pred.append(b1 * x[i] + b0)
    
    s = calculate_s(y,y_pred)
    Sxx = calculate_Sxx(x, mean_x) 
    print(linearity_ttest(b1, s, Sxx))