from p11_15 import * 
from scipy import stats
import matplotlib.pyplot as plt

def calculate_b1_from_origin(x, y):
    den = np.sum(np.power(x, 2))
    nom = 0
    for i in range(len(x)):
        nom += x[i] * y[i]
    return nom/den

def estimate_var(y, y_pred):
    return np.sum(np.power(np.subtract(y, y_pred), 2)) / (len(y) - 1)

if __name__ == "__main__":
    x = [2,15,30,10,20]   
    y = [7,50,100,40,70 ]
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    b1 = calculate_b1_from_origin(x, y)
    print(f"Slope from origin: {b1}")
    y_pred = []
    for i in range(len(x)):
        y_pred.append(b1 * x[i])
    
    s = calculate_s(y, y_pred)
    
    # estimator of population variance
    s2 = estimate_var(y, y_pred)
    print(f"Variance: {s2}")
    
    Sxx = calculate_Sxx(x, mean_x)
    df = len(x) - 1
    tsig = stats.t.isf(0.025, df)
    lb = b1 - tsig * s / math.sqrt(Sxx)
    up = b1 + tsig * s / math.sqrt(Sxx)
    
    
    print(f"B Confidence Interval: ({lb}, {up})")
    
    y_pred_up = []
    for i in range(len(x)):
        y_pred_up.append(up * x[i])
    
    y_pred_lb = []
    for i in range(len(x)):
        y_pred_lb.append(lb * x[i])
        
    
    plt.scatter(x, y)
    plt.plot(x, y_pred_up, color='g')
    plt.plot(x, y_pred, color='r')
    plt.plot(x, y_pred_lb, color='b')
    plt.show()
    
    